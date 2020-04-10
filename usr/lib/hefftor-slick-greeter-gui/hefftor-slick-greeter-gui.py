# ============================================
#           Author Brad Heffernan
# ============================================

import gi
import GUI
import Functions as fn
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk  # noqa


class SlickGreeterGUI(Gtk.Window):
    def __init__(self):
        super(SlickGreeterGUI, self).__init__(title="Slick Greeter GUI")
        self.connect("delete-event", Gtk.main_quit)
        # self.set_size_request(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        GUI.GUI(self, Gtk, fn)

        t = threading.Thread(target=fn.pop_themes, args=(self,))
        t.daemon = True
        t.start()

        t = threading.Thread(target=fn.pop_icons, args=(self,))
        t.daemon = True
        t.start()


if __name__ == '__main__':
    style_provider = Gtk.CssProvider()
    style_provider.load_from_path(fn.base_dir + "/hefftor-slick-greeter-gui.css")  # noqa

    Gtk.StyleContext.add_provider_for_screen(
        Gdk.Screen.get_default(),
        style_provider,
        Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION
    )
    w = SlickGreeterGUI()
    w.show_all()
    Gtk.main()
