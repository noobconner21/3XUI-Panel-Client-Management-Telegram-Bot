# 3xUI VPN Client Management Telegram Bot

A secure Telegram bot to manage VPN clients on 3xUI panel — create users, set data limits, and expiry dates quickly via Telegram commands.

---

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Running the Bot](#running-the-bot)
- [Use](#use)
- [License](#license)
- [Contact](#contact)

---

## Features

- Add new VPN clients easily via Telegram chat
- Support for setting data limits (GB) and expiry days
- Generates VLESS connection URIs for clients
- Access restricted to authorized Telegram users only
- Securely connects to 3xUI panel API
- User-friendly step-by-step commands

---

## Prerequisites

- Python 3.8 or higher
- Telegram bot token from [BotFather](https://t.me/BotFather)
- Access to 3xUI panel API with username and password
- Linux or macOS terminal (Windows users can use WSL or Git Bash)

---

## Installation

### 1. Clone this repository

```bash
git clone https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot
chmod +x install.sh
./install.sh

```
## Use

```bash
python bot.py

```

### Telegram Bot Use

- /start — Display welcome message and help
- /addclient — Start the client creation process (4 steps)
- /cancel — Cancel current operation


## License

- This project is licensed under the MIT License.

## Contact

- Telegram : https://t.me/ShayC21


