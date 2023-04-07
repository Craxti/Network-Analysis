import requests
import json

def check_asn(ip_address):
    url = f"https://ipinfo.io/{ip_address}/json"
    response = requests.get(url)
    data = json.loads(response.text)

    return {"IP Address": ip_address, "ASN": data.get("org", "")}
