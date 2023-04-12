import requests
from bs4 import BeautifulSoup

def check_breaches(email=None, username=None):
    # Check if either email or username was provided
    if email is None and username is None:
        print("Please provide either an email or a username.")
        return None

    # Define the base URL for the haveibeenpwned.com website
    base_url = "https://haveibeenpwned.com"

    # Check breaches by email address
    if email is not None:
        # Send a GET request to the haveibeenpwned.com API with the email address as a parameter
        url = f"{base_url}/unifiedsearch/{email}"
        response = requests.get(url)

        # Parse the HTML response with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the data from the HTML response
        data = {}
        for result in soup.find_all("div", class_="pwn-panel"):
            title = result.find("a", class_="pwn-link").text
            date = result.find("span", class_="pwn-date").text
            description = result.find("div", class_="pwn-description").text.strip()
            data[title] = {"Date": date, "Description": description}

        # Output the data
        if data:
            print(f"Breach data for email address {email}:")
            for title, details in data.items():
                print(f"\n{title}\nDate: {details['Date']}\nDescription: {details['Description']}")
        else:
            print(f"No breach data found for email address {email}.")

    # Check breaches by username
    if username is not None:
        # Send a GET request to the haveibeenpwned.com website with the username as a parameter
        url = f"{base_url}/Accounts/{username}"
        response = requests.get(url)

        # Check if the username was found
        if response.status_code == 404:
            print(f"No breach data found for username {username}.")
            return None

        # Parse the HTML response with BeautifulSoup
        soup = BeautifulSoup(response.content, "html.parser")

        # Extract the data from the HTML response
        data = {}
        for result in soup.find_all("div", class_="pwn"):
            title = result.find("div", class_="headline").text.strip()
            date = result.find("div", class_="date").text.strip()
            description = result.find("div", class_="description").text.strip()
            data[title] = {"Date": date, "Description": description}

        # Output the data
        if data:
            print(f"Breach data for username {username}:")
            for title, details in data.items():
                print(f"\n{title}\nDate: {details['Date']}\nDescription: {details['Description']}")
        else:
            print(f"No breach data found for username {username}.")
