from .api_client import ApiClient
from .configuration import Configuration
from .api.auth_service_api import AuthServiceApi
from .api.billing_service_api import BillingServiceApi
from .api.ledger_service_api import LedgerServiceApi
from .api.notification_service_api import NotificationServiceApi
from .api.payment_service_api import PaymentServiceApi
from .api.wallet_service_api import WalletServiceApi
from .events import Events
from .flows import Flows
# from .api.zone_service_api import ZoneServiceApi

class SapliyClient:
    def __init__(self, api_key: str, base_url: str = "http://localhost:8080"):
        self.configuration = Configuration(
            host=base_url,
        )
        self.configuration.api_key['X-API-Key'] = api_key
        
        self.api_client = ApiClient(self.configuration)
        
        self.auth = AuthServiceApi(self.api_client)
        self.billing = BillingServiceApi(self.api_client)
        self.ledger = LedgerServiceApi(self.api_client)
        self.notifications = NotificationServiceApi(self.api_client)
        self.payments = PaymentServiceApi(self.api_client)
        self.wallets = WalletServiceApi(self.api_client)
        # self.flows = FlowServiceApi(self.api_client)
        # self.zones = ZoneServiceApi(self.api_client)
        self.flows = Flows(self.api_client)
        self.events = Events(self.api_client)
