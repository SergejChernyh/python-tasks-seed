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
    assert base85ed.encode(b"2c5uJ4m90Tvrm578H668LGyfTF") == b"GGjG$N;GXbFjRJOZ8bMINH#V&Oh"
    assert base85ed.encode(b"sr1vFDG432HnDHBuerCD42MJHR") == b"b8<0uMnp$6GcrhSL`Xt)WpYDAG%`&}NKy"


def test_longs_decode():
    """
    Test random long decodes
    """
    assert base85ed.decode(b"GGjG$N;GXbFjRJOZ8bMINH#V&Oh") == b"2c5uJ4m90Tvrm578H668LGyfTF"
    assert base85ed.decode(b"b8<0uMnp$6GcrhSL`Xt)WpYDAG%`&}NKy") == b"sr1vFDG432HnDHBuerCD42MJHR"


def test_overflow():
    """
    Test if the function raises an exceptions
    """
    with pytest.raises(ValueError):
        base85ed.decode(b"~")
    with pytest.raises(ValueError):
        base85ed.decode(b"1234567890~")
