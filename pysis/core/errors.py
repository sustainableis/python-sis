# -*- encoding: utf-8 -*-

from pysis.exceptions import BadRequest, Unauthorized, Forbidden, NotFound, ServerError

class SISError(object):
    """ Handler for API errors """

    def __init__(self, reqURI, response):
        self.reqURI = reqURI
        self.response = response
        self.status_code = response[0]

    def process(self):
        raise_error = getattr(self, 'error_%s' % self.status_code, False)
        if raise_error:
            raise raise_error()
    
    def error_400(self):
        raise BadRequest("400 - %s\nRequest: %s" % (self.response[1].get('message'), self.reqURI))
    
    def error_401(self):
        raise Unauthorized("401 - %s\nRequest: %s" % (self.response[1].get('message'), self.reqURI))
    
    def error_403(self):
        raise Forbidden("403 - %s\nRequest: %s" % (self.response[1].get('message'), self.reqURI))
    
    def error_404(self):
        raise NotFound("404 - %s\nRequest: %s" % (self.response[1].get('message'), self.reqURI))
    
    def error_500(self):
        raise ServerError("500 - %s\nRequest: %s" % (self.response[1].get('message'), self.reqURI))
    
    
