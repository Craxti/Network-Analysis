import socket


def scan_domain(domain, ports=None):
    """
    Scans a domain for open ports.
    :param domain: The domain to scan.
    :param ports: A list of ports to scan. If None, will scan the top 1000 ports.
    :return: A dictionary containing the results of the scan.
    """
    result = {
        'domain': domain,
        'open_ports': [],
        'closed_ports': []
    }

    if not ports:
        ports = get_top_ports(1000)

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        try:
            s.connect((domain, port))
            result['open_ports'].append(port)
        except BaseException:
            result['closed_ports'].append(port)
        finally:
            s.close()

    return result


def enum_subdomains(domain, types=None, ports=None):
    """
    Enumerates subdomains of a domain.
    :param domain: The domain to enumerate subdomains for.
    :param types: A list of domain types to enumerate (e.g. ['www', 'ftp']). If None, will enumerate all common
    subdomain types.
    :param ports: A list of ports to scan. If None, will scan the top 1000 ports.
    :return: A dictionary containing the results of the subdomain enumeration and port scanning.
    """
    result = {
        'domain': domain,
        'subdomains': {}
    }

    if not types:
        types = [
            'www',
            'ftp',
            'mail',
            'webmail',
            'smtp',
            'imap',
            'pop',
            'ns1',
            'ns2']

    for subdomain_type in types:
        subdomain = subdomain_type + '.' + domain
        try:
            ip = socket.gethostbyname(subdomain)
            result['subdomains'][subdomain] = {
                'ip': ip
            }
            if ports:
                result['subdomains'][subdomain]['scan'] = scan_domain(
                    ip, ports=ports)
        except BaseException:
            pass

    return result


def get_top_ports(num_ports):
    """
    Returns the top num_ports most commonly used ports.
    :param num_ports: The number of ports to return.
    :return: A list of the top num_ports most commonly used ports.
    """
    top_ports = []
    try:
        with open('/etc/services', 'r') as f:
            lines = f.readlines()
            for line in lines:
                parts = line.split()
                if len(parts) > 1 and parts[1].isdigit():
                    top_ports.append(int(parts[1]))
                    if len(top_ports) >= num_ports:
                        break
    except FileNotFoundError:
        pass
    return top_ports
