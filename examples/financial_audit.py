from sapliyio_fintech import SapliyClient

"""
Real-world Example: Financial Auditing Script

This script performs a cross-zone audit:
1. Lists all zones
2. Checks the balance of the "Treasury" account in each zone
3. Flags any zone with a balance below a threshold
"""

def audit_zones(api_key: str, threshold: float = 10000.0):
    client = SapliyClient(api_key, base_url="http://localhost:8080")
    
    print("--- Starting Financial Audit ---")
    
    try:
        # 1. Fetch all zones
        # Note: In a real app we'd need org_id from the context
        org_id = "org_sapliy_corp"
        zones = client.zones.list_zones(org_id=org_id)
        
        for zone in zones:
            # zone is an instance of ListZones200ResponseInner or similar
            # In Python, Pydantic models use snake_case
            zone_id = getattr(zone, 'id', None)
            zone_name = getattr(zone, 'name', 'Unknown')
            
            print(f"\nAuditing Zone: {zone_name} ({zone_id})")
            
            # 2. Get specific account balance (e.g., 'acc_treasury_usd')
            # For this example, we'll try to get an account named 'acc_treasury_usd'
            treasury_acc_id = f"acc_treasury_{zone_id}"
            
            try:
                acc = client.ledger.get_ledger_account(id=treasury_acc_id, x_zone_id=zone_id)
                balance = float(acc.balance)
                
                print(f"  Balance: {balance} {acc.currency}")
                
                # 3. Validation
                if balance < threshold:
                    print(f"  [ALERT] Low balance in {zone_name}! Threshold: {threshold}")
                    
            except Exception as e:
                print(f"  Available balance check for {treasury_acc_id} skipped or failed: {e}")
                
    except Exception as e:
        print(f"Audit failed: {e}")

if __name__ == "__main__":
    # audit_zones("sk_test_audit_442")
    print("Audit script loaded.")
