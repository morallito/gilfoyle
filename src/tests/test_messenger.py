
from logstrings import MESSAGE_LOGGED_SUCCESSFULLY
from messenger.messenger import console_log_string
from returns.result import Result, Success
import pytest

@pytest.mark.parametrize("test_input,expected", [("any", Result(Success(MESSAGE_LOGGED_SUCCESSFULLY)))])
def test_eval(test_input, expected):
    assert console_log_string(test_input) == expected
