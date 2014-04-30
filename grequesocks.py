__author__ = 'TzAnAnY'

import requesocks
import grequests


def __grequesocks_send(self, **kwargs):
    merged_kwargs = {'prefetch': kwargs.pop('stream')}
    merged_kwargs.update(self.kwargs)
    self.response = self.session.request(self.method,
                                          self.url, **merged_kwargs)
    return self.response

# Do You Monkey Magic...
grequests.Session = requesocks.Session
setattr(grequests.AsyncRequest, 'send', __grequesocks_send)

from grequests import *