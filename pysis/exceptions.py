#!/usr/bin/env python
# -*- encoding: utf-8 -*-


class InvalidBodySchema(Exception):
    """ Raised when the 'valids_body' attribute of Resource isn't in a
    valid form (required.issubsetof(schema))"""
    pass


class RequestDoesNotExist(Exception):
    """ Raised when `Request` factory can't find the subclass """
    pass


class UriInvalid(Exception):
    """ Raised when `Request` factory's maker isn't in a valid form """
    pass


class ValidationError(Exception):
    """ Raised when a `Request` doesn't have the necessary args to make a
    valid URI """
    pass

class UnprocessableEntity(Exception):
    """ Raised when server response is 400 """
    pass

class BadRequest(Exception):
    pass

class Unauthorized(Exception):
    pass

class Forbidden(Exception):
    pass

class NotFound(Exception):
    pass

class ServerError(Exception):
    pass
