import pytest


def setup_module(module):
    print('\n1 Entering "setup_module"')
    print(module)
    # print('Leaving "setup_module"')


def teardown_module(module):
    print('1 Entering "teardown_module"')
    # print('Leaving "teardown_module"')


def setup_function(function):
    if function == test1:
        print('\nEntering "setup_function" for "test1"')
    elif function == test2:
        print('\nEntering "setup_function" for "test2"')
    else:
        print('\nEntering "setup_function" for UNKNOWN Test')
    # print('Leaving "setup_function"')


def teardown_function(function):
    if function == test1:
        print('\nEntering "teardown_function" for "test1"')
    elif function == test2:
        print('\nEntering "teardown_function" for "test2"')
    else:
        print('\nEntering "teardown_function" for UNKNOWN Test')
    # print('Leaving "teardown_function"')


def setup_class():
    print('\nEntering "setup_class" **********************')
    # print('Leaving "setup_class"')


def teardown_class():
    print('Entering "teardown_class" **********************')
    # print('Leaving "teardown_class"')


""" No Class class and method functions do not work"""


def setup_method(self, method):
    if method == self.test1:
        print('\nEntering "setup_method" for "test1"')
    elif method == self.test2:
        print('\nEntering "setup_method" for "test2"')
    else:
        print('\nEntering "setup_method" for UNKNOWN Test')
    # print('Leaving "setup_method"')


def teardown_method(self, method):
    if method == self.test1:
        print('\nEntering "teardown_method" for "test1"')
    elif method == self.test2:
        print('\nEntering "teardown_method" for "test2"')
    else:
        print('\nEntering "teardown_method" for UNKNOWN Test')
    # print('Leaving "teardown_method"')


def test1():
    print('Entering "test1"')
    assert True
    print('Leaving "test1"')


def test2():
    print('Entering "test2"')
    assert True
    print('Leaving "test2"')
