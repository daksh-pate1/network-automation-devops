import os

def network_scan(ip_range):
    response = os.system(f"ping -c 1 {ip_range}")
    if response == 0:
        print(f"{ip_range} is reachable")
    else:
        print(f"{ip_range} is not reachable")

if __name__ == "__main__":
    ip_range = input("Enter the IP range to scan (e.g., 192.168.1.0): ")
    network_scan(ip_range)
