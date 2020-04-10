# ============================================
#           Author Brad Heffernan
# ============================================
import os
import subprocess
from pathlib import Path
# from time import sleep
# import threading
from gi.repository import GLib

home = os.path.expanduser("~")
base_dir = os.path.dirname(os.path.realpath(__file__))
root_config = "/etc/lightdm/slick-greeter.conf"

# here = Path(__file__).resolve()
working_dir = ''.join([str(Path(__file__).parents[2]),
                       "/share/hefftor-slick-greeter-gui/"])
config = working_dir + "slick-greeter.conf"


def show_in_app_notification(self, message):
    if self.timeout_id is not None:
        GLib.source_remove(self.timeout_id)
        self.timeout_id = None

    self.notification_label.set_markup("<span foreground=\"white\">" +
                                       message + "</span>")
    self.notification_revealer.set_reveal_child(True)
    self.timeout_id = GLib.timeout_add(3000, timeOut, self)


def timeOut(self):
    close_in_app_notification(self)


def close_in_app_notification(self):
    self.notification_revealer.set_reveal_child(False)
    GLib.source_remove(self.timeout_id)
    self.timeout_id = None


def copy(src, dest):
    subprocess.run(["cp", src, dest])


def copy_root(src, dest):
    subprocess.run(["pkexec", "cp", src, dest])


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


def get_config(self, GdkPixbuf):
    with open(config, "r") as f:
        lines = f.readlines()
        f.close()

    main = _get_position(lines, "[Greeter]")
    pos_wall = _get_position(lines[main:], "background=")
    pos_num = _get_position(lines[main:], "activate-numlock=")
    pos_grid = _get_position(lines[main:], "draw-grid=")
    pos_power = _get_position(lines[main:], "show-power=")
    pos_quit = _get_position(lines[main:], "show-quit=")
    pos_clock = _get_position(lines[main:], "show-clock=")

    wall = lines[main + pos_wall].split("=")[1].strip()
    numlock = lines[main + pos_num].split("=")[1].strip()
    grid = lines[main + pos_grid].split("=")[1].strip()
    power = lines[main + pos_power].split("=")[1].strip()
    quit = lines[main + pos_quit].split("=")[1].strip()
    clock = lines[main + pos_clock].split("=")[1].strip()

    self.ch_grid.set_active(eval(grid.capitalize()))
    self.ch_power.set_active(eval(power.capitalize()))
    self.ch_quit.set_active(eval(quit.capitalize()))
    self.ch_clock.set_active(eval(clock.capitalize()))
    self.ch_num.set_active(eval(numlock.capitalize()))

    pixbuf4 = GdkPixbuf.Pixbuf().new_from_file_at_size(wall, 345, 345)  # noqa
    self.image.set_from_pixbuf(pixbuf4)
    self.wall.set_text(wall)


def set_config(self):
    with open(config, "r") as f:
        lines = f.readlines()
        f.close()

    main = _get_position(lines, "[Greeter]")
    pos_theme = _get_position(lines[main:], "theme-name=")
    pos_icon = _get_position(lines[main:], "icon-theme-name=")
    pos_wall = _get_position(lines[main:], "background=")
    pos_num = _get_position(lines[main:], "activate-numlock=")
    pos_grid = _get_position(lines[main:], "draw-grid=")
    pos_power = _get_position(lines[main:], "show-power=")
    pos_quit = _get_position(lines[main:], "show-quit=")
    pos_clock = _get_position(lines[main:], "show-clock=")

    lines[main + pos_theme] = "theme-name=" + self.theme_combo.get_active_text() + "\n"
    lines[main + pos_icon] = "icon-theme-name=" + self.icon_combo.get_active_text() + "\n"
    lines[main + pos_wall] = "background=" + self.wall.get_text() + "\n"

    lines[main + pos_num] = "activate-numlock=" + str(self.ch_num.get_active()).lower() + "\n"
    lines[main + pos_grid] = "draw-grid=" + str(self.ch_grid.get_active()).lower() + "\n"
    lines[main + pos_power] = "show-power=" + str(self.ch_power.get_active()).lower() + "\n"
    lines[main + pos_quit] = "show-quit=" + str(self.ch_quit.get_active()).lower() + "\n"
    lines[main + pos_clock] = "show-clock=" + str(self.ch_clock.get_active()).lower() + "\n"

    with open(config, "w") as f:
        f.writelines(lines)
        f.close()
