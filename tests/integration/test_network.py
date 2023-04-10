import os
import pytest
from models.scan_network import scan_network
from models.scan_ip import scan_ip


def test_scan_network():
    result = scan_network("192.168.1.1/24", protocol="icmp")
    assert isinstance(result, list)


def test_scan_ip():
    result = scan_ip("192.168.1.1", 1, 100)
    assert isinstance(result, list)
