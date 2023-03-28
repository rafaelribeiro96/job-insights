import pytest
from src.pre_built.counter import count_ocurrences
from unittest.mock import mock_open, patch


@pytest.fixture
def read_file():
    return """
    This text is a test,
    this text is a test,
    this text is a test,
    this text is a test,
    this text not a test,
    """


def test_counter(read_file):
    with patch("builtins.open", mock_open(read_data=read_file)):
        assert count_ocurrences("filename", "this") == 5
        assert count_ocurrences("filename", "test") == 5
        assert count_ocurrences("filename", "is a") == 4
        assert count_ocurrences("filename", "not a") == 1
