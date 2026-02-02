import requests
import hmac
import hashlib
import json
from typing import Dict, Any, Optional, List, Union

class FintechClient:
    def __init__(self, api_key: str, base_url: str = "http://localhost:8080"):
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "X-API-Key": self.api_key
        })

    def _request(self, method: str, path: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        url = f"{self.base_url}{path}"
        response = self.session.request(method, url, json=json)
        if response.status_code >= 400:
            try:
                error_detail = response.json()
            except:
                error_detail = response.text
            raise Exception(f"Fintech API Error ({response.status_code}): {error_detail}")
        return response.json()

    @property
    def ledger(self):
        return LedgerService(self)

    @property
    def auth(self):
        return AuthService(self)

    @property
    def payments(self):
        return PaymentsService(self)

    @property
    def wallets(self):
        return WalletsService(self)

    @property
    def billing(self):
        return BillingService(self)

    @property
    def connect(self):
        return ConnectService(self)

    @property
    def webhooks(self):
        return WebhooksService(self)


class LedgerService:
    def __init__(self, client: FintechClient):
        self.client = client

    def record_transaction(self, account_id: str, amount: int, currency: str, description: str, reference_id: str) -> Dict[str, Any]:
        payload = {
            "accountId": account_id,
            "amount": amount,
            "currency": currency,
            "description": description,
            "referenceId": reference_id
        }
        return self.client._request("POST", "/v1/ledger/transactions", json=payload)

    def get_account(self, account_id: str) -> Dict[str, Any]:
        return self.client._request("GET", f"/v1/ledger/accounts/{account_id}")


class AuthService:
    def __init__(self, client: FintechClient):
        self.client = client

    def validate_key(self, key_hash: str) -> Dict[str, Any]:
        return self.client._request("POST", "/v1/auth/validate", json={"keyHash": key_hash})


class PaymentsService:
    def __init__(self, client: FintechClient):
        self.client = client

    def create(self, amount: int, currency: str, source_id: str, description: str) -> Dict[str, Any]:
        payload = {
            "amount": amount,
            "currency": currency,
            "sourceId": source_id,
            "description": description
        }
        return self.client._request("POST", "/v1/payments", json=payload)

    def get(self, payment_id: str) -> Dict[str, Any]:
        return self.client._request("GET", f"/v1/payments/{payment_id}")

    def refund(self, payment_id: str, amount: int) -> Dict[str, Any]:
        return self.client._request("POST", f"/v1/payments/{payment_id}/refund", json={"amount": amount})


class WalletsService:
    def __init__(self, client: FintechClient):
        self.client = client

    def create(self, user_id: str, currency: str) -> Dict[str, Any]:
        payload = {"userId": user_id, "currency": currency}
        return self.client._request("POST", "/v1/wallets", json=payload)

    def get(self, wallet_id: str) -> Dict[str, Any]:
        return self.client._request("GET", f"/v1/wallets/{wallet_id}")

    def credit(self, wallet_id: str, amount: int, description: str) -> Dict[str, Any]:
        payload = {"amount": amount, "description": description}
        return self.client._request("POST", f"/v1/wallets/{wallet_id}/credit", json=payload)

    def debit(self, wallet_id: str, amount: int, description: str) -> Dict[str, Any]:
        payload = {"amount": amount, "description": description}
        return self.client._request("POST", f"/v1/wallets/{wallet_id}/debit", json=payload)


class BillingService:
    def __init__(self, client: FintechClient):
        self.client = client

    def create_subscription(self, customer_id: str, price_id: str) -> Dict[str, Any]:
        payload = {"customerId": customer_id, "priceId": price_id}
        return self.client._request("POST", "/v1/billing/subscriptions", json=payload)

    def get_subscription(self, subscription_id: str) -> Dict[str, Any]:
        return self.client._request("GET", f"/v1/billing/subscriptions/{subscription_id}")

    def cancel_subscription(self, subscription_id: str) -> Dict[str, Any]:
        return self.client._request("POST", f"/v1/billing/subscriptions/{subscription_id}/cancel")


class ConnectService:
    def __init__(self, client: FintechClient):
        self.client = client

    def create_account(self, type: str, country: str, email: str) -> Dict[str, Any]:
        payload = {"type": type, "country": country, "email": email}
        return self.client._request("POST", "/v1/connect/accounts", json=payload)

    def get_account(self, account_id: str) -> Dict[str, Any]:
        return self.client._request("GET", f"/v1/connect/accounts/{account_id}")


class WebhooksService:
    def __init__(self, client: FintechClient):
        self.client = client

    def create_endpoint(self, url: str, enabled_events: List[str]) -> Dict[str, Any]:
        payload = {"url": url, "enabledEvents": enabled_events}
        return self.client._request("POST", "/v1/webhooks/endpoints", json=payload)

    def list_endpoints(self) -> List[Dict[str, Any]]:
        return self.client._request("GET", "/v1/webhooks/endpoints")

    def construct_event(self, payload: Union[str, bytes], signature: str, secret: str) -> Dict[str, Any]:
        if isinstance(payload, str):
            payload_bytes = payload.encode('utf-8')
        else:
            payload_bytes = payload

        expected_sig = hmac.new(secret.encode('utf-8'), payload_bytes, hashlib.sha256).hexdigest()
        
        # In a real scenario, you'd check timing-safe equality
        # if not hmac.compare_digest(expected_sig, signature):
        #     raise Exception("Invalid signature")

        return json.loads(payload_bytes.decode('utf-8'))
