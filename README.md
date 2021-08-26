# lcd_hack

Quick app to use the LCD display that is included with the Recon Sentinel (https://hackaday.com/2020/11/16/teardown-recon-sentinel/) devices, viz a Rock64v2 connected over GPIO I²C port expander (using a PCF8574) to a Hitachi HD44780 controller.

See https://github.com/dhylands/python_lcd#custom-characters for indentifying which character sets are supported.


## Installing

If installing/working with a source checkout issue:

    sudo apt install python3-pip
    sudo pip3 install -r requirements.txt
    sudo pip3 install smbus2
    # or use virtualenv/venv (or local env)

See https://github.com/dbrgn/RPLCD for detailed install instructions.

See https://clach04.github.io/lcdchargen/ for custom character generator that emits Python (as well as C code), source code available from https://github.com/clach04/lcdchargen/tree/python

## Service

Systemd service (e.g. for Raspbian, Armbian, etc.).

Based on https://www.raspberrypi.org/documentation/linux/usage/systemd.md



NOTE hard coded paths in service file.

Install

    # edit lcd_hack.service  - see hard coded paths
    sudo cp lcd_hack.service /etc/systemd/system/lcd_hack.service
    sudo chmod 644 /etc/systemd/system/lcd_hack.service
    sudo systemctl enable lcd_hack.service

Usage

    sudo systemctl stop lcd_hack.service
    sudo systemctl start lcd_hack.service
    sudo systemctl restart lcd_hack.service
    sudo systemctl status lcd_hack.service  # status and recent logs
    sudo systemctl status lcd_hack.service -n 100  # show last 100 log entries
    journalctl  -u lcd_hack.service  # show all logs

    sudo systemctl status lcd_hack_https.service -n 100


    systemctl list-unit-files --state=enabled | grep lcd_hack

NOTE if changing service files, e.g. adding `Environment`, restart config (not just specific service):

    sudo systemctl daemon-reload
    sudo systemctl restart lcd_hack.service


