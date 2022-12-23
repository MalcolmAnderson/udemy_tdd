# run 2 and 3 together (they are meant to be paired)
# pytest -v -s TestFixtures_2_test.py TestFixtures_3_test.py

import pytest


# Test Fixture scope
#   Function - Run fixture once for each test
#   Class - Run fixture once for each class of tests
#   Module - Run once when the module goes in scope
#   Session - The fixture is run when pytest starts


# @pytest.fixture(scope="session", autouse=True)
# def setupSession():
#     print("\nSetup Session")


@pytest.fixture(scope="module", autouse=True)
def setupModule2():
    print("\nSetup Module2")


@pytest.fixture(scope="class", autouse=True)
def setupClass2():
    print("\nSetup Class2")


@pytest.fixture(scope="function", autouse=True)
def setupFunction2():
    print("\nSetup Function2")


class TestClass:
    def test_it(self):
        print("\nExecuting Test It")
        assert True

    def test_it2(self):
        print("\nExecuting Test It 2")
        assert True
