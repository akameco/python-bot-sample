# -*- coding: utf-8 -*-
from util.hook import cmd

@cmd("hello")
def hello(bot):
    bot.say("I'm Alice")

@cmd("goodby")
def goodby(bot):
    bot.say("アリス...さよなら...")

class TestBot(object):
    def __init__(self):
        pass
    @property
    def cmd(self):
        return 'hello'
    def say(self, m):
        print(m)

def main():
    bot = TestBot()
    hello(bot)

if __name__ == '__main__':
    main()
