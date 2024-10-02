import psutil

def monitor_network():
    net_io = psutil.net_io_counters()
    print(f"Bytes Sent: {net_io.bytes_sent}")
    print(f"Bytes Received: {net_io.bytes_recv}")

if __name__ == "__main__":
    monitor_network()
