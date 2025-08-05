#!/usr/bin/env python3
"""
3xUI API Client
Enhanced API client for interacting with 3xUI panel with connection pooling,
session management, and comprehensive error handling.
"""

import json
import logging
import requests
import urllib3
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Any
from urllib.parse import urljoin

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

logger = logging.getLogger(__name__)


class XUIAPIError(Exception):
    """Custom exception for 3xUI API errors"""
    pass


class XUIClient:
    """Enhanced 3xUI API client with session management and error handling"""

    def __init__(self, host: str, username: str, password: str, timeout: int = 30):
        """
        Initialize XUI client

        Args:
            host: 3xUI panel URL
            username: Panel username
            password: Panel password
            timeout: Request timeout in seconds
        """
        self.host = host.rstrip('/')
        self.username = username
        self.password = password
        self.timeout = timeout

        # Session management
        self.session = requests.Session()
        self.session.verify = False
        self.session.timeout = timeout

        # Login state tracking
        self._login_time = None
        self._login_duration = timedelta(hours=1)  # Re-login after 1 hour
        self._session_cookies = None

        logger.info(f"XUI Client initialized for {self.host}")

    def _is_login_valid(self) -> bool:
        """Check if current login session is still valid"""
        if not self._login_time or not self._session_cookies:
            return False
        return datetime.now() - self._login_time < self._login_duration

    def _make_request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        """Make HTTP request with error handling and logging"""
        url = urljoin(self.host, endpoint)
        start_time = datetime.now()

        try:
            response = self.session.request(method, url, **kwargs)
            response_time = (datetime.now() - start_time).total_seconds()

            logger.debug(f"{method} {endpoint} - {response.status_code} - {response_time:.3f}s")

            return response

        except requests.exceptions.Timeout:
            logger.error(f"Request timeout for {method} {endpoint}")
            raise XUIAPIError("Request timed out")
        except requests.exceptions.ConnectionError:
            logger.error(f"Connection error for {method} {endpoint}")
            raise XUIAPIError("Connection failed")
        except Exception as e:
            logger.error(f"Unexpected error for {method} {endpoint}: {e}")
            raise XUIAPIError(f"Request failed: {str(e)}")

    def login(self) -> bool:
        """Login to 3xUI panel with enhanced error handling"""
        try:
            if self._is_login_valid():
                return True

            logger.info("Attempting login to 3xUI panel")

            response = self._make_request(
                'POST',
                '/login',
                data={'username': self.username, 'password': self.password}
            )

            if response.status_code == 200:
                try:
                    result = response.json()
                    if result.get("success"):
                        self._login_time = datetime.now()
                        self._session_cookies = response.cookies
                        logger.info("Successfully logged into 3xUI panel")
                        return True
                    else:
                        error_msg = result.get('msg', 'Unknown login error')
                        logger.error(f"Login failed: {error_msg}")
                        raise XUIAPIError(f"Login failed: {error_msg}")
                except json.JSONDecodeError:
                    logger.error("Invalid JSON response from login endpoint")
                    raise XUIAPIError("Invalid response format")
            else:
                logger.error(f"Login request failed with status {response.status_code}")
                raise XUIAPIError(f"Login request failed: HTTP {response.status_code}")

        except XUIAPIError:
            raise
        except Exception as e:
            logger.error(f"Unexpected login error: {e}")
            raise XUIAPIError(f"Login error: {str(e)}")

    def get_inbounds(self) -> List[Dict[str, Any]]:
        """Get list of all inbounds"""
        if not self.login():
            raise XUIAPIError("Authentication failed")

        try:
            response = self._make_request('GET', '/panel/api/inbounds/list')

            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    inbounds = data.get("obj", [])
                    logger.info(f"Retrieved {len(inbounds)} inbounds")
                    return inbounds
                else:
                    error_msg = data.get('msg', 'Failed to get inbounds')
                    raise XUIAPIError(error_msg)
            else:
                raise XUIAPIError(f"HTTP {response.status_code}: {response.text}")

        except XUIAPIError:
            raise
        except Exception as e:
            logger.error(f"Error fetching inbounds: {e}")
            raise XUIAPIError(f"Failed to get inbounds: {str(e)}")

    def get_inbound(self, inbound_id: int) -> Optional[Dict[str, Any]]:
        """Get specific inbound by ID"""
        if not self.login():
            raise XUIAPIError("Authentication failed")

        try:
            response = self._make_request('GET', f'/panel/api/inbounds/get/{inbound_id}')

            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    inbound = data.get("obj")
                    logger.info(f"Retrieved inbound {inbound_id}")
                    return inbound
                else:
                    error_msg = data.get('msg', f'Inbound {inbound_id} not found')
                    raise XUIAPIError(error_msg)
            else:
                raise XUIAPIError(f"HTTP {response.status_code}: {response.text}")

        except XUIAPIError:
            raise
        except Exception as e:
            logger.error(f"Error fetching inbound {inbound_id}: {e}")
            raise XUIAPIError(f"Failed to get inbound: {str(e)}")

    def add_client(self, inbound_id: int, client_config: Dict[str, Any]) -> Tuple[bool, str]:
        """Add client to inbound"""
        if not self.login():
            return False, "Authentication failed"

        try:
            payload = {
                "id": inbound_id,
                "settings": json.dumps({"clients": [client_config]})
            }

            response = self._make_request(
                'POST',
                '/panel/api/inbounds/addClient',
                json=payload
            )

            if response.status_code == 200:
                result = response.json()
                if result.get("success"):
                    logger.info(f"Successfully added client {client_config.get('email')} to inbound {inbound_id}")
                    return True, "Client added successfully"
                else:
                    error_msg = result.get("msg", "Unknown error")
                    logger.error(f"Failed to add client: {error_msg}")
                    return False, error_msg
            else:
                error_msg = f"HTTP {response.status_code}: {response.text}"
                logger.error(f"Add client request failed: {error_msg}")
                return False, error_msg

        except Exception as e:
            logger.error(f"Error adding client: {e}")
            return False, str(e)

    def remove_client(self, inbound_id: int, client_uuid: str) -> Tuple[bool, str]:
        """Remove client from inbound"""
        if not self.login():
            return False, "Authentication failed"

        try:
            payload = {
                "id": inbound_id,
                "uuid": client_uuid
            }

            response = self._make_request(
                'POST',
                f'/panel/api/inbounds/delClient/{client_uuid}',
                json=payload
            )

            if response.status_code == 200:
                result = response.json()
                if result.get("success"):
                    logger.info(f"Successfully removed client {client_uuid} from inbound {inbound_id}")
                    return True, "Client removed successfully"
                else:
                    error_msg = result.get("msg", "Unknown error")
                    logger.error(f"Failed to remove client: {error_msg}")
                    return False, error_msg
            else:
                error_msg = f"HTTP {response.status_code}: {response.text}"
                logger.error(f"Remove client request failed: {error_msg}")
                return False, error_msg

        except Exception as e:
            logger.error(f"Error removing client: {e}")
            return False, str(e)

    def get_client_traffic(self, inbound_id: int, client_email: str) -> Optional[Dict[str, Any]]:
        """Get client traffic statistics"""
        if not self.login():
            raise XUIAPIError("Authentication failed")

        try:
            inbound = self.get_inbound(inbound_id)
            if not inbound:
                return None

            # Parse client settings
            settings = json.loads(inbound.get("settings", "{}"))
            clients = settings.get("clients", [])

            for client in clients:
                if client.get("email") == client_email:
                    return {
                        "email": client.get("email"),
                        "totalGB": client.get("totalGB", 0),
                        "expiryTime": client.get("expiryTime", 0),
                        "enable": client.get("enable", True),
                        "up": client.get("up", 0),
                        "down": client.get("down", 0),
                        "total": client.get("total", 0)
                    }

            return None

        except Exception as e:
            logger.error(f"Error getting client traffic: {e}")
            return None

    def reset_client_traffic(self, inbound_id: int, client_email: str) -> Tuple[bool, str]:
        """Reset client traffic statistics"""
        if not self.login():
            return False, "Authentication failed"

        try:
            payload = {
                "id": inbound_id,
                "email": client_email
            }

            response = self._make_request(
                'POST',
                '/panel/api/inbounds/resetClientTraffic',
                json=payload
            )

            if response.status_code == 200:
                result = response.json()
                if result.get("success"):
                    logger.info(f"Successfully reset traffic for client {client_email}")
                    return True, "Traffic reset successfully"
                else:
                    error_msg = result.get("msg", "Unknown error")
                    return False, error_msg
            else:
                return False, f"HTTP {response.status_code}: {response.text}"

        except Exception as e:
            logger.error(f"Error resetting client traffic: {e}")
            return False, str(e)

    def get_system_stats(self) -> Optional[Dict[str, Any]]:
        """Get system statistics"""
        if not self.login():
            raise XUIAPIError("Authentication failed")

        try:
            response = self._make_request('POST', '/panel/api/inbounds/getSystemStats')

            if response.status_code == 200:
                data = response.json()
                if data.get("success"):
                    return data.get("obj", {})

            return None

        except Exception as e:
            logger.error(f"Error getting system stats: {e}")
            return None

    def close(self):
        """Close the session"""
        if self.session:
            self.session.close()
            logger.info("XUI Client session closed")
