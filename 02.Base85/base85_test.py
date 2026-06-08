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


def test_longs_encode():
    """
    Test random long encodes
    """
    assert base85ed.decode(b"2c5uJ4m90Tvrm578H668LGyfTF") == b"11N1a8i1BF0N<49D)F7382`@c9LjA?<(6"
    assert base85ed.decode(b"sr1vFDG432HnDHBuerCD42MJHR") == b"F)j!Y7RTa'1GVL=6qBXeATC.+1bqct85]"


def test_longs_decode():
    """
    Test random long decodes
    """
    assert base85ed.decode(b"11N1a8i1BF0N<49D)F7382`@c9LjA?<(6") == b"2c5uJ4m90Tvrm578H668LGyfTF"
    assert base85ed.decode(b"F)j!Y7RTa'1GVL=6qBXeATC.+1bqct85]") == b"sr1vFDG432HnDHBuerCD42MJHR"


def test_overflow():
    """
    Test if the function raises an exceptions
    """
    with pytest.raises(ValueError):
        base85ed.decode(b"~")
    with pytest.raises(ValueError):
        base85ed.decode(b"1234567890~")
