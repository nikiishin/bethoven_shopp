import pytest


@pytest.fixture()
def set_up():
    print('Start tests')


    yield
    print('Finish tests')