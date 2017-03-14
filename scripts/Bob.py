# -*- coding: utf-8 -*-
from util.hook import cmd

@cmd
def hello(bot):
    if bot.cmd == "hello":
        bot.say("I'm Bob")

@cmd("goodby")
def goodby(bot):
    bot.say("Bob...")
