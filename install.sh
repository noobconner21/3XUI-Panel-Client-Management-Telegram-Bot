#!/bin/bash

# Colors for pretty output
GREEN="\033[1;32m"
YELLOW="\033[1;33m"
RED="\033[1;31m"
CYAN="\033[1;36m"
RESET="\033[0m"
clear
echo "Wait..."
sleep 3
function prompt_input() {
  local prompt="$1"
  local varname="$2"
  local silent="$3"
  while true; do
    if [ "$silent" = true ]; then
      read -s -p "$prompt: " input
      echo
    else
      read -p "$prompt: " input
    fi
    if [ -z "$input" ]; then
      echo -e "${RED}Input cannot be empty. Please try again.${RESET}"
    else
      eval $varname="'$input'"
      break
    fi
  done
}

function prompt_numeric() {
  local prompt="$1"
  local varname="$2"
  while true; do
    read -p "$prompt: " input
    if [[ "$input" =~ ^[0-9]+$ ]]; then
      eval $varname="$input"
      break
    else
      echo -e "${RED}Please enter a valid numeric value.${RESET}"
    fi
  done
}

echo -e "${CYAN}=== V2Ray Bot Setup ===${RESET}"

prompt_input "Enter XUI Host URL (e.g. https://example.com:8080)" XUI_HOST false
prompt_input "Enter XUI Username" USERNAME false
prompt_input "Enter XUI Password" PASSWORD true
prompt_input "Enter Telegram Bot Token" BOT_TOKEN true
prompt_numeric "Enter your Telegram User ID (numeric)" TG_ID

echo -e "\n${YELLOW}Creating config.json...${RESET}"
cat > config.json <<EOF
{
  "XUI_HOST": "$XUI_HOST",
  "USERNAME": "$USERNAME",
  "PASSWORD": "$PASSWORD",
  "BOT_TOKEN": "$BOT_TOKEN",
  "TG_ID": $TG_ID
}
EOF
echo -e "${GREEN}config.json created successfully!${RESET}"

# Setup Python venv
if [ ! -d "venv" ]; then
  echo -e "${YELLOW}Creating Python virtual environment...${RESET}"
  python3 -m venv venv
fi

echo -e "${YELLOW}Activating virtual environment and installing requirements...${RESET}"
source venv/bin/activate
pip install --upgrade pip
pip install python-telegram-bot requests

echo -e "${GREEN}Setup complete!${RESET}"
echo -e "${CYAN}Run your bot with:${RESET}"
echo -e "source venv/bin/activate"
echo -e "python V2ray.py"
