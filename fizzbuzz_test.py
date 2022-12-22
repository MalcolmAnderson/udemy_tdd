import pytest


def fizzBuzz(value):
    retval = ""
    if value % 3 == 0:
        retval = "Fizz"
    if value % 5 == 0:
        retval += "Buzz"
    if retval == "":
        retval = str(value)
    return retval


def test_canCallFizzBuzz():
    fizzBuzz(1)


def test_1_should_return_1():
    assert fizzBuzz(1) == "1"


def test_2_should_return_2():
    assert fizzBuzz(2) == "2"


def test_3_should_return_Fizz():
    assert fizzBuzz(3) == "Fizz"


def test_5_should_return_Buzz():
    assert fizzBuzz(5) == "Buzz"


def test_6_should_return_Fizz():
    assert fizzBuzz(6) == "Fizz"


def test_10_should_return_Buzz():
    assert fizzBuzz(10) == "Buzz"


def test_15_should_return_FizzBuzz():
    assert fizzBuzz(15) == "FizzBuzz"


def test_30_should_return_FizzBuzz():
    assert fizzBuzz(30) == "FizzBuzz"


for i in range(1, 32):
    print(fizzBuzz(i))
