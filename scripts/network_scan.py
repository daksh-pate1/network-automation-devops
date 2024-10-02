import os
import platform
def network_scan(ip_range):
    # Determine the flag based on the OS
    param = "-n" if platform.system().lower() == "windows" else "-c"
    
    for i in range(1, 255):
        ip = f"{ip_range}.{i}"
        response = os.system(f"ping {param} 1 {ip}")
        if response == 0:
            print(f"{ip} is reachable")
        else:
            print(f"{ip} is not reachable")

if __name__ == "__main__":
    ip_range = input("Enter the IP range to scan (e.g., 192.168.1): ")
    network_scan(ip_range)