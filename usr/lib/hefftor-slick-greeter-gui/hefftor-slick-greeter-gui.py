# ============================================
#           Author Brad Heffernan
# ============================================

import gi
import GUI
import Functions as fn
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk  # noqa


class SlickGreeterGUI(Gtk.Window):
    def __init__(self):
        super(SlickGreeterGUI, self).__init__(title="Slick Greeter GUI")
        self.connect("delete-event", Gtk.main_quit)
        GUI.GUI(self, Gtk, fn)


if __name__ == '__main__':
    w = SlickGreeterGUI()
    w.show_all()
    Gtk.main()
