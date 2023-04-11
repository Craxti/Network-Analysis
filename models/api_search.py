import requests
import json

with open("models/keys.json") as f:
    keys = json.load(f)


# Shodan API
def shodan_scan(ip, timeout=10):
    api_key = keys["shodan"]
    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
    try:
        response = requests.get(url, timeout=timeout)
        return response.json()
    except requests.exceptions.Timeout:
        print(f"Error: Request timed out after {timeout} seconds")
        return None


# HaveIBeenPwned API
def hibp_breach(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {
        "hibp-api-key": keys["hibp"]
    }
    response = requests.get(url, headers=headers)
    return response.json()


# GreyNoise API
def greynoise_ip(ip):
    api_key = keys["greynoise"]
    url = f"https://api.greynoise.io/v3/community/{ip}"
    headers = {
        "key": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()


# AlienVault API
def alienvault_ip(ip):
    api_key = keys["alienvault"]
    url = f"https://otx.alienvault.com/api/v1/indicators/ip/{ip}/reputation"
    params = {
        "apikey": api_key
    }
    response = requests.get(url, params=params)
    return response.json()


# SecurityTrails API
def securitytrails_subdomain(domain):
    api_key = keys["securitytrails"]
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {
        "APIKEY": api_key
    }
    response = requests.get(url, headers=headers)
    return response.json()

# Тестирование функций
# ip = "8.8.8.8"
# email = "example@example.com"
# domain = "google.com"
# print("SHODAN:")
# pprint(shodan_scan(ip))
# print("HaveIBeenPwned:")
# pprint(hibp_breach(email))
# print("GreyNoise:")
# pprint(greynoise_ip(ip))
# print("AlienVault:")
# pprint(alienvault_ip(ip))
# print("SecurityTrails:")
# pprint(securitytrails_subdomain(domain))
