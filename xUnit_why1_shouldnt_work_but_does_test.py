import pytest


def setup_module():
    print('\n1 Entering "setup_module"                                           shouldn\'t work but does')
    # print('Leaving "setup_module"')


def teardown_module():
    print('1 Entering "teardown_module"')
    # print('Leaving "teardown_module"')


def setup_function():
    print('\nEntering "setup_function"')
    # print('Leaving "setup_function"')


def teardown_function():
    print('\nEntering "teardown_function"')
    # print('Leaving "teardown_function"')


def setup_class():
    print('\nEntering "setup_class" **********************')
    # print('Leaving "setup_class"')


def teardown_class():
    print('Entering "teardown_class" **********************')
    # print('Leaving "teardown_class"')


def setup_method():
    print('\nEntering "setup_method"')
    # print('Leaving "setup_method"')


def teardown_method():
    print('Entering "teardown_method"')
    # print('Leaving "teardown_method"')


def test1():
    print('Entering "test1"')
    assert True
    print('Leaving "test1"')


def test2():
    print('Entering "test2"')
    assert True
    print('Leaving "test2"')
