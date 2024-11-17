from datetime import datetime
from threading import Lock
import os
from .utils import LogWriter


__all__ = ['log']


PREF_R = '\033[31m'
PREF_G = '\033[32m'
PREF_Y = '\033[33m'
SUFF = '\033[0m'


# https://blog.csdn.net/cui_yonghua/article/details/129751013
def nefx_print(input, level):
    if level == -1:
        print(input)
    if level == 0:
        print(PREF_G + input + SUFF)
    if level == 1:
        print(PREF_Y + input + SUFF)
    if level == 2:
        print(PREF_R + input + SUFF)



# def log(input):
#     nefx_print(input, -1)

# def info(input):
#     nefx_print(input, 0)

# def warn(input):
#     nefx_print(input, 1)

# def error(input):
#     nefx_print(input, 2)


class NefxLogger():
    ''''''
    def __init__(self, **kwargs):
        
        # use_file = 'file' in kwargs
        # if use_file:
        #     file_config = kwargs['file']
        # use_backend = 'backend' in kwargs
        # if use_backend:
        #     backend_config = kwargs['use_backend']

        # use_backend = backend_config is not None
        self.writers = []

        pass

    def log(self, input):
        '''
        Output all log, For test.
        Not recommended for deployment environments.
        '''
        now = datetime.now()
        self.append_item(input, -1, now.timestamp())
        nefx_print(f'[{now.strftime('%Y-%m-%d %H:%M:%S')}] {input}', -1)
        return

    def info(self, input):
        now = datetime.now()
        self.append_item(input, 0, now.timestamp())
        nefx_print(f'[{now.strftime('%Y-%m-%d %H:%M:%S')}] {input}', 0)
        return

    def warn(self, input):
        now = datetime.now()
        self.append_item(input, 1, now.timestamp())
        nefx_print(f'[{now.strftime('%Y-%m-%d %H:%M:%S')}] {input}', 1)
        return

    def error(self, input):
        now = datetime.now()
        self.append_item(input, 2, now.timestamp())
        nefx_print(f'[{now.strftime('%Y-%m-%d %H:%M:%S')}] {input}', 2)
        return

    def append_item(self, input, level, timestamp):
        item = {
            'ts': timestamp,
            'lv': level,
            'msg': input
        }
        for writer in self.writers:
            if issubclass(LogWriter, type(writer)): 
                print('Wrong writer instance.')
                continue
            writer.write(level, timestamp, input)
        return 
    

class NefxLoggerBuilder():
    def __init__(self):
        ''''''
        self.logger = NefxLogger()

    def use_file(self):
        from .file_logger import FileLogger
        self.logger.writers.append(FileLogger())
        return self

    # def use_sqlite(self):
    #     from sqlite_logger import SqliteLogger
    #     self.logger.writers.append(SqliteLogger())

    def build(self):
        return self.logger