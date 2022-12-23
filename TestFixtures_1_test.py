import pytest


@pytest.fixture()
def setup():
    print("\nSetup ***********")


def test1(setup):
    print("Executing test1 !")
    assert True
    # print("\nLeaving test1!")


@pytest.mark.usefixtures("setup")
def test2(setup):
    print("Executing test2 !")
    assert True
    # print("\nLeaving test2!")
