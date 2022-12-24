"""Test basic assertions, plus a few interesting ones"""
import pytest
from pytest import approx
from pytest import raises


def test_IntNotEqualAssert():
    assert 1 != 2


def test_IntAssertInequality():
    assert 1 <= 2


def test_StrAssert():
    assert "str" == "str"


def test_floatAssert():
    assert 1.0 == 1.0


def test_arrayAssert():
    assert [1, 2, 3] == [1, 2, 3]


def test_dictAssert():
    assert {"1": 1} == {"1": 1}


def test_BadFloatCompare():
    assert (0.1 + 0.2) == approx(0.3)


def raisesValueExepction():
    raise ValueError


def test_Exception():
    with raises(ValueError):
        raise raisesValueExepction()
