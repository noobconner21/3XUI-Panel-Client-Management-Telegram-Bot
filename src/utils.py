#!/usr/bin/env python3
"""
Utility functions for 3xUI Telegram Bot
Helper functions for data formatting, URI generation, and common operations.
"""

import json
import logging
from datetime import datetime
from urllib.parse import quote
from typing import Dict, Any
import base64

logger = logging.getLogger(__name__)


def format_bytes(bytes_value: int) -> str:
    """Convert bytes to human readable format"""
    if bytes_value == 0:
        return "Unlimited"

    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_value < 1024.0:
            return f"{bytes_value:.2f} {unit}"
        bytes_value /= 1024.0
    return f"{bytes_value:.2f} PB"


def format_timestamp(timestamp: int) -> str:
    """Convert timestamp to readable date format"""
    if timestamp == 0:
        return "Never"
    return datetime.fromtimestamp(timestamp / 1000).strftime('%Y-%m-%d %H:%M')


def generate_connection_uri(inbound_obj: Dict[str, Any], client: Dict[str, Any], hostname: str) -> str:
    """Generate connection URI based on inbound protocol"""
    protocol = inbound_obj.get("protocol", "vless")

    if protocol == "vless":
        return generate_vless_uri(inbound_obj, client, hostname)
    elif protocol == "vmess":
        return generate_vmess_uri(inbound_obj, client, hostname)
    elif protocol == "trojan":
        return generate_trojan_uri(inbound_obj, client, hostname)
    else:
        return generate_vless_uri(inbound_obj, client, hostname)  # Default to VLESS


def generate_vless_uri(inbound_obj: Dict[str, Any], client: Dict[str, Any], hostname: str) -> str:
    """Generate VLESS connection URI with enhanced support"""
    uuid = client.get("id")
    email = client.get("email", "user")
    port = inbound_obj.get("port", 443)
    protocol = "vless"

    try:
        stream_settings = json.loads(inbound_obj.get("streamSettings", "{}"))
    except:
        stream_settings = {}

    network = stream_settings.get("network", "tcp")
    security = stream_settings.get("security", "none")

    # Build query parameters
    params = [f"type={network}", f"security={security}"]

    if network == "ws":
        ws_settings = stream_settings.get("wsSettings", {})
        path = ws_settings.get("path", "/")
        params.append(f"path={quote(path)}")

        host_header = ws_settings.get("headers", {}).get("Host", hostname)
        params.append(f"host={host_header}")

    elif network == "grpc":
        grpc_settings = stream_settings.get("grpcSettings", {})
        service_name = grpc_settings.get("serviceName", "")
        if service_name:
            params.append(f"serviceName={quote(service_name)}")

    # TLS settings
    if security == "tls":
        tls_settings = stream_settings.get("tlsSettings", {})
        sni = tls_settings.get("serverName", hostname)
        params.append(f"sni={sni}")

        alpn = tls_settings.get("alpn", [])
        if alpn:
            params.append(f"alpn={','.join(alpn)}")

    query = "&".join(params)
    return f"{protocol}://{uuid}@{hostname}:{port}?{query}#{quote(email)}"


def generate_vmess_uri(inbound_obj: Dict[str, Any], client: Dict[str, Any], hostname: str) -> str:
    """Generate VMess connection URI"""
    config = {
        "v": "2",
        "ps": client.get("email", "user"),
        "add": hostname,
        "port": str(inbound_obj.get("port", 443)),
        "id": client.get("id"),
        "aid": str(client.get("alterId", 0)),
        "scy": "auto",
        "net": "tcp",
        "type": "none",
        "host": "",
        "path": "",
        "tls": "",
        "sni": "",
        "alpn": ""
    }

    try:
        stream_settings = json.loads(inbound_obj.get("streamSettings", "{}"))
        config["net"] = stream_settings.get("network", "tcp")
        config["tls"] = stream_settings.get("security", "none")

        if config["net"] == "ws":
            ws_settings = stream_settings.get("wsSettings", {})
            config["path"] = ws_settings.get("path", "/")
            config["host"] = ws_settings.get("headers", {}).get("Host", "")

    except:
        pass

    config_json = json.dumps(config, separators=(',', ':'))
    encoded = base64.b64encode(config_json.encode()).decode()
    return f"vmess://{encoded}"


def generate_trojan_uri(inbound_obj: Dict[str, Any], client: Dict[str, Any], hostname: str) -> str:
    """Generate Trojan connection URI"""
    password = client.get("password", client.get("id"))
    port = inbound_obj.get("port", 443)
    email = client.get("email", "user")

    params = ["type=tcp"]

    try:
        stream_settings = json.loads(inbound_obj.get("streamSettings", "{}"))
        network = stream_settings.get("network", "tcp")
        params[0] = f"type={network}"

        if stream_settings.get("security") == "tls":
            tls_settings = stream_settings.get("tlsSettings", {})
            sni = tls_settings.get("serverName", hostname)
            params.append(f"sni={sni}")

    except:
        pass

    query = "&".join(params)
    return f"trojan://{password}@{hostname}:{port}?{query}#{quote(email)}"


def validate_email(email: str) -> bool:
    """Basic email validation"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def sanitize_filename(filename: str) -> str:
    """Sanitize filename for safe file operations"""
    import re
    # Remove invalid characters
    filename = re.sub(r'[^\w\s.-]', '_', filename)
    # Replace multiple spaces with single underscore
    filename = re.sub(r'\s+', '_', filename)
    return filename.strip('._')


def generate_random_string(length: int = 8) -> str:
    """Generate random string for temporary uses"""
    import secrets
    import string
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))


def is_valid_uuid(uuid_string: str) -> bool:
    """Validate UUID format"""
    import re
    uuid_pattern = re.compile(
        r'^[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$',
        re.IGNORECASE
    )
    return bool(uuid_pattern.match(uuid_string))


def parse_data_limit(limit_str: str) -> int:
    """Parse data limit string to bytes"""
    try:
        limit_str = limit_str.strip().lower()

        # Handle different units
        multipliers = {
            'b': 1,
            'kb': 1024,
            'mb': 1024**2,
            'gb': 1024**3,
            'tb': 1024**4
        }

        # Extract number and unit
        import re
        match = re.match(r'^(\d+(?:\.\d+)?)\s*([kmgt]?b)?$', limit_str)
        if not match:
            # Try just number (assume GB)
            number = float(limit_str)
            return int(number * 1024**3) if number > 0 else 0

        number, unit = match.groups()
        number = float(number)
        unit = unit or 'gb'  # Default to GB

        return int(number * multipliers.get(unit, 1024**3))

    except (ValueError, AttributeError):
        return 0


def format_duration(seconds: int) -> str:
    """Format duration in seconds to human readable format"""
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        return f"{seconds // 60}m {seconds % 60}s"
    elif seconds < 86400:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        return f"{hours}h {minutes}m"
    else:
        days = seconds // 86400
        hours = (seconds % 86400) // 3600
        return f"{days}d {hours}h"


def truncate_text(text: str, max_length: int = 100, suffix: str = "...") -> str:
    """Truncate text to specified length"""
    if len(text) <= max_length:
        return text
    return text[:max_length - len(suffix)] + suffix


def mask_sensitive_data(data: str, show_chars: int = 4) -> str:
    """Mask sensitive data showing only first/last characters"""
    if len(data) <= show_chars * 2:
        return "*" * len(data)

    return data[:show_chars] + "*" * (len(data) - show_chars * 2) + data[-show_chars:]
