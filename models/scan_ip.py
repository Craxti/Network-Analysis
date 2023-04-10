import socket
import re


def scan_ip(target, ports=None, subdomains=None):
    """
    Scans an IP address for open ports and enumerates subdomains.
    :param target: The IP address to scan.
    :param ports: A list of ports to scan. If None, will scan the top 1000 ports.
    :param subdomains: A list of subdomains to enumerate. If None, will enumerate common subdomains.
    :return: A dictionary containing the results of the scan.
    """
    result = {
        'target': target,
        'open_ports': [],
        'closed_ports': [],
        'subdomains': {}
    }

    if not ports:
        ports = get_top_ports(1000)

    if not subdomains:
        subdomains = ['www', 'ftp', 'mail', 'webmail', 'smtp', 'imap', 'pop', 'ns1', 'ns2']

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((target, port))
            result['open_ports'].append(port)
        except:
            result['closed_ports'].append(port)
        finally:
            s.close()

    for subdomain_type in subdomains:
        subdomain = subdomain_type + '.' + target
        try:
            ip = socket.gethostbyname(subdomain)
            result['subdomains'][subdomain] = {
                'ip': ip,
                'open_ports': [],
                'closed_ports': []
            }
            for port in ports:
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(1)
                try:
                    s.connect((ip, port))
                    result['subdomains'][subdomain]['open_ports'].append(port)
                except:
                    result['subdomains'][subdomain]['closed_ports'].append(port)
                finally:
                    s.close()
        except:
            pass

    return result

def get_top_ports(num_ports):
    """
    Returns the top num_ports most commonly used ports.
    :param num_ports: The number of ports to return.
    :return: A list of the top num_ports most commonly used ports.
    """
    top_ports = []
    with open('/etc/services', 'r') as f:
        lines = f.readlines()
        for line in lines:
            match = re.search(r'^\w+\s+(\d+)/\w+', line)
            if match:
                top_ports.append(int(match.group(1)))
            if len(top_ports) == num_ports:
                break
    return top_ports