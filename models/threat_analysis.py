import requests


def threat_analysis(ip_address):
    url = f"https://ipinfo.io/{ip_address}/abuse_reports"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        if not data:
            return f"No abuse reports found for {ip_address}"

        threats = {}
        for report in data:
            threat_type = report.get('category')
            if threat_type in threats:
                threats[threat_type].append(report)
            else:
                threats[threat_type] = [report]

        return threats
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"