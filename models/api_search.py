import requests
import json
from bs4 import BeautifulSoup


def shodan_scan(ip):
    url = f"https://www.shodan.io/host/{ip}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
    }
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        results = {}
        results["ip"] = ip
        results["os"] = soup.find("div", {"class": "os"}).text.strip()
        results["hostnames"] = [i.text.strip() for i in soup.find_all("a", {"class": "ellipsis"})]
        results["ports"] = [i.text.strip() for i in soup.find_all("span", {"class": "tag tag-default"}) if ":" in i.text.strip()]
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def hibp_breach(email):
    url = f"https://haveibeenpwned.com/unifiedsearch/{email}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
    }
    try:
        response = requests.get(url, headers=headers)
        results = []
        for item in response.json()["Breaches"]:
            result = {}
            result["title"] = item["Title"]
            result["date"] = item["BreachDate"]
            result["description"] = item["Description"]
            results.append(result)
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def greynoise_ip(ip):
    url = f"https://viz.greynoise.io/ip/{ip}"
    try:
        response = requests.get(url)
        results = {}
        results["ip"] = ip
        results["last_seen"] = response.json()["last_seen"]
        results["classification"] = response.json()["classification"]
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def alienvault_ip(ip):
    url = f"https://otx.alienvault.com/api/v1/indicators/ip/{ip}/reputation"
    try:
        response = requests.get(url)
        results = {}
        results["ip"] = ip
        results["reputation"] = response.json()["reputation"]
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def securitytrails_subdomain(domain):
    url = f"https://securitytrails.com/list/ip/{domain}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    subdomains = []
    for subdomain in soup.find_all("a", class_="node-name"):
        subdomains.append(subdomain.text)
    return subdomains

#with open("keys.json") as f:
#    keys = json.load(f)


# Shodan API
#def shodan_scan(ip, timeout=10):
#    api_key = keys["shodan"]
#    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
#    try:
#        response = requests.get(url, timeout=timeout)
#        return response.json()
#    except requests.exceptions.Timeout:
#        print(f"Error: Request timed out after {timeout} seconds")
#        return None


# HaveIBeenPwned API
#def hibp_breach(email):
#    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
#    headers = {
#        "hibp-api-key": keys["hibp"]
#    }
#    response = requests.get(url, headers=headers)
#    return response.json()


# GreyNoise API
#def greynoise_ip(ip):
#    api_key = keys["greynoise"]
#    url = f"https://api.greynoise.io/v3/community/{ip}"
#    headers = {
#        "key": api_key
#    }
#    response = requests.get(url, headers=headers)
#    return response.json()


# AlienVault API
#def alienvault_ip(ip):
#    api_key = keys["alienvault"]
#    url = f"https://otx.alienvault.com/api/v1/indicators/ip/{ip}/reputation"
#    params = {
#        "apikey": api_key
#    }
#    response = requests.get(url, params=params)
#    return response.json()


# SecurityTrails API
#def securitytrails_subdomain(domain):
#    api_key = keys["securitytrails"]
#    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
#    headers = {
#        "APIKEY": api_key
#    }
#    response = requests.get(url, headers=headers)
#    return response.json()

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
