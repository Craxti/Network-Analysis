import requests
from bs4 import BeautifulSoup


class Threat:
    def __init__(self, name, description, score):
        self.name = name
        self.description = description
        self.score = score

    def __str__(self):
        return f"{self.name} ({self.score}): {self.description}"


def threat_analysis(ip_address):
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
