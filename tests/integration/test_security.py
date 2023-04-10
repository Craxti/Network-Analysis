import os
import pytest
from models.threat_analysis import threat_analysis
from models.check_breaches import check_breaches


def test_threat_analysis():
    result = threat_analysis("tests/test_files/security_test_files")
    assert isinstance(result, list)


def test_check_breaches():
    result = check_breaches("tests/test_files/security_test_files/test_breach.txt")
    assert isinstance(result, list)
