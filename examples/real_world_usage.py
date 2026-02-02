from sapliyio_fintech import SapliyClient

def run_example():
    client = SapliyClient(api_key="sk_test_123", base_url="http://localhost:8080")

    try:
        print("--- Payments Example ---")
        payment = client.payments.payment_service_create_payment_intent(
            body={
                "amount": "2500",  # $25.00
                "currency": "USD",
                "description": "Example Payment for Python SDK"
            }
        )
        print(f"Created Payment Intent: {payment.id}")

        client.payments.payment_service_confirm_payment_intent(
            id=payment.id,
            body={"paymentMethodId": "pm_card_mastercard"}
        )
        print("Confirmed Payment Intent!")

        print("\n--- Billing Example ---")
        subscription = client.billing.billing_service_create_subscription(
            body={
                "userId": "user_456",
                "orgId": "org_789",
                "planId": "plan_premium"
            }
        )
        print(f"Created Subscription: {subscription.id}, Status: {subscription.status}")

        print("\n--- Wallets Example ---")
        wallet = client.wallets.wallet_service_create_wallet(
            body={"userId": "user_456", "currency": "USD"}
        )
        print(f"Created Wallet: {wallet.id}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_example()
