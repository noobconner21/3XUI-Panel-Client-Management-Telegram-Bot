#!/usr/bin/env python3
"""
Logging Setup for 3xUI Telegram Bot
Configures comprehensive logging with file rotation and multiple handlers.
"""

import logging
import logging.handlers
import os
import sys
from datetime import datetime
from typing import Optional


def setup_logging(
    log_level: str = "INFO",
    log_dir: str = "logs",
    max_bytes: int = 10 * 1024 * 1024,  # 10MB
    backup_count: int = 5,
    console_output: bool = True
) -> logging.Logger:
    """
    Configure enhanced logging with file output and rotation

    Args:
        log_level: Logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
        log_dir: Directory for log files
        max_bytes: Maximum size of each log file before rotation
        backup_count: Number of backup files to keep
        console_output: Whether to output to console

    Returns:
        Configured logger instance
    """
    # Create logs directory
    os.makedirs(log_dir, exist_ok=True)

    # Convert log level string to constant
    numeric_level = getattr(logging, log_level.upper(), logging.INFO)

    # Create formatters
    detailed_formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )

    simple_formatter = logging.Formatter(
        '%(asctime)s - %(levelname)s - %(message)s',
        datefmt='%H:%M:%S'
    )

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Capture all levels, handlers will filter

    # Clear any existing handlers
    root_logger.handlers.clear()

    # Console handler
    if console_output:
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.setLevel(numeric_level)
        console_handler.setFormatter(simple_formatter)
        root_logger.addHandler(console_handler)

    # Main log file handler with rotation
    main_log_file = os.path.join(log_dir, 'bot.log')
    file_handler = logging.handlers.RotatingFileHandler(
        main_log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(detailed_formatter)
    root_logger.addHandler(file_handler)

    # Error log file handler
    error_log_file = os.path.join(log_dir, 'errors.log')
    error_handler = logging.handlers.RotatingFileHandler(
        error_log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(detailed_formatter)
    root_logger.addHandler(error_handler)

    # Security/access log file handler
    access_log_file = os.path.join(log_dir, 'access.log')
    access_handler = logging.handlers.RotatingFileHandler(
        access_log_file,
        maxBytes=max_bytes,
        backupCount=backup_count,
        encoding='utf-8'
    )
    access_handler.setLevel(logging.INFO)
    access_handler.setFormatter(detailed_formatter)

    # Create access logger
    access_logger = logging.getLogger('access')
    access_logger.addHandler(access_handler)
    access_logger.setLevel(logging.INFO)
    access_logger.propagate = False  # Don't propagate to root logger

    # Get main logger
    logger = logging.getLogger(__name__)
    logger.info(f"Logging initialized - Level: {log_level}, Directory: {log_dir}")

    return logger


def get_logger(name: str) -> logging.Logger:
    """Get a logger instance with the specified name"""
    return logging.getLogger(name)


def log_access(user_id: int, username: str, action: str, success: bool = True):
    """Log user access and actions"""
    access_logger = logging.getLogger('access')
    status = "SUCCESS" if success else "FAILED"
    access_logger.info(f"User {user_id} (@{username}) - {action} - {status}")


def log_api_call(endpoint: str, method: str, status_code: int, response_time: float):
    """Log API calls to 3xUI panel"""
    logger = logging.getLogger('api')
    logger.info(f"{method} {endpoint} - {status_code} - {response_time:.3f}s")


class LoggerAdapter(logging.LoggerAdapter):
    """Custom logger adapter for adding context"""

    def process(self, msg, kwargs):
        return f"[{self.extra['context']}] {msg}", kwargs


def get_context_logger(name: str, context: str) -> LoggerAdapter:
    """Get a logger with context information"""
    logger = logging.getLogger(name)
    return LoggerAdapter(logger, {'context': context})
