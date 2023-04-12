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


import socket

def scan_ip(ip, start_port, end_port):
    for port in range(start_port, end_port+1):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            return "IP is alive"
        sock.close()
    return "IP is dead"
