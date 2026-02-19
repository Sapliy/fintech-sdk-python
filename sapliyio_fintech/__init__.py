# coding: utf-8

"""
    Sapliy Fintech API

    Official API for the Sapliy Fintech Ecosystem. Build robust financial applications with our type-safe, high-integrity platform.

    The version of the OpenAPI document: 1.0.0
    Contact: support@sapliy.io
"""

__version__ = "1.0.0"

# Import all APIs
from sapliyio_fintech.api.auth_api import AuthApi
from sapliyio_fintech.api.billing_api import BillingApi
from sapliyio_fintech.api.events_api import EventsApi
from sapliyio_fintech.api.executions_api import ExecutionsApi
from sapliyio_fintech.api.flows_api import FlowsApi
from sapliyio_fintech.api.ledger_api import LedgerApi
from sapliyio_fintech.api.payments_api import PaymentsApi
from sapliyio_fintech.api.wallets_api import WalletsApi
from sapliyio_fintech.api.zones_api import ZonesApi

# Import core client classes
from sapliyio_fintech.api_client import ApiClient
from sapliyio_fintech.configuration import Configuration
from sapliyio_fintech.exceptions import OpenApiException, ApiException

# Import models
from sapliyio_fintech.models.automation_flow import AutomationFlow
from sapliyio_fintech.models.automation_flow_edge import AutomationFlowEdge
from sapliyio_fintech.models.automation_flow_execution import AutomationFlowExecution
from sapliyio_fintech.models.automation_flow_execution_step import AutomationFlowExecutionStep
from sapliyio_fintech.models.automation_flow_node import AutomationFlowNode
from sapliyio_fintech.models.automation_flow_trigger import AutomationFlowTrigger
from sapliyio_fintech.models.billing_subscription import BillingSubscription
from sapliyio_fintech.models.confirm_payment_intent_request import ConfirmPaymentIntentRequest
from sapliyio_fintech.models.create_payment_intent_request import CreatePaymentIntentRequest
from sapliyio_fintech.models.create_subscription_request import CreateSubscriptionRequest
from sapliyio_fintech.models.create_zone_request import CreateZoneRequest
from sapliyio_fintech.models.emit_event202_response import EmitEvent202Response
from sapliyio_fintech.models.emit_event_request import EmitEventRequest
from sapliyio_fintech.models.error_envelope import ErrorEnvelope
from sapliyio_fintech.models.get_past_events200_response import GetPastEvents200Response
from sapliyio_fintech.models.ledger_account import LedgerAccount
from sapliyio_fintech.models.ledger_entry import LedgerEntry
from sapliyio_fintech.models.ledger_transaction import LedgerTransaction
from sapliyio_fintech.models.payment_intent import PaymentIntent
from sapliyio_fintech.models.register_user_request import RegisterUserRequest
from sapliyio_fintech.models.topup_wallet_request import TopupWalletRequest
from sapliyio_fintech.models.transfer_wallet_request import TransferWalletRequest
from sapliyio_fintech.models.user import User
from sapliyio_fintech.models.v1_ledger_accounts_post_request import V1LedgerAccountsPostRequest
from sapliyio_fintech.models.v1_ledger_transactions_post_request import V1LedgerTransactionsPostRequest
from sapliyio_fintech.models.wallet import Wallet

class SapliyClient:
    """
    Unified client for the Sapliy Fintech API.
    """
    def __init__(self, api_key: str, base_url: str = "https://api.sapliy.io"):
        self.configuration = Configuration(host=base_url)
        self.configuration.access_token = api_key
        
        self.api_client = ApiClient(self.configuration)
        
        self.auth = AuthApi(self.api_client)
        self.billing = BillingApi(self.api_client)
        self.events = EventsApi(self.api_client)
        self.executions = ExecutionsApi(self.api_client)
        self.flows = FlowsApi(self.api_client)
        self.ledger = LedgerApi(self.api_client)
        self.payments = PaymentsApi(self.api_client)
        self.wallets = WalletsApi(self.api_client)
        self.zones = ZonesApi(self.api_client)

    def emit_event(self, request: EmitEventRequest):
        return self.events.emit_event(request)

    def record_transaction(self, zone_id: str, request: V1LedgerTransactionsPostRequest):
        return self.ledger.v1_ledger_transactions_post(zone_id, request)
