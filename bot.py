#!/usr/bin/env python3
"""
✨ Modern 3xUI Telegram Bot - Add Client Only ✨
🔒 Uses config.json for settings
By t.me/ShayC21
"""

import logging
import requests
import urllib3
import json
from uuid import uuid4
from datetime import datetime, timedelta
from urllib.parse import quote, urlparse
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# === Load config ===
with open("config.json") as f:
    config = json.load(f)

XUI_HOST = config["XUI_HOST"]
USERNAME = config["USERNAME"]
PASSWORD = config["PASSWORD"]
BOT_TOKEN = config["BOT_TOKEN"]
API_HOSTNAME = urlparse(XUI_HOST).hostname
AUTHORIZED_USERS = {int(config["TG_ID"])}

# === Setup ===
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
session = requests.Session()

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

INBOUND_ID, CLIENT_NAME, CLIENT_DATA, CLIENT_EXPIRY = range(4)
user_data_temp = {}

# === Helpers ===
async def is_authorized(update: Update) -> bool:
    user_id = update.effective_user.id
    if user_id not in AUTHORIZED_USERS:
        logger.warning(f"Unauthorized access by user ID: {user_id}")
        await update.message.reply_text(
            "⛔ <b>Access Denied</b>\nYou are not authorized to use this bot.",
            parse_mode="HTML"
        )
        return False
    return True

def xui_login() -> bool:
    try:
        res = session.post(f"{XUI_HOST}/login", data={
            'username': USERNAME,
            'password': PASSWORD
        }, verify=False)
        logger.info(f"Login status: {res.status_code}, body: {res.text}")
        return res.status_code == 200 and res.json().get("success")
    except Exception as e:
        logger.error(f"Login error: {e}")
        return False

def generate_vless_uri(inbound_obj, client):
    uuid = client.get("id")
    email = client.get("email", "user")
    port = inbound_obj.get("port", 443)
    protocol = "vless"
    host = API_HOSTNAME or "example.com"

    stream_settings = json.loads(inbound_obj.get("streamSettings", "{}"))
    network = stream_settings.get("network", "tcp")
    security = stream_settings.get("security", "none")
    path = "/"

    if network == "ws":
        path = stream_settings.get("wsSettings", {}).get("path", "/")

    query = f"type={network}&security={security}&path={quote(path)}&host={host}"
    return f"{protocol}://{uuid}@{host}:{port}?{query}#{quote(email)}"

# === Handlers ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_authorized(update):
        return
    await update.message.reply_text(
        "🌐 <b>Client Management Bot</b> 🌐\n\n"
        "⚡️ Fast and reliable VPN client management\n\n"
        "🔹 <b>/addclient</b> - Create new VPN user\n\n"
        "🔒 Restricted access",
        parse_mode="HTML"
    )

async def addclient_start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not await is_authorized(update):
        return ConversationHandler.END
    await update.message.reply_text(
        "📥 Let's create a new client!\n\n"
        "🔢 <b>Step 1/4</b>: Enter Inbound ID:",
        parse_mode="HTML"
    )
    return INBOUND_ID

async def get_inbound_id(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user_data_temp[update.effective_chat.id] = {
            "inbound_id": int(update.message.text)
        }
        await update.message.reply_text(
            "👤 <b>Step 2/4</b>: Enter client name/email:",
            parse_mode="HTML"
        )
        return CLIENT_NAME
    except:
        await update.message.reply_text("❌ Invalid ID. Enter a number.")
        return INBOUND_ID

async def get_client_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data_temp[update.effective_chat.id]["email"] = update.message.text
    await update.message.reply_text(
        "📊 <b>Step 3/4</b>: Enter data limit in GB(0 = Unlimited):",
        parse_mode="HTML"
    )
    return CLIENT_DATA

async def get_client_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        gb = float(update.message.text)
        bytes_ = int(gb * 1024 ** 3) if gb > 0 else 0
        user_data_temp[update.effective_chat.id]["total_gb"] = bytes_
        await update.message.reply_text(
            "⏳ <b>Step 4/4</b>: Enter expiry in days(0 = Lifetime):",
            parse_mode="HTML"
        )
        return CLIENT_EXPIRY
    except:
        await update.message.reply_text("❌ Invalid value. Enter a number.")
        return CLIENT_DATA

async def get_client_expiry(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        data = user_data_temp[update.effective_chat.id]
        expiry_days = int(update.message.text)
        expiry_time = int((datetime.now() + timedelta(days=expiry_days)).timestamp() * 1000) if expiry_days > 0 else 0
        uuid = str(uuid4())
        sub_id = uuid[:16]

        payload = {
            "id": data["inbound_id"],
            "settings": json.dumps({
                "clients": [{
                    "id": uuid,
                    "email": data["email"],
                    "limitIp": 0,
                    "totalGB": data["total_gb"],
                    "expiryTime": expiry_time,
                    "enable": True,
                    "subId": sub_id,
                    "reset": 0
                }]
            })
        }

        if not xui_login():
            await update.message.reply_text("❌ Login failed.")
            return ConversationHandler.END

        r = session.post(f"{XUI_HOST}/panel/api/inbounds/addClient", json=payload, verify=False)
        if not (r.status_code == 200 and r.json().get("success")):
            await update.message.reply_text("❌ Failed to add client.")
            return ConversationHandler.END

        r2 = session.get(f"{XUI_HOST}/panel/api/inbounds/get/{data['inbound_id']}", verify=False)
        inbound_obj = r2.json().get("obj", {})
        settings = json.loads(inbound_obj.get("settings", "{}"))
        client = next((c for c in settings.get("clients", []) if c.get("id") == uuid), None)

        if client:
            vless = generate_vless_uri(inbound_obj, client)
            expiry_text = "Never" if expiry_days == 0 else (datetime.now() + timedelta(days=expiry_days)).strftime('%Y-%m-%d')
            size = "Unlimited" if data['total_gb'] == 0 else f"{data['total_gb'] / 1024 ** 3:.2f} GB"
            await update.message.reply_text(
                f"✅ <b>Client created!</b>\n"
                f"📧 Email: <code>{data['email']}</code>\n"
                f"🔑 UUID: <code>{uuid}</code>\n"
                f"💾 Limit: {size}\n"
                f"📅 Expiry: {expiry_text}\n"
                f"🔗 Link:\n<code>{vless}</code>",
                parse_mode="HTML"
            )
        else:
            await update.message.reply_text("⚠️ Client added but not listed.")
    except Exception as e:
        await update.message.reply_text(f"❌ Error: <code>{str(e)}</code>", parse_mode="HTML")
    finally:
        user_data_temp.pop(update.effective_chat.id, None)
        return ConversationHandler.END

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_data_temp.pop(update.effective_chat.id, None)
    await update.message.reply_text("❌ Operation cancelled.")
    return ConversationHandler.END

def main():
    if not xui_login():
        logger.error("Login to panel failed.")
        return

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    conv = ConversationHandler(
        entry_points=[CommandHandler("addclient", addclient_start)],
        states={
            INBOUND_ID: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_inbound_id)],
            CLIENT_NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_client_name)],
            CLIENT_DATA: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_client_data)],
            CLIENT_EXPIRY: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_client_expiry)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    app.add_handler(CommandHandler("start", start))
    app.add_handler(conv)

    logger.info("🤖 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
