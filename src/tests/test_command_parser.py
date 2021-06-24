from logstrings import *
from command_parser.command_parser import *
from returns.result import Result, Success
import pytest

list_test_provider = [
    ("aws", Result(Success(MESSAGE_VALID_PROVIER))),
    ("azure", Result(Success(MESSAGE_VALID_PROVIER))),
    ("oracle", Result(Success(MESSAGE_VALID_PROVIER))),
    ("other", Result(Failure(MESSAGE_INVALID_PROVIDER))),
]
list_test_list_size = [
    (["a", "b"], Result(Success(MESSAGE_LIST_SIZE_EVEN))),
    (["a", "b", "c"], Result(Failure(MESSAGE_LIST_SIZE_NOT_EVEN))),
]


@pytest.mark.parametrize("test_input,expected", list_test_provider)
def test_eval(test_input, expected):
    assert validate_cli(test_input) == expected


@pytest.mark.parametrize("test_input,expected", list_test_list_size)
def test_eval(test_input, expected):
    assert validate_list_size(test_input) == expected
