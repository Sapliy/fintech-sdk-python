# Sapliyio Fintech Python SDK

Official Python SDK for the Sapliy Fintech Ecosystem.

## Installation

```bash
pip install sapliyio-fintech
```

## Usage

```python
from sapliyio_fintech import FintechClient

# Initialize the client
client = FintechClient(api_key="your_api_key")

# Example: Record a transaction
response = client.ledger.record_transaction(
    account_id="acc_123",
    amount=1000,
    currency="USD",
    description="Coffee",
    reference_id="ref_456"
)

print(response)
```
