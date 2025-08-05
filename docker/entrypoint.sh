#!/bin/bash
# Simple entrypoint for 3xUI Telegram Bot

set -e

# Start the bot
echo "Starting 3xUI Telegram Bot..."
exec python src/main.py
