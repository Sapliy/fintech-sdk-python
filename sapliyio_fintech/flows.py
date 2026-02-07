"""
Flows service implementation for Sapliy SDK
"""
from typing import Optional, Dict, List, Any
from sapliyio_fintech.api_client import ApiClient

class Flows:
    def __init__(self, api_client: ApiClient):
        self.api_client = api_client

    def create(self, zone_id: str, name: str, description: str, enabled: bool, nodes: Dict, edges: List) -> Dict:
        """Create a new flow"""
        body = {
            "zone_id": zone_id,
            "name": name,
            "description": description,
            "enabled": enabled,
            "nodes": nodes,
            "edges": edges
        }
        return self.api_client.call_api(
            '/v1/flows', 'POST',
            body=body,
            response_type=object,
            auth_settings=['ApiKeyAuth'],
            _return_http_data_only=True
        )

    def get(self, flow_id: str) -> Dict:
        """Get a flow by ID"""
        return self.api_client.call_api(
            f'/v1/flows/{flow_id}', 'GET',
            response_type=object,
            auth_settings=['ApiKeyAuth'],
            _return_http_data_only=True
        )

    def list(self, zone_id: str) -> Dict:
        """List flows for a zone"""
        return self.api_client.call_api(
            f'/v1/zones/{zone_id}/flows', 'GET',
            response_type=object,
            auth_settings=['ApiKeyAuth'],
            _return_http_data_only=True
        )

    def update(self, flow_id: str, zone_id: str, name: str, description: str, enabled: bool, nodes: Dict, edges: List) -> Dict:
        """Update a flow"""
        body = {
            "zone_id": zone_id,
            "name": name,
            "description": description,
            "enabled": enabled,
            "nodes": nodes,
            "edges": edges
        }
        return self.api_client.call_api(
            f'/v1/flows/{flow_id}', 'PUT',
            body=body,
            response_type=object,
            auth_settings=['ApiKeyAuth'],
            _return_http_data_only=True
        )

    def delete(self, flow_id: str) -> None:
        """Delete (disable) a flow"""
        self.api_client.call_api(
            f'/v1/flows/{flow_id}', 'DELETE',
            auth_settings=['ApiKeyAuth'],
            _return_http_data_only=True
        )

    def enable(self, flow_id: str) -> Dict:
        """Enable a flow"""
        return self.api_client.call_api(
            f'/v1/flows/{flow_id}/enable', 'POST',
            response_type=object,
            auth_settings=['ApiKeyAuth'],
            _return_http_data_only=True
        )

    def disable(self, flow_id: str) -> Dict:
        """Disable a flow"""
        return self.api_client.call_api(
            f'/v1/flows/{flow_id}/disable', 'POST',
            response_type=object,
            auth_settings=['ApiKeyAuth'],
            _return_http_data_only=True
        )
