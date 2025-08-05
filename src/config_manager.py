#!/usr/bin/env python3
"""
Configuration Manager for 3xUI Telegram Bot
Handles configuration loading, validation, and management.
"""

import json
import os
import sys
import logging
from typing import Dict, Any, Union, List

logger = logging.getLogger(__name__)


class ConfigManager:
    """Configuration manager with validation and fallbacks"""

    def __init__(self, config_file: str = "config/config.json"):
        self.config_file = config_file
        self.config = self._load_config()
        self._validate_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file with error handling"""
        # Try multiple possible locations
        possible_paths = [
            self.config_file,
            "config.json",
            "config/config.json",
            "../config/config.json"
        ]

        for path in possible_paths:
            if os.path.exists(path):
                self.config_file = path
                break
        else:
            logger.error(f"Configuration file not found in any of: {possible_paths}")
            sys.exit(1)

        try:
            with open(self.config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            logger.info(f"Configuration loaded from {self.config_file}")
            return config
        except json.JSONDecodeError as e:
            logger.error(f"Invalid JSON in config file: {e}")
            sys.exit(1)
        except Exception as e:
            logger.error(f"Error loading config: {e}")
            sys.exit(1)

    def _validate_config(self) -> None:
        """Validate required configuration fields"""
        required_fields = ["XUI_HOST", "USERNAME", "PASSWORD", "BOT_TOKEN", "TG_ID"]
        missing_fields = [field for field in required_fields if not self.config.get(field)]

        if missing_fields:
            logger.error(f"Missing required configuration fields: {missing_fields}")
            sys.exit(1)

        # Validate URL format
        if not self.config["XUI_HOST"].startswith(("http://", "https://")):
            logger.error("XUI_HOST must start with http:// or https://")
            sys.exit(1)

        # Validate Telegram user IDs
        tg_ids = self.config["TG_ID"]
        if isinstance(tg_ids, int):
            if tg_ids <= 0:
                logger.error("TG_ID must be a positive integer")
                sys.exit(1)
        elif isinstance(tg_ids, list):
            if not all(isinstance(uid, int) and uid > 0 for uid in tg_ids):
                logger.error("All TG_IDs must be positive integers")
                sys.exit(1)
        else:
            logger.error("TG_ID must be an integer or list of integers")
            sys.exit(1)

    def get(self, key: str, default: Any = None) -> Any:
        """Get configuration value with optional default"""
        return self.config.get(key, default)

    def get_authorized_users(self) -> set:
        """Get set of authorized Telegram user IDs"""
        tg_ids = self.config["TG_ID"]
        if isinstance(tg_ids, int):
            return {tg_ids}
        elif isinstance(tg_ids, list):
            return set(tg_ids)
        else:
            return set()

    def reload(self) -> None:
        """Reload configuration from file"""
        self.config = self._load_config()
        self._validate_config()
        logger.info("Configuration reloaded")

    def update(self, key: str, value: Any) -> None:
        """Update configuration value (runtime only)"""
        self.config[key] = value
        logger.info(f"Configuration updated: {key}")

    def save(self, backup: bool = True) -> None:
        """Save current configuration to file"""
        if backup and os.path.exists(self.config_file):
            backup_file = f"{self.config_file}.backup"
            os.rename(self.config_file, backup_file)
            logger.info(f"Configuration backed up to {backup_file}")

        try:
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, indent=2, ensure_ascii=False)
            logger.info(f"Configuration saved to {self.config_file}")
        except Exception as e:
            logger.error(f"Error saving configuration: {e}")
            raise
