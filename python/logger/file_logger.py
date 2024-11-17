import os
from datetime import datetime as dt
from threading import Lock

from .utils import LogWriter


class FileLogger(LogWriter):
    def __init__(self, root='logs/', max_length='65536'):
        super().__init__()
        self.lock = Lock()
        self.file = None
        if not root.endswith('/') and not root.endswith('\\'):
            root += '/'
        self.root = root
        self.open_file()

    def write(self, lv, ts, msg):
        '''
        '''
        level = ''
        if lv == 2:
            level = 'ERROR! '
        if lv == 1:
            level = 'WARNING! '
        self.file.write(f'[{dt.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')}] {level}{msg}\n')


    def open_file(self):
        with self.lock:
            if not os.path.exists(self.root):
                os.makedirs(self.root)
            if self.file:
                self.file.close()
            self.file = open(f'{self.root}{dt.now().strftime('%Y-%m-%d-%H-%M-%S')}.log', 'a+')