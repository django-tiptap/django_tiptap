import pytest


@pytest.fixture
def fix():
    return "Hello"


def test_dummy(fix):
    assert fix
