import requests
from bs4 import BeautifulSoup


class Threat:
    def __init__(self, name, description, score):
        self.name = name
        self.description = description
        self.score = score

    def __str__(self):
        return f"{self.name} ({self.score}): {self.description}"


def check_malware(ip_address):
    threats = []

    # Check for malware and phishing using urlquery.net
    url = f"https://urlquery.net/ip/{ip_address}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Malware
    malware = soup.find("span", {"class": "label-danger"})
    if malware is not None:
        name = "Malware"
        description = "This IP has been associated with malware activity."
        score = 10
        threats.append(Threat(name, description, score))

    # Phishing
    phishing = soup.find("span", {"class": "label-warning"})
    if phishing is not None:
        name = "Phishing"
        description = "This IP has been associated with phishing activity."
        score = 8
        threats.append(Threat(name, description, score))

    # Check for malware using VirusTotal API
    url = "https://www.virustotal.com/vtapi/v2/ip-address/report"
    params = {
        "apikey": "YOUR_API_KEY",
        "ip": ip_address
    }
    response = requests.get(url, params=params)
    result = response.json()

    if result["response_code"] == 1 and "detected_urls" in result:
        name = "Malware"
        count = len(result["detected_urls"])
        description = f"This IP has been associated with {count} known malware URLs."
        score = count * 2
        threats.append(Threat(name, description, score))

    return threats


def check_botnet(ip_address):
    threats = []

    # Check for botnet activity using GreyNoise API
    url = "https://api.greynoise.io/v3/community/quick"
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Key": "YOUR_API_KEY"
    }
    data = {
        "ip": ip_address
    }
    response = requests.post(url, headers=headers, json=data)
    result = response.json()

    if "noise" in result and result["noise"] == "Botnet":
        name = "Botnet Activity"
        description = "This IP has been associated with botnet activity."
        score = 9
        threats.append(Threat(name, description, score))

    return threats


def check_brute_force(ip_address):
    threats = []

    # Check for brute force attacks using badips.com
    url = f"https://www.badips.com/get/list/ssh/2?ip={ip_address}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Brute force attacks
    badips = soup.find_all("tr")
    if len(badips) > 1:
        name = "Brute Force"
        description = f"This IP has been associated with {len(badips) - 1} SSH brute force attacks."
        score = len(badips) - 1
        threats.append(Threat(name, description, score))

    return threats


def threat_analysis(ip_address):
    threats = []

    threats += check_botnet(ip_address)
    threats += check_brute_force(ip_address)

    return threats

