__author__ = 'RealGame (Tomer Zait)'
__version__ = '1.2'

import requesocks
import grequests


def __grequesocks_send(self, **kwargs):
    merged_kwargs = {'prefetch': kwargs.pop('stream')}
    merged_kwargs.update(self.kwargs)
    # Now you will get exception tuple if the request went wrong for better debugging.
    try:
        self.response = self.session.request(self.method,
                                             self.url, **merged_kwargs)
    except Exception as error:
        self.response = error, (self.method, self.url), merged_kwargs
        error_res, error_args, error_kwargs = self.response
        if ('hooks' in merged_kwargs) and ('response' in merged_kwargs['hooks']):
            callback = merged_kwargs['hooks']['response']
            callback(error_res, *error_args, **error_kwargs)

    return self.response

# Do You Monkey Magic...
grequests.Session = requesocks.Session
setattr(grequests.AsyncRequest, 'send', __grequesocks_send)

from grequests import *