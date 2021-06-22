#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from logstrings import MESSAGE_LOGGED_SUCCESSFULLY, MESSAGE_LOGGING_ERROR
from returns.result import Result, Failure, Success
from logstrings import *

def console_log_string (message: str)-> Result[Failure, Success]:
    try:
        print (message)
        return Result(Success(MESSAGE_LOGGED_SUCCESSFULLY))
    except Exception as error:
        return Result(Failure(MESSAGE_LOGGING_ERROR.format(error, message)))

