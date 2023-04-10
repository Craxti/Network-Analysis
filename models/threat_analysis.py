import requests

def threat_analysis(ip_address):
    # IP-address or  URL-address or domen name
    url = f"https://ipinfo.io/{ip_address}/abuse"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        # VirusTotal API
        vt_url = f"https://www.virustotal.com/vtapi/v2/ip-address/report?apikey=API_KEY&ip={ip_address}"
        vt_response = requests.get(vt_url)
        vt_response.raise_for_status()
        vt_data = vt_response.json()

        # ThreatCrowd API
        tc_url = f"https://www.threatcrowd.org/searchApi/v2/ip/report/?ip={ip_address}"
        tc_response = requests.get(tc_url)
        tc_response.raise_for_status()
        tc_data = tc_response.json()

        # AbuseIPDB API
        ab_url = f"https://api.abuseipdb.com/api/v2/check?ipAddress={ip_address}&maxAgeInDays=90"
        ab_response = requests.get(ab_url, headers={"Key": "API_KEY"})
        ab_response.raise_for_status()
        ab_data = ab_response.json()

        #return dict all
        return {
            "ipinfo": data,
            "virustotal": vt_data,
            "threatcrowd": tc_data,
            "abuseipdb": ab_data
        }
    except requests.exceptions.HTTPError as e:
        return f"Error: {e}"
