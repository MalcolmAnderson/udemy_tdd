import pytest


@pytest.fixture()
def setup():
    print("\nSetup ***********")


def test1():
    print("\nExecuting test1!")
    assert True


def test2():
    print("\nExecuting test2!")
    assert True
