# 🤖 3XUI Panel Client Management Bot

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Telegram](https://img.shields.io/badge/Telegram-Bot-26A5E4?style=for-the-badge&logo=telegram&logoColor=white)](https://core.telegram.org/bots)
[![Docker](https://img.shields.io/badge/Docker-Ready-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docker.com)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

**🚀 A powerful, modern Telegram bot for seamless 3XUI panel client management**

[✨ Features](#-features) • [🚀 Quick Start](#-quick-start) • [📖 Commands](#-commands) • [🛠️ Installation](#️-installation) • [🤝 Contributing](#-contributing)

</div>

---

## ✨ Features

### 🎯 **Core Client Management**
- 🆕 **Create Clients** - Instant client creation with smart configuration
- 👀 **View Details** - Comprehensive client information display  
- 🗑️ **Delete Clients** - Safe removal with confirmation prompts
- 📋 **List All** - Paginated client listings for easy browsing
- 🔍 **Smart Search** - Find clients by email, name, or keywords
- ⚡ **Bulk Operations** - Manage multiple clients simultaneously

### 📊 **Advanced Features**
- 🔒 **Multi-Protocol** - Support for VLESS, VMess, and Trojan protocols
- 🌐 **Inbound Management** - Handle multiple server configurations
- ⚙️ **Flexible Config** - Customizable client settings and limits
- 📱 **QR Codes** - Generate connection QR codes instantly
- 🔄 **Auto-Management** - Automated client operations

### 🛡️ **Security & Control**
- 🔐 **Admin Access** - Secure admin-only bot control
- 📝 **Activity Logs** - Detailed operation tracking
- 🚫 **Rate Limiting** - Protection against abuse
- 🔒 **Secure API** - Encrypted communication with 3XUI panel

---

## 🚀 Quick Start

### 🐳 **Docker Deployment (Recommended)**

```bash
# 📥 Clone the repository
git clone https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot

# 🔧 Setup environment
cd docker
cp .env.example .env
nano .env  # Configure your settings

# 🚀 Launch with Docker
docker-compose up -d
```

### 🐍 **Manual Installation**

```bash
# 📥 Clone and setup
git clone https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot

# 📦 Install dependencies
pip install -r requirements.txt

# 🔧 Configure environment
cp docker/.env.example .env
nano .env

# 🚀 Start the bot
python src/main.py
```

---

## 🔧 Configuration

### 📋 **Environment Setup**

Create your `.env` file with these essential variables:

```env
# 🤖 Telegram Bot Configuration
BOT_TOKEN=your_bot_token_from_botfather
ADMIN_USER_ID=your_telegram_user_id

# 🌐 3xUI Panel Settings  
XUI_HOST=https://your-panel-domain.com
XUI_USERNAME=admin
XUI_PASSWORD=your_secure_password

# ⚙️ Optional Settings
LOG_LEVEL=INFO
SESSION_TIMEOUT=3600
```

### 🔑 **Getting Your Credentials**

| What you need | How to get it | Bot to message |
|---------------|---------------|----------------|
| 🤖 **Bot Token** | Create a new bot | [@BotFather](https://t.me/botfather) |
| 👤 **User ID** | Get your Telegram ID | [@userinfobot](https://t.me/userinfobot) |
| 🌐 **Panel URL** | Your 3XUI web interface | `https://your-server-ip:port` |
    ---

## 📖 Commands

### 🎮 **Bot Commands**

<table>
<tr><th>Command</th><th>Description</th><th>Example Usage</th></tr>
<tr><td><code>🏁 /start</code></td><td>Initialize and welcome</td><td><code>/start</code></td></tr>
<tr><td><code>❓ /help</code></td><td>Show help menu</td><td><code>/help</code></td></tr>
<tr><td><code>➕ /create</code></td><td>Create new client</td><td><code>/create user@domain.com</code></td></tr>
<tr><td><code>📋 /list</code></td><td>List all clients</td><td><code>/list</code></td></tr>
<tr><td><code>ℹ️ /info</code></td><td>Get client details</td><td><code>/info user@domain.com</code></td></tr>
<tr><td><code>🗑️ /delete</code></td><td>Remove client</td><td><code>/delete user@domain.com</code></td></tr>
<tr><td><code>🔍 /search</code></td><td>Search clients</td><td><code>/search keyword</code></td></tr>
<tr><td><code>📊 /stats</code></td><td>System statistics</td><td><code>/stats</code></td></tr>
</table>

### 🛠️ **Advanced Usage**

**🆕 Create clients with custom settings:**
```
/create user@example.com --protocol vless --limit 100GB --expire 30d
```

**📊 Get detailed client info:**
```
/info user@example.com
```

**🔍 Smart search across clients:**
```
/search example  # Finds all clients matching "example"
```

---

## 🛠️ Installation

### 🐳 **Docker Installation (Recommended)**

#### 📋 **Prerequisites**
- Docker and Docker Compose installed
- 3XUI panel running and accessible
- Telegram bot token from [@BotFather](https://t.me/botfather)

#### 🚀 **Step-by-Step Setup**

1. **📥 Clone Repository**
```bash
git clone https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot
```

2. **🔧 Configure Environment**
```bash
cd docker
cp .env.example .env
```

Edit `.env` with your settings:
```env
# 🤖 Telegram Configuration
BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
ADMIN_USER_ID=123456789

# 🌐 3XUI Panel Configuration  
XUI_HOST=https://your-panel.com:2053
XUI_USERNAME=admin
XUI_PASSWORD=your_secure_password

# ⚙️ Optional Configuration
LOG_LEVEL=INFO
SESSION_TIMEOUT=3600
```

3. **🚀 Deploy Application**
```bash
docker-compose up -d
```

4. **✅ Verify Installation**
```bash
docker-compose logs -f xui-bot
```

### 🐍 **Manual Installation**

#### 📋 **Prerequisites**
- Python 3.11 or higher
- pip package manager
- Virtual environment (recommended)

#### 🚀 **Step-by-Step Setup**

1. **📥 Clone Repository**
```bash
git clone https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot
```

2. **🐍 Setup Python Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
venv\Scripts\activate
```

3. **📦 Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **🔧 Configure Environment** 
```bash
cp docker/.env.example .env
nano .env  # Edit with your settings
```

5. **🚀 Run the Bot**
```bash
python src/main.py
```

---

## 🏗️ Project Structure

```
🗂️ 3XUI-Panel-Client-Management-Telegram-Bot/
├── 📁 src/                     # 🐍 Source code
│   ├── 🚀 main.py              # Main application entry
│   ├── ⚙️ config_manager.py    # Configuration handler
│   ├── 📝 logger_setup.py      # Logging system
│   ├── 🌐 xui_client.py        # 3XUI API client
│   └── 🛠️ utils.py             # Helper utilities
├── 📁 docker/                  # 🐳 Container files
│   ├── 🐳 Dockerfile           # Container definition
│   ├── 🐙 docker-compose.yml   # Orchestration config
│   └── 📄 .env.example         # Environment template
├── 📦 requirements.txt         # Python dependencies
├── 📜 LICENSE                  # MIT License
└── 📖 README.md               # This documentation
```

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### 🔧 **Development Setup**

```bash
# 🍴 Fork and clone
git clone https://github.com/your-username/3XUI-Panel-Client-Management-Telegram-Bot.git
cd 3XUI-Panel-Client-Management-Telegram-Bot

# 🐍 Setup Python environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 📦 Install dependencies
pip install -r requirements.txt

# 🔧 Configure environment
cp docker/.env.example .env
# Edit .env with your settings

# 🚀 Run for development
python src/main.py
```

### 📝 **Contribution Guidelines**

1. 🍴 **Fork** the repository
2. 🌿 **Create** your feature branch (`git checkout -b feature/amazing-feature`)
3. ✨ **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. 📤 **Push** to the branch (`git push origin feature/amazing-feature`)  
5. 🔄 **Open** a Pull Request

---

## 🆘 Troubleshooting

### 🐛 **Common Issues**

<details>
<summary><strong>🤖 Bot not responding</strong></summary>

**Possible causes:**
- ❌ Incorrect bot token
- ❌ Bot not initialized with `/start`
- ❌ Wrong admin user ID
- ❌ Network connectivity issues

**Solutions:**
- ✅ Verify bot token is correct in `.env`
- ✅ Send `/start` command to initialize bot
- ✅ Check admin user ID is properly configured
- ✅ Test bot token with [@BotFather](https://t.me/botfather)
</details>

<details>
<summary><strong>🌐 3XUI connection failed</strong></summary>

**Possible causes:**
- ❌ Incorrect panel URL or credentials
- ❌ Network connectivity issues
- ❌ Firewall blocking access
- ❌ 3XUI panel not running

**Solutions:**
- ✅ Verify panel URL and credentials in browser
- ✅ Check network connectivity to panel
- ✅ Ensure 3XUI panel is running and accessible
- ✅ Check firewall settings and port access
</details>

<details>
<summary><strong>🚫 Permission denied</strong></summary>

**Possible causes:**
- ❌ User not configured as admin
- ❌ Incorrect admin user ID
- ❌ Bot doesn't have necessary permissions

**Solutions:**
- ✅ Verify admin user ID in configuration
- ✅ Get correct user ID from [@userinfobot](https://t.me/userinfobot)
- ✅ Ensure bot has proper Telegram permissions
</details>

<details>
<summary><strong>🐳 Docker issues</strong></summary>

**Possible causes:**
- ❌ Docker not installed or running
- ❌ Port conflicts
- ❌ Environment variables not set

**Solutions:**
- ✅ Install Docker and Docker Compose
- ✅ Check for port conflicts (`docker-compose ps`)
- ✅ Verify `.env` file configuration
- ✅ Restart Docker daemon if needed
</details>

### 📋 **Viewing Logs**

**🐳 Docker logs:**
```bash
# View bot logs
docker-compose logs -f xui-bot

# View all services
docker-compose logs -f
```

**🐍 Manual installation logs:**
```bash
# Real-time logs
tail -f logs/bot.log

# All logs
cat logs/bot.log
```

### 🔧 **Debug Mode**

Enable debug logging by setting in `.env`:
```env
LOG_LEVEL=DEBUG
```

---

## ❓ FAQ

<details>
<summary><strong>❓ Can multiple admins use the bot?</strong></summary>
Currently supports single admin configuration. Multi-admin support is planned for future releases.
</details>

<details>
<summary><strong>❓ Does it work with other x-ui panels?</strong></summary>
This bot is specifically designed for 3x-ui panels. Compatibility with other x-ui variants is not guaranteed.
</details>

<details>
<summary><strong>❓ Can I customize client configurations?</strong></summary>
Yes! The bot supports various client configuration options through command parameters and settings.
</details>

<details>
<summary><strong>❓ Is there a web interface?</strong></summary>
Currently, this is a Telegram-only bot. Web interface support may be considered for future versions.
</details>

<details>
<summary><strong>❓ How secure is the bot?</strong></summary>
The bot uses secure API communication, admin-only access control, and follows Telegram security best practices.
</details>

<details>
<summary><strong>❓ Can I run multiple instances?</strong></summary>
Yes, you can run multiple instances with different configurations for different panels or admin groups.
</details>

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

```
MIT License - you are free to:
✅ Use commercially
✅ Modify and distribute  
✅ Use privately
✅ Sublicense
```

---

## 💬 Support & Community

<div align="center">

[![GitHub Issues](https://img.shields.io/badge/🐛_Bug_Reports-GitHub_Issues-red?style=for-the-badge)](https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot/issues)
[![GitHub Discussions](https://img.shields.io/badge/💬_Discussions-GitHub_Discussions-blue?style=for-the-badge)](https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot/discussions)

**📞 Need help?** Open an issue • **💡 Have ideas?** Start a discussion • **🐛 Found a bug?** Report it

</div>

### 📞 **Getting Help**

1. **📖 Check Documentation** - Review this README and troubleshooting section
2. **🔍 Search Issues** - Look for existing solutions in [GitHub Issues](https://github.com/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot/issues)
3. **💬 Community Discussion** - Join discussions for feature requests and general questions
4. **🐛 Report Bugs** - Create detailed issue reports with logs and steps to reproduce

### 🤝 **Community Guidelines**

- 🎯 Be respectful and constructive
- 📝 Provide detailed information when reporting issues
- 🔍 Search for existing issues before creating new ones
- ✨ Contribute with code, documentation, or testing

---

## 🚀 Roadmap

### 📅 **Planned Features**

- 🔄 **v1.1**: Multi-admin support
- 📊 **v1.2**: Advanced traffic analytics  
- 📱 **v1.3**: Mobile app companion
- 🌐 **v1.4**: Web dashboard interface
- 🤖 **v1.5**: AI-powered client management
- 🔗 **v1.6**: Multi-panel support

### 🎯 **Current Focus**

- 🐛 Bug fixes and stability improvements
- 📚 Documentation enhancements
- 🔧 Configuration simplification
- 🚀 Performance optimizations

---

## 🙏 Acknowledgments

- 🎯 **3x-ui Project** - For the excellent panel software
- 🤖 **Telegram Bot API** - For the robust bot framework  
- 🐳 **Docker Community** - For containerization support
- 🐍 **Python Community** - For the amazing ecosystem
- 🌟 **Contributors** - For making this project better

---

## 📈 Stats

<div align="center">

![GitHub stars](https://img.shields.io/github/stars/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot?style=social)
![GitHub forks](https://img.shields.io/github/forks/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot?style=social)
![GitHub watchers](https://img.shields.io/github/watchers/noobconner21/3XUI-Panel-Client-Management-Telegram-Bot?style=social)

</div>

---

<div align="center">

**⭐ Found this helpful? Give it a star!**

**🚀 Ready to manage your 3XUI clients like a pro?**

[![Deploy Now](https://img.shields.io/badge/🚀_Deploy_Now-Get_Started-success?style=for-the-badge)](#-quick-start)
[![Documentation](https://img.shields.io/badge/📖_Read_Docs-Learn_More-blue?style=for-the-badge)](#-commands)
[![Contributing](https://img.shields.io/badge/🤝_Contribute-Help_Build-orange?style=for-the-badge)](#-contributing)

**Made with ❤️ for the 3XUI community**

</div>
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
