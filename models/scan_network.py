import subprocess
import ipaddress


def scan_ip_with_timeout(ip_address, timeout=2):
    try:
        subprocess.run(['ping', '-c', '1', '-w', str(timeout), ip_address], check=True, stdout=subprocess.DEVNULL)
        return (ip_address, True)
    except subprocess.CalledProcessError:
        return (ip_address, False)


def scan_network(cidr_address, timeout=2):
    try:
        network = ipaddress.IPv4Network(cidr_address)
    except ValueError:
        return f"{cidr_address} is not a valid CIDR network address"

    addresses = [str(ip_address) for ip_address in network.hosts()]

    results = []
    for address in addresses:
        results.append(scan_ip_with_timeout(address, timeout))

    return results
