import socket

def scan_ip(ip_address):
    try:
        socket.inet_aton(ip_address)
    except socket.error:
        return f"{ip_address} is not a valid IP address"

    try:
        hostname = socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        hostname = ""

    open_ports = []
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            open_ports.append(port)
        sock.close()

    return {"IP Address": ip_address, "Hostname": hostname, "Open Ports": open_ports}
