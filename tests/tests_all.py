import os
import pytest
from models.scan_network import scan_network
from models.check_asn import check_asn
from models.threat_analysis import threat_analysis
from models.ip_geolocation import ip_geolocation, geolocate_ip
from models.check_breaches import check_breaches
from models.extract_metadata import extract_metadata
from models.scan_ip import scan_ip
from models.api_search import shodan_scan, hibp_breach, greynoise_ip, alienvault_ip, securitytrails_subdomain
from models.crypto_check import get_bitcoin_address, get_ethereum_address
from models.domain_scanner import scan_domain, enum_subdomains

@pytest.mark.parametrize("ip_range", [
    ("192.168.1.1/24"),
    ("10.0.0.1/24"),
])
def test_scan_network(ip_range):
    assert len(scan_network(ip_range)) > 0

def test_check_asn():
    assert check_asn("AS13335") == "CLOUDFLARENET - Cloudflare, Inc."

def test_threat_analysis():
    assert threat_analysis("google.com") == True

def test_ip_geolocation():
    assert ip_geolocation("8.8.8.8")["country_code"] == "US"
    assert geolocate_ip("8.8.8.8")["latitude"] == 37.751

def test_check_breaches():
    assert check_breaches("test@test.com") == "Oh no — pwned!"

def test_extract_metadata():
    assert len(extract_metadata("test_files")) > 0

def test_scan_ip():
    assert scan_ip("8.8.8.8") == "IP is alive"

def test_shodan_scan():
    assert len(shodan_scan("apache")) > 0

def test_hibp_breach():
    assert len(hibp_breach("test@test.com")) > 0

def test_greynoise_ip():
    assert greynoise_ip("8.8.8.8")["classification"] == "benign"

def test_alienvault_ip():
    assert len(alienvault_ip("8.8.8.8")) > 0

def test_securitytrails_subdomain():
    assert len(securitytrails_subdomain("google.com")) > 0

def test_get_bitcoin_address():
    assert get_bitcoin_address("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2") == True

def test_get_ethereum_address():
    assert get_ethereum_address("0x742d35Cc6634C0532925a3b844Bc454e4438f44e") == True

def test_scan_domain():
    assert len(scan_domain("google.com")) > 0

def test_enum_subdomains():
    assert len(enum_subdomains("google.com")) > 0
