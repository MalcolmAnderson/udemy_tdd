import pytest


@pytest.fixture()
def setup():
    print("\nSetup ***********")


def test1(setup):
    print("\nExecuting test1!")
    assert True
    print("\nLeaving test1!")


def test2(setup):
    print("\nExecuting test2!")
    assert True
    print("\nLeaving test2!")
