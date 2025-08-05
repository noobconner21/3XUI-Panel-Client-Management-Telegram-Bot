# 3xUI Telegram Bot

A simple Telegram bot for managing 3xUI panel clients.

## Features

- **Client Management**: Create, delete, enable/disable clients
- **Traffic Monitoring**: Real-time usage statistics
- **Multi-Protocol Support**: VLESS, VMess, Trojan protocols
- **Admin Controls**: Secure administrative functions
- **Docker Ready**: Easy deployment with Docker

## Quick Start

### Using Docker (Recommended)

1. **Clone and setup**:
```bash
git clone <repository-url>
cd 3XUI-Panel-Client-Management-Telegram-Bot
cd docker
cp .env.example .env
```

2. **Configure** `.env` file:
```env
TELEGRAM_BOT_TOKEN=your_bot_token
XUI_PANEL_URL=https://your-panel-domain.com
XUI_USERNAME=your_username
XUI_PASSWORD=your_password
ADMIN_USER_IDS=123456789,987654321
```

3. **Deploy**:
```bash
docker-compose up -d
```

### Manual Installation

1. **Install dependencies**:
```bash
pip install -r requirements.txt
```

2. **Configure** `config/config.json`:
```json
{
  "telegram": {
    "bot_token": "your_bot_token",
    "admin_users": [123456789]
  },
  "xui": {
    "panel_url": "https://your-panel-domain.com",
    "username": "your_username",
    "password": "your_password"
  }
}
```

3. **Run**:
```bash
python src/main.py
```

## Bot Commands

### User Commands
- `/start` - Initialize bot
- `/help` - Show help message
- `/status` - Panel status
- `/clients` - List clients

### Admin Commands
- `/addclient <email>` - Add new client
- `/delclient <email>` - Delete client
- `/enable <email>` - Enable client
- `/disable <email>` - Disable client
- `/traffic` - Traffic statistics

## Project Structure

```
├── src/                 # Source code
│   ├── main.py         # Main bot application
│   ├── config_manager.py
│   ├── xui_client.py
│   ├── logger_setup.py
│   └── utils.py
├── config/             # Configuration
│   └── config.example.json
├── docker/             # Docker setup
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── .env.example
└── requirements.txt    # Dependencies
```

## Management

```bash
# View logs
docker-compose logs -f

# Restart bot
docker-compose restart

# Stop bot
docker-compose down

# Update and restart
docker-compose pull && docker-compose up -d
```
