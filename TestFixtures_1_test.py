import pytest


@pytest.fixture()
def setup1():
    # yield
    print("\nSetup 1  *")
    yield  # yield is a replacement for return
    print("\nYield TearDown")


@pytest.fixture()
def setup2(request):
    print("\nSetup 2  **")

    def teardown_a():
        print("\nTeardown A")

    def teardown_b():
        print("\nTeardown B")

    request.addfinalizer(teardown_a)
    request.addfinalizer(teardown_b)


def test1(setup1):
    print("\nExecuting test1 !")
    assert True
    # print("\nLeaving test1!")


def test2(setup2):
    print("\nExecuting test2 !")
    assert True
    # print("\nLeaving test2!")
