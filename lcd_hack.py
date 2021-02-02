#!/usr/bin/env python3


import fcntl  # only used my linux only code
import platform
import socket
import struct  # only used my linux only code
import sys

from RPLCD.i2c import CharLCD  # from https://github.com/dbrgn/RPLCD


def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def determine_ip():
    for devname in [b"eth0", b"eth1", b"eth2", b"wlan0", b"wlan1", b"wifi0", b"ath0", b"ath1", b"ppp0"]:
        try:
            ip = get_ip_address(devname)
            if not ip.startswith('127.'):
                return ip
                break
        except IOError:
            pass
    return 'unknown IP'



# FIXME pick up from config, see charmap demo?
lcd = CharLCD('PCF8574', 0x27)  # determine address via "i2cdetect -y 1"

argv = sys.argv
try:
    lcd_str = argv[1]
except IndexError:
    lcd_str = 'The quick brown fox jumps over the lazy dog'
    lcd_str = socket.gethostname() + '\n\r' + determine_ip()

lcd.clear()
lcd.write_string(lcd_str)

