import requests
from bs4 import BeautifulSoup

def check_asn(asn):
    url = f"https://ipinfo.io/AS{asn}"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        heading = soup.find("div", {"id": "block-whois"}).find("h2").text.strip()
        tables = soup.find_all("div", {"class": "border p-3"})
        result = {heading: {}}
        for table in tables:
            for pre in table.find_all("pre"):
                items = pre.text.split("\n\n")
                for item in items:
                    item = item.strip()
                    if item:
                        key, value = item.split(":", 1)
                        result[heading][key.strip()] = value.strip()
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None
asn_info = check_asn(13335)
print(asn_info)