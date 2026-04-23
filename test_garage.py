import pytest
from garage import enter_garage

def test_entergarage():
    assert enter_garage() == True