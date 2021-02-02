# lcd_hack

If installing/working with a source checkout issue:

    sudo apt install python3-pip
    sudo pip3 install -r requirements.txt
    sudo pip3 install smbus2
    # or use virtualenv/venv (or local env)

See https://github.com/dbrgn/RPLCD for detailed install instructions.

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


