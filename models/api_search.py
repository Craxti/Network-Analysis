import requests
from bs4 import BeautifulSoup
import json


def shodan_scan(ip):
    url = f"https://www.shodan.io/host/{ip}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299"
    }
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")
        results = dict()
        results["ip"] = ip
        os_tag = soup.find("div", {"class": "os"})
        if os_tag is not None:
            results["os"] = os_tag.text.strip()
        else:
            results["os"] = "N/A"
        return results
    except Exception as e:
        print(e)
        return None



def hibp_breach(email):
    # Load API key from keys.json
    with open("keys.json") as f:
        keys = json.load(f)
        api_key = keys["hibp"]

    # Make API request
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"hibp-api-key": api_key}
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        results = []
        for item in response.json():
            result = dict()
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
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            results = dict()
            results["ip"] = ip
            updated = soup.find("td", string="UPDATED")
            if updated:
                results["last_seen"] = updated.find_previous_sibling("td").get_text()
            else:
                results["last_seen"] = ""
            classification = soup.find("td", string="DESCRIPTION2")
            if classification:
                results["classification"] = classification.find_previous_sibling("td").get_text().strip()
            else:
                results["classification"] = ""
            return results
        else:
            print(f"Error: Status code {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None



def alienvault_ip(ip):
    url = f"https://otx.alienvault.com/api/v1/indicators/ip/{ip}/reputation"
    try:
        response = requests.get(url)
        results = dict()
        results["ip"] = ip
        results["reputation"] = response.json()["reputation"]
        return results
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


def securitytrails_subdomain(domain):
    url = f"https://securitytrails.com/domain/{domain}/dns"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")
    subdomains = []
    for subdomain in soup.find_all("a", class_="node-name"):
        subdomains.append(subdomain.text)
    return subdomains


def virustotal_search(search_term):
    """
    Search VirusTotal for information related to a search term
    """
    url = f'https://www.virustotal.com/gui/search/{search_term}/files'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for result in soup.find_all('div', class_='enum-result'):
        name = result.find('a', class_='enum-link').text.strip()
        sha256 = result.find('span', class_='enum-file-hash').text.strip()
        results.append({'name': name, 'sha256': sha256})

    return results


def censys_search(search_term):
    """
    Search Censys for information related to a search term
    """
    url = f'https://censys.io/ipv4?q={search_term}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []

    for result in soup.find_all('tr'):
        ip_address = result.find(
            'a', class_='text-overflow-ellipsis').text.strip()
        port_protocol = result.find(
            'td', class_='protocol-popover').text.strip()
        results.append({'ip_address': ip_address,
                       'port_protocol': port_protocol})

    return results

# with open("keys.json") as f:
#    keys = json.load(f)


# Shodan API
# def shodan_scan(ip, timeout=10):
#    api_key = keys["shodan"]
#    url = f"https://api.shodan.io/shodan/host/{ip}?key={api_key}"
#    try:
#        response = requests.get(url, timeout=timeout)
#        return response.json()
#    except requests.exceptions.Timeout:
#        print(f"Error: Request timed out after {timeout} seconds")
#        return None


# HaveIBeenPwned API
# def hibp_breach(email):
#    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
#    headers = {
#        "hibp-api-key": keys["hibp"]
#    }
#    response = requests.get(url, headers=headers)
#    return response.json()


# GreyNoise API
# def greynoise_ip(ip):
#    api_key = keys["greynoise"]
#    url = f"https://api.greynoise.io/v3/community/{ip}"
#    headers = {
#        "key": api_key
#    }
#    response = requests.get(url, headers=headers)
#    return response.json()


# AlienVault API
# def alienvault_ip(ip):
#    api_key = keys["alienvault"]
#    url = f"https://otx.alienvault.com/api/v1/indicators/ip/{ip}/reputation"
#    params = {
#        "apikey": api_key
#    }
#    response = requests.get(url, params=params)
#    return response.json()


# SecurityTrails API
# def securitytrails_subdomain(domain):
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
