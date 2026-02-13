# sapliyio-fintech

[![PyPI version](https://badge.fury.io/py/sapliyio-fintech.svg)](https://badge.fury.io/py/sapliyio-fintech)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Official Python SDK for the Sapliy Fintech Ecosystem. Build financial applications with a clean, Pythonic API.

## Features

- **Payments** — Create charges, handle refunds, manage payment lifecycle
- **Wallets** — User balances and internal accounting
- **Ledger** — Double-entry bookkeeping for high-integrity transactions
- **Billing** — Subscriptions and recurring billing
- **Connect** — Multi-tenant support and managed accounts
- **Webhooks** — Event handling with signature verification
- **Type Hints** — Full typing support for IDE autocomplete

## Installation

```bash
pip install sapliyio-fintech
```

## Quick Start

```python
from sapliyio_fintech import FintechClient

client = FintechClient(api_key="sk_test_...")

# Create a payment
payment = client.payments.create(
    amount=2000,  # $20.00
    currency="USD",
    source_id="src_123",
    description="Order #1234"
)

print(f"Payment created: {payment.id}")
```

## Configuration

```python
# Custom base URL (for self-hosted)
client = FintechClient(
    api_key="sk_test_...",
    base_url="https://api.yourdomain.com"
)

# Custom timeout
client = FintechClient(
    api_key="sk_test_...",
    timeout=30  # seconds
)
```

## API Reference

### Payments

```python
# Create a charge
payment = client.payments.create(
    amount=1000,
    currency="USD",
    source_id="src_123",
    description="Coffee"
)

# Get payment details
payment = client.payments.get("pay_123")

# Refund a payment
payment = client.payments.refund("pay_123", amount=500)  # partial refund
```

### Wallets

```python
# Create a wallet
wallet = client.wallets.create(
    name="User Wallet",
    currency="USD"
)

# Get wallet balance
wallet = client.wallets.get("wal_123")

# Credit (add funds)
wallet = client.wallets.credit(
    wallet_id="wal_123",
    amount=1000,
    description="Deposit"
)

# Debit (withdraw funds)
wallet = client.wallets.debit(
    wallet_id="wal_123",
    amount=500,
    description="Purchase"
)
```

### Ledger

```python
# Record a transaction
response = client.ledger.record_transaction(
    account_id="acc_123",
    amount=1000,
    currency="USD",
    description="Payment received",
    reference_id="ref_456"
)

# Get account details
account = client.ledger.get_account("acc_123")
print(f"Balance: {account.balance}")
```

### Billing

```python
# Create a subscription
subscription = client.billing.create_subscription(
    customer_id="cust_123",
    plan_id="plan_monthly"
)

# Get subscription
subscription = client.billing.get_subscription("sub_123")

# Cancel subscription
client.billing.cancel_subscription("sub_123")
```

### Events (Automation)

```python
# Emit an event to trigger flows
client.events.emit("checkout.completed", {
    "cartId": "cart_123",
    "total": 5000,
    "customerId": "cust_456"
})
```

## Flow Builder Template Variables

When creating flows in the Sapliy Flow Builder, you can use **Handlebars template syntax** to dynamically reference event data in your automation logic. This is particularly useful for approval messages, webhook payloads, and conditional logic.

### Available Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `{{event.type}}` | The event type that triggered the flow | `payment.completed` |
| `{{event.id}}` | Unique event identifier | `evt_abc123` |
| `{{event.payload.*}}` | Access any field from the event payload | `{{event.payload.amount}}` |
| `{{event.createdAt}}` | Timestamp when event was created | `2024-01-15T10:30:00Z` |

### Usage Examples

#### Approval Node Message

```handlebars
Approval required for payment of ${{event.payload.amount}} {{event.payload.currency}}
Customer: {{event.payload.customerId}}
```

When you emit an event like:

```python
client.events.emit("payment.high_value", {
    "amount": 10000,
    "currency": "USD",
    "customerId": "cust_456"
})
```

The approval message will render as:

```
Approval required for payment of $10000 USD
Customer: cust_456
```

#### Webhook Payload Template

```json
{
  "orderId": "{{event.payload.orderId}}",
  "status": "approved",
  "approvedAt": "{{event.createdAt}}",
  "amount": {{event.payload.amount}}
}
```

### Best Practices

1. **Always validate data exists**: Use the Flow Builder's test mode to ensure your template variables resolve correctly
2. **Type safety**: Numeric fields don't need quotes in JSON templates: `{{amount}}` not `"{{amount}}"`
3. **Nested objects**: Access nested data with dot notation: `{{event.payload.customer.email}}`
4. **Debugging**: Use `sapliy listen` to see the actual event payloads and verify your template paths

## Webhook Handling

### Flask Example

```python
from flask import Flask, request
from sapliyio_fintech import FintechClient

app = Flask(__name__)
client = FintechClient(api_key="sk_test_...")

@app.route("/webhooks", methods=["POST"])
def webhook():
    payload = request.data
    signature = request.headers.get("X-Sapliy-Signature")
    secret = "whsec_..."

    try:
        event = client.webhooks.construct_event(payload, signature, secret)
    except ValueError:
        return "Invalid signature", 400

    if event.type == "payment.succeeded":
        payment = event.data.object
        # Handle successful payment
    elif event.type == "payment.failed":
        # Handle failed payment
        pass

    return {"received": True}
```

### Django Example

```python
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from sapliyio_fintech import FintechClient

client = FintechClient(api_key="sk_test_...")

@csrf_exempt
def webhook_view(request):
    payload = request.body
    signature = request.headers.get("X-Sapliy-Signature")
    secret = "whsec_..."

    try:
        event = client.webhooks.construct_event(payload, signature, secret)
    except ValueError:
        return JsonResponse({"error": "Invalid signature"}, status=400)

    # Handle event
    return JsonResponse({"received": True})
```

## Async Support

```python
import asyncio
from sapliyio_fintech import AsyncFintechClient

async def main():
    client = AsyncFintechClient(api_key="sk_test_...")

    payment = await client.payments.create(
        amount=2000,
        currency="USD",
        source_id="src_123",
        description="Async payment"
    )

    print(f"Payment: {payment.id}")

asyncio.run(main())
```

## Error Handling

```python
from sapliyio_fintech.exceptions import FintechError, PaymentError

try:
    payment = client.payments.get("invalid_id")
except PaymentError as e:
    print(f"Payment error: {e.message}")
except FintechError as e:
    print(f"API error ({e.status_code}): {e.message}")
```

## Part of Sapliy Fintech Ecosystem

- [fintech-ecosystem](https://github.com/Sapliy/fintech-ecosystem) — Core backend
- [fintech-sdk-node](https://github.com/Sapliy/fintech-sdk-node) — Node.js SDK
- [fintech-sdk-go](https://github.com/Sapliy/fintech-sdk-go) — Go SDK

## License

MIT © [Sapliy](https://github.com/sapliy)
