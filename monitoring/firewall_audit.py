import os

def audit_firewall_rules():
    os.system('sudo iptables -L')
    print("Firewall audit complete")

if __name__ == "__main__":
    audit_firewall_rules()
