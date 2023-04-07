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


# Test scan_network.py
def test_scan_network():
    assert scan_network("192.168.0.1") == ["192.168.0.1", "192.168.0.2", "192.168.0.3", ...]


# Test check_asn.py
def test_check_asn():
    assert check_asn("8.8.8.8") == "AS15169 Google LLC"


# Test threat_analysis.py
def test_threat_analysis():
    assert "abuse" in threat_analysis("8.8.8.8")


# Test ip_geolocation.py
def test_ip_geolocation():
    assert "country" in ip_geolocation("8.8.8.8")


def test_geolocate_ip():
    assert geolocate_ip("google.com") == "8.8.8.8"


# Test check_breaches.py
def test_check_breaches():
    assert check_breaches("example@gmail.com") == ["Adobe", "Linkedin", "Dropbox", ...]


# Test extract_metadata.py
def test_extract_metadata():
    assert "title" in extract_metadata("https://github.com/")


# Test scan_ip.py
def test_scan_ip():
    assert scan_ip("8.8.8.8") == {"ports": {"53": "open"}, "os": "Linux"}


# Test api_search.py
def test_shodan_scan():
    assert "city" in shodan_scan("8.8.8.8")


def test_hibp_breach():
    assert "Adobe" in hibp_breach("example@gmail.com")


def test_greynoise_ip():
    assert "classification" in greynoise_ip("8.8.8.8")


def test_alienvault_ip():
    assert "reputation" in alienvault_ip("8.8.8.8")


def test_securitytrails_subdomain():
    assert "google.com" in securitytrails_subdomain("google.com")


# Test crypto_check.py
def test_get_bitcoin_address():
    assert get_bitcoin_address("alice") == "1L6YJU6zuLzkeCwpS6QMRW8oA2QtfT1mJi"


def test_get_ethereum_address():
    assert get_ethereum_address("alice") == "0x00c9e9E4F4Fc3a4b6cCe31Ea22E6C7aAC0525f8c"


# Test domain_scanner.py
def test_scan_domain():
    assert "Domain Name" in scan_domain("google.com")


def test_enum_subdomains():
    assert "drive.google.com" in enum_subdomains("google.com")
