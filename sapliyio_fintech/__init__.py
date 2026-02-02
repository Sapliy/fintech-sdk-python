from .generated.sapliyio_fintech.api_client import ApiClient
from .generated.sapliyio_fintech.configuration import Configuration
from .generated.sapliyio_fintech.api.auth_service_api import AuthServiceApi
from .generated.sapliyio_fintech.api.billing_service_api import BillingServiceApi
from .generated.sapliyio_fintech.api.ledger_service_api import LedgerServiceApi
from .generated.sapliyio_fintech.api.notification_service_api import NotificationServiceApi
from .generated.sapliyio_fintech.api.payment_service_api import PaymentServiceApi
from .generated.sapliyio_fintech.api.wallet_service_api import WalletServiceApi

class SapliyClient:
    def __init__(self, api_key: str, base_url: str = "http://localhost:8080"):
        self.configuration = Configuration(
            host=base_url,
        )
        self.configuration.api_key['Authorization'] = f"Bearer {api_key}"
        
        self.api_client = ApiClient(self.configuration)
        
        self.auth = AuthServiceApi(self.api_client)
        self.billing = BillingServiceApi(self.api_client)
        self.ledger = LedgerServiceApi(self.api_client)
        self.notifications = NotificationServiceApi(self.api_client)
        self.payments = PaymentServiceApi(self.api_client)
        self.wallets = WalletServiceApi(self.api_client)
