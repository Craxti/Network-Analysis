import geoip2.database
import requests
import logging



def ip_geolocation(ip_address):
    try:
        # Open the GeoLite2-City database and get the geolocation data for the
        # IP address
        reader = geoip2.database.Reader('GeoLite2-City.mmdb')
        response = reader.city(ip_address)
        city = response.city.name
        country = response.country.name
        subdivision = response.subdivisions.most_specific.name
        latitude = response.location.latitude
        longitude = response.location.longitude
        reader.close()

        # Get the ASN information for the IP address
        url = f'https://rdap.arin.net/registry/ip/{ip_address}'
        response = requests.get(url).json()
        asn = response['entities'][0]['handle']
        asn_url = f'https://rdap.arin.net/registry/autnum/{asn}'
        response = requests.get(asn_url).json()
        asn_name = response['name']
        asn_description = response['entities'][0]['roles'][0]

        # Create a dictionary with the geolocation and ASN information
        geolocation = {
            'ip_address': str(ip_address),
            'city': city,
            'country': country,
            'subdivision': subdivision,
            'latitude': latitude,
            'longitude': longitude,
            'asn': asn,
            'asn_name': asn_name,
            'asn_description': asn_description
        }
        return geolocation

    except Exception as e:
        return str(e)
