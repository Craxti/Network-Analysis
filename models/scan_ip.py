import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)
        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"Port {port} on {ip} is open")
        sock.close()
    except Exception as e:
        pass

def scan_ip(ip_address, start_port, end_port):
    with ThreadPoolExecutor(max_workers=10) as executor:
        for port in range(start_port, end_port+1):
            executor.submit(scan_port, ip_address, port)
