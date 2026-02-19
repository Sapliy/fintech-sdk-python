from sapliyio_fintech import SapliyClient, CreatePaymentIntentRequest, ConfirmPaymentIntentRequest, EmitEventRequest

def run_example():
    client = SapliyClient(api_key="sk_test_123", base_url="http://localhost:8080")
    zone_id = "zone_main_123"

    try:
        print("--- Payments Example ---")
        # Python SDK uses snake_case method names
        payment = client.payments.create_payment_intent(
            x_zone_id=zone_id,
            create_payment_intent_request=CreatePaymentIntentRequest(
                amount=2500,  # $25.00
                currency="USD",
                description="Example Payment for Python SDK"
            )
        )
        print(f"Created Payment Intent: {payment.id}, Status: {payment.status}")

        client.payments.confirm_payment_intent(
            id=payment.id,
            x_zone_id=zone_id,
            confirm_payment_intent_request=ConfirmPaymentIntentRequest(
                payment_method_id="pm_card_mastercard"
            )
        )
        print("Confirmed Payment Intent!")

        print("\n--- Wallets Example ---")
        wallet = client.wallets.get_wallet(user_id="user_456", x_zone_id=zone_id)
        print(f"Wallet Balance: {wallet.balance} {wallet.currency}")

        print("\n--- Events Example ---")
        event = client.emit_event(EmitEventRequest(
            type="user.login",
            data={"user_id": "user_456", "ip": "1.1.1.1"}
        ))
        print(f"Emitted Event ID: {event.event_id}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    run_example()
