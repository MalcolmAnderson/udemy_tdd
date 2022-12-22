import pytest


def fizzBuzz(value):
    return value


def test_canCallFizzBuzz():
    fizzBuzz(1)


def test_1_should_return_1():
    assert fizzBuzz(1) == 1


def test_2_should_return_2():
    assert fizzBuzz(2) == 2
