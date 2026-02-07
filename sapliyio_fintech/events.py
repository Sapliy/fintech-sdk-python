"""
Events implementation for Sapliy SDK
"""
import hashlib
import json
import time
from typing import Optional, Dict, Any, Union

from sapliyio_fintech.api_client import ApiClient

class Events:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def emit(self, event_type: str, data: Dict[str, Any], 
             idempotency_key: Optional[str] = None,
             source: str = "sdk-python",
             env: str = "development") -> Dict[str, Any]:
        """
        Emit an event to the Sapliy Gateway.
        
        :param event_type: Event type string (e.g., "payment.created")
        :param data: Event payload dictionary
        :param idempotency_key: Optional custom idempotency key
        :param source: Event source metadata
        :param env: Environment metadata
        :return: Response dictionary
        """
        
        # Auto-generate idempotency key if not provided
        if not idempotency_key:
            # Simple repeatable hash for payload
            payload_str = json.dumps(data, sort_keys=True)
            payload_hash = hashlib.sha256(payload_str.encode("utf-8")).hexdigest()[:8]
            # Use timestamp to uniqueness if payload is same but different time
            idempotency_key = f"{event_type}-{payload_hash}-{int(time.time() * 1000)}"

        # Construct payload
        body = {
            "type": event_type,
            "data": data,
            "meta": {
                "source": source,
                "env": env
            }
        }

        # Set headers
        header_params = {
            "Idempotency-Key": idempotency_key
        }

        # Use the api_client.call_api method
        # Depending on generated code, call_api signature:
        # call_api(resource_path, method, path_params, query_params, header_params, body, post_params, files, response_type, auth_settings, async_req, _return_http_data_only, collection_formats, _preload_content, _request_timeout)
        
        return self.api_client.call_api(
            '/v1/events/emit', 'POST',
            header_params=header_params,
            body=body,
            response_type=object,
            auth_settings=['ApiKeyAuth'],
            _return_http_data_only=True
        )
