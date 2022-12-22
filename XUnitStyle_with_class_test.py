import pytest


class TestClass:

    def setup_module(self, module):
        print('\n1 Entering "setup_module"')
        print(module)
        # print('Leaving "setup_module"')

    def teardown_module(self, module):
        print('1 Entering "teardown_module"')
        # print('Leaving "teardown_module"')

    def setup_function(self, function):
        if function == self.test1:
            print('\nEntering "setup_function" for "test1"')
        elif function == self.test2:
            print('\nEntering "setup_function" for "test2"')
        else:
            print('\nEntering "setup_function" for UNKNOWN Test')
        # print('Leaving "setup_function"')

    def teardown_function(self, function):
        if function == self.test1:
            print('\nEntering "teardown_function" for "test1"')
        elif function == self.test2:
            print('\nEntering "teardown_function" for "test2"')
        else:
            print('\nEntering "teardown_function" for UNKNOWN Test')
        # print('Leaving "teardown_function"')

    def setup_class(cls):
        print('\nEntering "setup_class" **********************')
        # print('Leaving "setup_class"')

    def teardown_class(cls):
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

    def test1(self):
        print('Entering "test1"')
        assert True
        print('Leaving "test1"')

    def test2(self):
        print('Entering "test2"')
        assert True
        print('Leaving "test2"')
