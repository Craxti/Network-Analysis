import requests
import json


def check_breaches(email):
    url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
    headers = {"User-Agent": "OSINT tool by ChatGPT"}
    response = requests.get(url, headers=headers)

    if response.status_code == 404:
        print(f"No breaches found for {email}")
    elif response.status_code == 200:
        breaches = json.loads(response.content)
        print(f"Breaches found for {email}:")
        for breach in breaches:
            print(f"\t{breach['Name']}")
    elif response.status_code == 429:
        print("Too many requests. Please try again later.")
    else:
        print("Something went wrong. Please try again later.")
