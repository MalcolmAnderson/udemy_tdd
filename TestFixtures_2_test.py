# use the following command to run tests
# pytest -v -s TestFixtures_2_test.py

import pytest

# Test Fixture scope
#   Function - Run fixture once for each test
#   Class - Run fixture once for each class of tests
#   Module - Run once when the module goes in scope
#   Session - The fixture is run when pytest starts


@pytest.fixture(scope="session", autouse=True)
def setupSession():
    print("\nSetup Session")


@pytest.fixture(scope="module", autouse=True)
def setupModule():
    print("\nSetup Module")


@pytest.fixture(scope="function", autouse=True)
def setupFunction():
    print("\nSetup Function")


def test1():
    print("\nExecuting test1 !")
    assert True


def test2():
    print("\nExecuting test2 !")
    assert True
