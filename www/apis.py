#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = ''

'''
JSON API definition
'''

import json, logging, inspect, functools

class APIError(Exception):
    '''
    the base APIError which contains error(required) and messages(option).
    '''
    def __init__(self, error, data='', message=''):
        super().__init__(message)
        self.error = error
        self.data = data
        self.message = message

class APIValuesError(APIError):
    '''
    Indicate the input value has error or invalid. The data specifies the error field of input form.
    '''
    def __init__(self, field, message=''):
        super().__init__('value:invalid', field, message)

class APIResourceNotFoundError(APIError):
    '''
    Indicate the resource was not found. The data specifies the error field of  input form.
    '''
    def __init__(self, field, message=''):
        super().__init__('value:not found', field, message)

class APIPermissionError(APIError):
    '''
    Indicate the api has no permission.
    '''
    def __init__(self, message=''):
        super().__init__('permission:forbidden', 'permission', message)