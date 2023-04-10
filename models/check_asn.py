import requests


def check_asn(asn):
    url = f"https://stat.ripe.net/data/as-overview/data.json?resource=AS{asn}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if "data" not in data or "as-overview" not in data["data"]:
            return f"No information found for ASN {asn}"

        overview = data["data"]["as-overview"]
        asn_data = {
            "asn": overview["asn"],
            "holder": overview["holder"],
            "prefixes": overview["num-prefixes"],
            "peers": overview["num-peers"],
            "members": overview["num-members"],
            "routes": overview["num-routes"],
        }

        return asn_data

    except requests.exceptions.HTTPError as e:
        return f"Error: {e}"
