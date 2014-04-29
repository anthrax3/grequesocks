__author__ = 'TzAnAnY'

import requesocks as requesocks
import grequests as grequests


def grequesocks_send(self, **kwargs):
    merged_kwargs = {}
    merged_kwargs.update(self.kwargs)
    merged_kwargs.update(kwargs)
    del(merged_kwargs['stream'])
    self.response = self.session.request(self.method,
                                          self.url, **merged_kwargs)
    return self.response

# Do You Monkey Magic...
grequests.Session = requesocks.Session
setattr(grequests.AsyncRequest, 'send', grequesocks_send)

from grequests import *