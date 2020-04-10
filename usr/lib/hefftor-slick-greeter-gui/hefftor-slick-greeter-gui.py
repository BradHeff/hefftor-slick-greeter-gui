# ============================================
#           Author Brad Heffernan
# ============================================

import gi
import GUI
import Functions as fn
import threading
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GdkPixbuf  # noqa


class SlickGreeterGUI(Gtk.Window):
    def __init__(self):
        super(SlickGreeterGUI, self).__init__(title="Slick Greeter GUI")
        self.connect("delete-event", self.close)
        # self.set_size_request(800, 600)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.timeout_id = None
        fn.copy(fn.root_config, fn.config)

        GUI.GUI(self, Gtk, fn, GdkPixbuf)

        t = threading.Thread(target=fn.pop_themes, args=(self,))
        t.daemon = True
        t.start()

        t = threading.Thread(target=fn.pop_icons, args=(self,))
        t.daemon = True
        t.start()

        fn.get_config(self, GdkPixbuf)

    def on_apply_clicked(self, widget):
        fn.set_config(self)
        fn.copy_root(fn.config, fn.root_config)
        fn.show_in_app_notification(self, "Config set successfully")

    def on_browser_clicked(self, widget):
        dialog = Gtk.FileChooserDialog(
                                       title="Please choose a file",
                                       action=Gtk.FileChooserAction.OPEN,)
        filter = Gtk.FileFilter()
        filter.set_name("IMAGE Files")
        filter.add_mime_type("image/png")
        filter.add_mime_type("image/jpg")
        filter.add_mime_type("image/jpeg")
        dialog.set_filter(filter)
        dialog.set_current_folder(fn.home)
        dialog.add_buttons(Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Open",
                           Gtk.ResponseType.OK)
        dialog.connect("response", self.open_response)

        dialog.show()

    def open_response(self, dialog, response):
        if response == Gtk.ResponseType.OK:
            self.wall.set_text(dialog.get_filename())
            pixbuf4 = GdkPixbuf.Pixbuf().new_from_file_at_size(self.wall.get_text(), 345, 345)  # noqa
            self.image.set_from_pixbuf(pixbuf4)
            dialog.destroy()
        elif response == Gtk.ResponseType.CANCEL:
            dialog.destroy()

    def close(self, widget, data):
        fn.os.unlink(fn.config)
        Gtk.main_quit()


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
