import sys
import traceback

class WException(Exception):
    def print(self):
        print (
           'Exception {}({})'.format ( type(self).__name__, self ),
           'at {}:{}'.format(
              sys.exc_info()[-1].tb_frame.f_code.co_filename,
              sys.exc_info()[-1].tb_lineno
           )
        )
        traceback.print_exc()

class WExceptionWidget(WException):
    def __init__(self,message):
        self.message = message
