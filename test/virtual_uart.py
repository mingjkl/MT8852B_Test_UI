
import pty
import time

master1, slave1 = pty.openpty()
master2, slave2 = pty.openpty()