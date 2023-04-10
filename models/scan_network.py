import socket
import ipaddress
from concurrent.futures import ThreadPoolExecutor

def scan_network(ip_range, protocol="icmp", timeout=1):
    if protocol == "icmp":
        # ICMP echo request
        protocol_number = socket.IPPROTO_ICMP
        request = b"\x08\x00\x7d\x4b\x00\x00\x00\x00" # echo request packet
    elif protocol == "tcp":
        # TCP SYN packet
        protocol_number = socket.IPPROTO_TCP
        request = b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x04\x05\xb4\x04\x02\x08\x0a\x00\xde\x11\x5d\x00\x00\x00\x00\x04\x02\x00\x00"
    elif protocol == "udp":
        # UDP packet
        protocol_number = socket.IPPROTO_UDP
        request = b"\x00\x00\x00\x00" # empty UDP packet
    else:
        raise ValueError("Invalid protocol")

    active_hosts = []

    def scan(ip):
        sock = socket.socket(socket.AF_INET, socket.SOCK_RAW, protocol_number)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.settimeout(timeout)
        try:
            sock.bind((str(ip), 0))
            sock.sendto(request, (str(ip), 0))
            response, _ = sock.recvfrom(1024)
            active_hosts.append(ip)
        except socket.timeout:
            pass
        finally:
            sock.close()

    with ThreadPoolExecutor() as executor:
        for ip in ipaddress.IPv4Network(ip_range):
            executor.submit(scan, ip)

    return active_hosts
