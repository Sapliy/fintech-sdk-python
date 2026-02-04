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
        zones_resp = client.zones.zone_service_list_zones(org_id=org_id)
        
        for zone in zones_resp.zones:
            print(f"\nAuditing Zone: {zone.name} ({zone.id})")
            
            # 2. Get specific account balance (e.g., 'acc_treasury_usd')
            # For simplicity, we assume account IDs follow a pattern or are stored in metadata
            treasury_acc_id = zone.metadata.get("treasury_account_id") if zone.metadata else None
            
            if not treasury_acc_id:
                print(f"Skipping {zone.name}: No treasury_account_id in metadata")
                continue
                
            try:
                acc = client.ledger.ledger_service_get_account(id=treasury_acc_id)
                balance = float(acc.balance)
                
                print(f"  Balance: {balance} {acc.currency}")
                
                # 3. Validation
                if balance < threshold:
                    print(f"  [ALERT] Low balance in {zone.name}! Threshold: {threshold}")
                    
            except Exception as e:
                print(f"  Error fetching account {treasury_acc_id}: {e}")
                
    except Exception as e:
        print(f"Audit failed: {e}")

if __name__ == "__main__":
    # audit_zones("sk_test_audit_442")
    pass
