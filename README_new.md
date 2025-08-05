# 🚀 Enhanced 3xUI VPN Client Management Telegram Bot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Telegram](https://img.shields.io/badge/Telegram-Bot%20API-blue.svg)
![3xUI](https://img.shields.io/badge/3xUI-Panel-green.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

A comprehensive, secure, and user-friendly Telegram bot for managing VPN clients on 3xUI panel with advanced features and enhanced security.

[Features](#-features) • [Installation](#-installation) • [Configuration](#-configuration) • [Usage](#-usage) • [Screenshots](#-screenshots) • [Contributing](#-contributing)

</div>

---

## 🌟 Features

### 🔥 Core Functionality
- **➕ Add Clients**: Create VPN clients with custom settings
- **🗑️ Remove Clients**: Safely delete clients with confirmation
- **📋 List Clients**: View all clients with detailed information
- **📊 Statistics**: Monitor inbound traffic and client counts
- **🔗 Multi-Protocol**: Support for VLESS, VMess, and Trojan
- **⚡ Real-time**: Instant client creation and management

### 🛡️ Security & Reliability
- **🔐 Access Control**: Restricted to authorized Telegram users
- **📝 Comprehensive Logging**: Detailed logs with rotation
- **🔄 Session Management**: Automatic login with session persistence
- **⚠️ Error Handling**: Robust error handling and user feedback
- **🚫 Rate Limiting**: Protection against abuse
- **🔍 Input Validation**: Thorough validation of all user inputs

### 💡 Enhanced User Experience
- **🎯 Interactive Menus**: Inline keyboards for easy navigation
- **📱 Mobile Friendly**: Optimized for mobile Telegram clients
- **🌍 Multi-language Ready**: Structured for easy localization
- **💾 Data Persistence**: Temporary data management during operations
- **🔔 Smart Notifications**: Contextual feedback and confirmations

### 🔧 Advanced Features
- **📈 Traffic Monitoring**: View data usage statistics
- **⏰ Expiry Management**: Flexible expiry date settings
- **🎛️ Protocol Detection**: Automatic protocol-specific URI generation
- **📋 Client Validation**: Prevent duplicate clients
- **🔄 Auto-reconnection**: Resilient connection handling

---

## 📋 Prerequisites

### System Requirements
- **Python**: 3.8 or higher
- **Operating System**: Linux, macOS, or Windows (WSL recommended)
- **Memory**: At least 512MB RAM
- **Storage**: 100MB free space

### External Dependencies
- **3xUI Panel**: Working 3xUI installation with API access
- **Telegram Bot**: Bot token from [@BotFather](https://t.me/BotFather)
- **Network**: Stable internet connection
- **SSL**: HTTPS access to your 3xUI panel (recommended)

---

## 🚀 Installation

### Method 1: Quick Install (Recommended)

```bash
# Clone the repository
git clone https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot

# Make installer executable and run
chmod +x install.sh
./install.sh
```

The installer will:
- ✅ Create Python virtual environment
- ✅ Install all dependencies
- ✅ Guide you through configuration
- ✅ Generate secure config file
- ✅ Test your setup

### Method 2: Manual Installation

```bash
# Clone repository
git clone https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt

# Copy and configure
cp config.example.json config.json
nano config.json  # Edit with your settings
```

---

## ⚙️ Configuration

### Basic Configuration

Create `config.json` with your settings:

```json
{
  "XUI_HOST": "https://your-server.com:2053",
  "USERNAME": "admin",
  "PASSWORD": "your_panel_password",
  "BOT_TOKEN": "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz",
  "TG_ID": 123456789
}
```

### Advanced Configuration

For power users, the bot supports advanced configuration options:

```json
{
  "XUI_HOST": "https://your-server.com:2053",
  "USERNAME": "admin",
  "PASSWORD": "your_panel_password",
  "BOT_TOKEN": "1234567890:ABCdefGHIjklMNOpqrsTUVwxyz",
  "TG_ID": [123456789, 987654321],
  "ADVANCED_SETTINGS": {
    "LOG_LEVEL": "INFO",
    "MAX_CLIENTS_PER_INBOUND": 100,
    "DEFAULT_DATA_LIMIT_GB": 50,
    "DEFAULT_EXPIRY_DAYS": 30,
    "ENABLE_TRAFFIC_MONITORING": true
  }
}
```

### Configuration Parameters

| Parameter | Type | Description | Example |
|-----------|------|-------------|---------|
| `XUI_HOST` | string | 3xUI panel URL with protocol and port | `https://panel.example.com:2053` |
| `USERNAME` | string | 3xUI panel admin username | `admin` |
| `PASSWORD` | string | 3xUI panel admin password | `secure_password123` |
| `BOT_TOKEN` | string | Telegram bot token from BotFather | `1234567890:ABC...` |
| `TG_ID` | int/array | Authorized Telegram user ID(s) | `123456789` or `[123, 456]` |

### Getting Required Information

1. **XUI_HOST**: Your 3xUI panel URL (e.g., `https://yourserver.com:2053`)
2. **USERNAME/PASSWORD**: Your 3xUI panel admin credentials
3. **BOT_TOKEN**:
   - Message [@BotFather](https://t.me/BotFather) on Telegram
   - Use `/newbot` command
   - Follow instructions to get your token
4. **TG_ID**:
   - Message [@userinfobot](https://t.me/userinfobot) on Telegram
   - It will reply with your user ID

---

## 🎮 Usage

### Starting the Bot

```bash
# Activate virtual environment (if not already active)
source venv/bin/activate

# Start the bot
python bot.py
```

### Available Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `/start` | Show main menu and welcome message | `/start` |
| `/addclient` | Add a new VPN client | `/addclient` |
| `/removeclient` | Remove an existing client | `/removeclient` |
| `/listclients` | List all clients with details | `/listclients` |
| `/stats` | Show inbound statistics | `/stats` |
| `/help` | Show detailed help information | `/help` |
| `/cancel` | Cancel current operation | `/cancel` |

### Step-by-Step Client Creation

1. **Start Process**: Send `/addclient` or use the interactive menu
2. **Select Inbound**: Choose from available inbound IDs
3. **Enter Email**: Provide a unique client identifier
4. **Set Data Limit**: Enter data limit in GB (0 = unlimited)
5. **Set Expiry**: Enter expiry period in days (0 = never expires)
6. **Get Connection**: Receive the connection URI and details

### Interactive Features

- **🎯 Inline Keyboards**: Click buttons for easy navigation
- **✅ Confirmations**: Safety confirmations for destructive actions
- **📊 Real-time Stats**: Live monitoring of your VPN infrastructure
- **🔍 Smart Search**: Find clients quickly by email/name

---

## 📱 Screenshots

### Main Menu
```
🌐 3xUI Management Bot v2.0 🌐

👋 Welcome, Username!

🚀 Enhanced Features:
• ➕ Add VPN clients with custom settings
• 🗑️ Remove clients safely
• 📋 List all clients with details
• 📊 View inbound statistics
• 🔗 Support for VLESS, VMess, Trojan

[➕ Add Client] [🗑️ Remove Client]
[📋 List Clients] [📊 Inbound Stats]
```

### Client Creation
```
✅ Client Created Successfully!

📧 Email: john.doe@example.com
🔑 UUID: 12345678-1234-1234-1234-123456789abc
🔗 Protocol: VLESS
💾 Data Limit: 50.00 GB
📅 Expires: 2024-09-05 15:30

🔗 Connection Link:
vless://12345678-1234-1234-1234-123456789abc@server.com:443?type=ws&security=tls&path=/ws&host=server.com#john.doe
```

---

## 📁 Project Structure

```
3XUI-Panel-Client-Management-Telegram-Bot/
├── 📄 bot.py                 # Main bot application
├── 📄 requirements.txt       # Python dependencies
├── 📄 install.sh            # Automated installer
├── 📄 config.example.json   # Configuration template
├── 📄 README.md             # This documentation
├── 📁 logs/                 # Log files (created automatically)
│   ├── bot.log              # General bot logs
│   └── errors.log           # Error logs
└── 📁 venv/                 # Virtual environment (created by installer)
```

---

## 🔧 Advanced Usage

### Running as a Service

Create a systemd service for production deployment:

```bash
# Create service file
sudo nano /etc/systemd/system/3xui-bot.service
```

```ini
[Unit]
Description=3xUI Telegram Bot
After=network.target

[Service]
Type=simple
User=your-username
WorkingDirectory=/path/to/3XUI-Panel-Client-Management-Telegram-Bot
Environment=PATH=/path/to/3XUI-Panel-Client-Management-Telegram-Bot/venv/bin
ExecStart=/path/to/3XUI-Panel-Client-Management-Telegram-Bot/venv/bin/python bot.py
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable 3xui-bot.service
sudo systemctl start 3xui-bot.service

# Check status
sudo systemctl status 3xui-bot.service
```

### Docker Deployment

```dockerfile
FROM python:3.9-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
CMD ["python", "bot.py"]
```

```bash
# Build and run
docker build -t 3xui-bot .
docker run -d --name 3xui-bot --restart unless-stopped 3xui-bot
```

### Monitoring and Logging

The bot creates detailed logs in the `logs/` directory:

- **`logs/bot.log`**: General application logs
- **`logs/errors.log`**: Error-specific logs

Monitor logs in real-time:
```bash
tail -f logs/bot.log
```

---

## 🛠️ Development

### Contributing

We welcome contributions! Please follow these steps:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Development Setup

```bash
# Clone for development
git clone https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot

# Install development dependencies
pip install -r requirements.txt
pip install black flake8 pytest  # Development tools

# Run code formatting
black bot.py

# Run linting
flake8 bot.py
```

### Code Style

- **Python**: Follow PEP 8 guidelines
- **Comments**: Use descriptive comments and docstrings
- **Logging**: Use appropriate log levels
- **Error Handling**: Always handle exceptions gracefully

---

## 🐛 Troubleshooting

### Common Issues

#### 1. "Failed to connect to 3xUI panel"
- ✅ Check your `XUI_HOST` URL format
- ✅ Verify SSL certificate if using HTTPS
- ✅ Ensure 3xUI panel is accessible
- ✅ Check firewall settings

#### 2. "Unauthorized access"
- ✅ Verify your Telegram ID in config
- ✅ Use [@userinfobot](https://t.me/userinfobot) to get correct ID
- ✅ Check bot token is correct

#### 3. "Login failed"
- ✅ Verify username and password
- ✅ Check 3xUI panel is running
- ✅ Test manual login to panel

#### 4. "Module not found" errors
- ✅ Activate virtual environment: `source venv/bin/activate`
- ✅ Install requirements: `pip install -r requirements.txt`

### Debug Mode

Enable detailed logging by modifying the config:
```json
{
  "ADVANCED_SETTINGS": {
    "LOG_LEVEL": "DEBUG"
  }
}
```

### Getting Help

- 📧 **Issues**: [GitHub Issues](https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot/issues)
- 💬 **Telegram**: [@ShayC21](https://t.me/ShayC21)
- 📚 **Documentation**: Check this README and code comments

---

## 📈 Changelog

### Version 2.0 (Enhanced Version)
- ✅ Complete rewrite with enhanced architecture
- ✅ Multi-protocol support (VLESS, VMess, Trojan)
- ✅ Interactive inline keyboards
- ✅ Comprehensive logging system
- ✅ Advanced error handling
- ✅ Client removal functionality
- ✅ Statistics and monitoring
- ✅ Input validation and security
- ✅ Session management
- ✅ Better documentation

### Version 1.0 (Original)
- ✅ Basic client addition
- ✅ VLESS URI generation
- ✅ Simple authorization

---

## 🔒 Security Considerations

- **🔐 Access Control**: Only authorized users can access the bot
- **📝 Logging**: All actions are logged for audit trails
- **🔒 SSL/TLS**: Use HTTPS for 3xUI panel connections
- **🛡️ Input Validation**: All user inputs are validated
- **⚠️ Error Handling**: Sensitive information is not exposed in errors
- **🔄 Session Management**: Automatic session renewal

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software.
```

---

## 🙏 Acknowledgments

- **Enhanced by**: [@ShayC21](https://t.me/ShayC21)
- **3xUI Panel**: Thanks to the 3xUI development team
- **Python Telegram Bot**: Built with [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot)

---

## 🌟 Star History

If this project helped you, please give it a ⭐!

---

<div align="center">

**Made with ❤️ for the community**

[⬆ Back to Top](#-enhanced-3xui-vpn-client-management-telegram-bot)

</div>
