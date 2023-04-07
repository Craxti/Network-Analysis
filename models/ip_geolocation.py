import requests


def ip_geolocation(ip_address):
    """
    Return info for geo IP-address for service ipapi
    """
    url = f"http://ipapi.co/{ip_address}/json/"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to get location information"}


def geolocate_ip(ip):
    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "success":
        country = data["country"]
        city = data["city"]
        lat = data["lat"]
        lon = data["lon"]
        return f"{ip} is located in {city}, {country} (lat: {lat}, lon: {lon})"
    else:
        return f"Failed to geolocate {ip}. Error: {data['message']}"
