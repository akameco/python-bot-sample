# -*- coding: utf-8 -*-
from os import path
from glob import glob
import sys
import importlib

class Bot(object):
    def __init__(self):
        self._cmd = ''
        self._listeners = []

    def add_listener(self, listener):
        self._listeners.append(listener)

    def say(self, m):
        print(m)

    @property
    def cmd(self):
        return self._cmd

    @cmd.setter
    def cmd(self, value):
        self._cmd = value

    def listen(self, cmd):
        self.cmd = cmd
        for l in self._listeners:
            if hasattr(l, "_command"):
                if l._command == self.cmd:
                    l(self)
            else:
                l(self)

def main():
    sys.path += ['scripts']
    bot = Bot()

    for f in glob('scripts/*.py'):
        module_name = path.splitext(path.basename(f))[0]
        module = importlib.import_module('scripts.' + module_name)
        for x in dir(module):
            method = getattr(module, x)
            if hasattr(method, "_hook"):
                bot.add_listener(getattr(module, x))

    bot.listen('hello')
    bot.listen('goodby')

if __name__ == '__main__':
    main()
