#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from constants import AWS_PROVIDER, ORACLE_PROVIDER, AZURE_PROVIDER
from returns.result import Result, Failure, Success
from logstrings import *
from typing import List


def validate_cli(parsed_cli: str) -> Result:
    # TODO -> Replace this big and dirty statement with pattern matching as
    # soon as python 3.10 releases
    if (
        (parsed_cli == AWS_PROVIDER)
        or (parsed_cli == ORACLE_PROVIDER)
        or (parsed_cli == AZURE_PROVIDER)
    ):
        return Result(Success(MESSAGE_VALID_PROVIER))
    else:
        return Result(Failure(MESSAGE_INVALID_PROVIDER))
        # TODO -> Call messenger


def validate_list_size(l: List[str]):
    list_length = len(l)
    is_even = lambda x: (x % 2) == 0
    if is_even(list_length):
        return Result(Success(MESSAGE_LIST_SIZE_EVEN))
    else:
        return Result(Failure(MESSAGE_LIST_SIZE_NOT_EVEN))
        # TODO -> CAll messenger
