import subprocess
import ipaddress
import json
import nmap


def scan_ip_with_timeout(ip_address, timeout=2):
    try:
        subprocess.run(['ping', '-c', '1', '-w', str(timeout),
                       ip_address], check=True, stdout=subprocess.DEVNULL)
        return ip_address, True
    except subprocess.CalledProcessError:
        return ip_address, False


def scan_network(ip_range, output_format=None):
    nm = nmap.PortScanner()
    nm.scan(ip_range)

    hosts = []
    for host in nm.all_hosts():
        host_data = {
            "ip": host,
            "hostname": nm[host].hostname() if "hostname" in nm[host] else "",
            "state": nm[host].state(),
            "ports": []
        }

        if "tcp" in nm[host]:
            for port in nm[host]["tcp"]:
                port_data = {
                    "port": port,
                    "name": nm[host]["tcp"][port]["name"],
                    "state": nm[host]["tcp"][port]["state"]
                }
                host_data["ports"].append(port_data)

        hosts.append(host_data)

    # Output results
    if output_format is None or output_format == "console":
        print(json.dumps(hosts, indent=4))
    elif output_format == "json":
        with open("scan_results.json", "w") as f:
            json.dump(hosts, f)
