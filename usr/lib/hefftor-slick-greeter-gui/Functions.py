# ============================================
#           Author Brad Heffernan
# ============================================
import os
# import subprocess
from pathlib import Path
# from time import sleep
# import threading
from gi.repository import GLib

home = os.path.expanduser("~")
base_dir = os.path.dirname(os.path.realpath(__file__))
config = "/etc/lightdm/slick-greeter.conf"
# here = Path(__file__).resolve()
working_dir = ''.join([str(Path(__file__).parents[2]),
                       "/share/hefftor-slick-greeter-gui/"])


def _get_position(lists, value):
    data = [string for string in lists if value in string]
    position = lists.index(data[0])
    return position


def pop_themes(self):
    with open(config, "r") as f:
        lines = f.readlines()
        f.close()

    main = _get_position(lines, "[Greeter]")
    pos = _get_position(lines[main:], "theme-name=")
    
    name = lines[main + pos].split("=")[1].strip()
    
    themes = os.listdir("/usr/share/themes")
    active = 0

    for x in range(0, len(themes)):
        GLib.idle_add(self.theme_combo.append_text, themes[x])
        if themes[x] == name:
            active = x
    GLib.idle_add(self.theme_combo.set_active, active)


def pop_icons(self):
    with open(config, "r") as f:
        lines = f.readlines()
        f.close()

    main = _get_position(lines, "[Greeter]")
    pos = _get_position(lines[main:], "icon-theme-name=")

    name = lines[main + pos].split("=")[1].strip()

    themes = os.listdir("/usr/share/icons")
    active = 0

    for x in range(0, len(themes)):
        GLib.idle_add(self.icon_combo.append_text, themes[x])
        if themes[x] == name:
            active = x
    GLib.idle_add(self.icon_combo.set_active, active)
