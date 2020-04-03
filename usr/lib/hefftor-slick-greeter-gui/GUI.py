# ============================================
#           Author Brad Heffernan
# ============================================


def GUI(self, Gtk, fn):
    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    # vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.add(vbox)
    self.set_name("window")

    lbl1 = Gtk.Label(label="Theme Name")
    self.theme_combo = Gtk.ComboBoxText()

    lbl2 = Gtk.Label(label="Icon Name")
    self.icon_combo = Gtk.ComboBoxText()

    lbl3 = Gtk.Label(label="Font Name")
    self.font = Gtk.FontButton()

    hbox1.pack_start(lbl1, False, False, 0)
    hbox1.pack_start(self.theme_combo, False, False, 0)

    hbox2.pack_start(lbl2, False, False, 0)
    hbox2.pack_start(self.icon_combo, False, False, 0)

    hbox3.pack_start(lbl3, False, False, 0)
    hbox3.pack_start(self.font, False, False, 0)

    vbox.pack_start(hbox1, False, False, 0)
    vbox.pack_start(hbox2, False, False, 0)
    vbox.pack_start(hbox3, False, False, 0)

    fn.pop_themes(self)
