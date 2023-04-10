import os
import pytest
from models.api_search import shodan_scan, hibp_breach, greynoise_ip, alienvault_ip, securitytrails_subdomain


def test_shodan_scan():
    result = shodan_scan("apache")
    assert isinstance(result, dict)


def test_hibp_breach():
    result = hibp_breach("test@example.com")
    assert isinstance(result, list)


def test_greynoise_ip():
    result = greynoise_ip("8.8.8.8")
    assert isinstance(result, dict)


def test_alienvault_ip():
    result = alienvault_ip("8.8.8.8")
    assert isinstance(result, dict)


def test_securitytrails_subdomain():
    result = securitytrails_subdomain("google.com")
    assert isinstance(result, list)
