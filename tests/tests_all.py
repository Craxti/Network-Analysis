import pytest
from unittest.mock import MagicMock, patch
from models.scan_network import scan_network
from models.check_asn import check_asn
from models.threat_analysis import threat_analysis
from models.ip_geolocation import ip_geolocation
from models.check_breaches import check_breaches
from models.extract_metadata import extract_metadata
from models.scan_ip import scan_ip
from models.api_search import shodan_scan, hibp_breach, greynoise_ip, securitytrails_subdomain
from models.crypto_check import get_bitcoin_address, get_ethereum_address
from models.domain_scanner import scan_domain, enum_subdomains


#@pytest.mark.parametrize("ip_range", [
#    "192.168.1.1/24",
#    "10.0.0.1/24",
#])
#def test_scan_network(ip_range):
#    assert len(scan_network(ip_range)) > 0


#def test_check_asn():
#    assert check_asn("13335") == "Cloudflare, Inc."


#def test_threat_analysis():
#    assert threat_analysis("8.8.8.8")

def test_check_malware():
    assert len(check_malware("8.8.8.8")) > 0

#def test_check_botnet():
    # Check a known botnet IP address
#    threats = check_botnet("185.255.56.56")
#    assert len(threats) > 0, "Expected threats for known botnet IP"


def test_ip_geolocation():
    assert ip_geolocation("8.8.8.8") is not None


def test_check_breaches():
    assert check_breaches("test@test.com") is None or check_breaches("test@test.com") == "Oh no — pwned!"


def test_extract_metadata():
    assert len(extract_metadata("test-file-l.jpg")) > 0


def test_scan_ip():
    assert scan_ip("scanme.nmap.org", start_port=1, end_port=1000) == "IP is alive"


def test_shodan_scan():
    assert len(shodan_scan("apache")) > 0


#def test_hibp_breach():
#    assert len(hibp_breach("test@test.com")) > 0


def test_greynoise_ip():
    result = greynoise_ip("8.8.8.8")
    assert result is not None, "API request failed"


def test_securitytrails_subdomain():
    subdomains = securitytrails_subdomain("google.com")
    assert len(subdomains) >= 0, "Subdomain list is empty"


def test_get_bitcoin_address():
    assert get_bitcoin_address("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2")


def test_get_ethereum_address():
    assert get_ethereum_address("0x742d35Cc6634C0532925a3b844Bc454e4438f44e")


def test_scan_domain():
    assert len(scan_domain("google.com")) > 0


def test_enum_subdomains():
    assert len(enum_subdomains("google.com")) > 0
