"""
Unit tests for 02.Base85
"""

import pytest
import base85ed


def test_shorts_encode():
    """
    Test trivial short encodes
    """
    assert base85ed.encode(b"1") == b"F#"
    assert base85ed.encode(b"12") == b"F){"
    assert base85ed.encode(b"123") == b"F)}j"
    assert base85ed.encode(b"1234") == b"F)}kW"


def test_shorts_decode():
    """
    Test trivial short decodes
    """
    assert base85ed.decode(b"F#") == b"1"
    assert base85ed.decode(b"F){") == b"12"
    assert base85ed.decode(b"F)}j") == b"123"
    assert base85ed.decode(b"F)}kW") == b"1234"


def test_len5_encode():
    """
    Test random long encodes
    """
    assert base85ed.encode(b"\x03/\x98\x8f\x12") == b"1234567"
    assert base85ed.encode(b"sr1vF") == b"b8<0uMg"


def test_len6_decode():
    """
    Test random long decodes
    """
    assert base85ed.decode(b"GGjG${") == b"2c5u"
    assert base85ed.decode(b"GGjG$") == b"2c5u"
    assert base85ed.decode(b"b8<0u0") == b"sr1v"
    assert base85ed.decode(b"b8<0u") == b"sr1v"


def test_overflow():
    """
    Test if the function raises an exceptions
    """
    assert base85ed.decode(b"|0") == b"\xff"
    assert base85ed.encode(b"\xff\xff\xff\xff") == b"|NsC0"

    assert base85ed.decode(b"|NsC0") == b"\xff\xff\xff\xff"
    with pytest.raises(ValueError):
        base85ed.decode(b"|NsC1")

    assert base85ed.decode(b"|0") == b"\xff"
    with pytest.raises(ValueError):
        base85ed.decode(b"|")
    
