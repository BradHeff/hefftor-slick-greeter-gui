# ============================================
#           Author Brad Heffernan
# ============================================


def GUI(self, Gtk, fn, GdkPixbuf):
    hb = Gtk.HeaderBar()
    hb.props.show_close_button = True
    hb.props.title = "Hefftors Slick Greeter Tool"
    hb.props.subtitle = "Safely configure slick greeter with ease"
    self.set_titlebar(hb)

    # =======================================================
    #                       App Notifications
    # =======================================================

    self.notification_revealer = Gtk.Revealer()
    self.notification_revealer.set_reveal_child(False)

    self.notification_label = Gtk.Label()

    pb_panel = GdkPixbuf.Pixbuf().new_from_file(fn.working_dir + 'panel.png')
    panel = Gtk.Image().new_from_pixbuf(pb_panel)

    overlayFrame = Gtk.Overlay()
    overlayFrame.add(panel)
    overlayFrame.add_overlay(self.notification_label)

    self.notification_revealer.add(overlayFrame)

    vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    vbox2 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    main = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hbox1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox3 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)
    hbox4 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    hboxbtn = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    self.add(vbox)
    self.set_name("window")

    hbox4.pack_start(self.notification_revealer, True, False, 0)

    lbl1 = Gtk.Label(label="Theme Name")
    self.theme_combo = Gtk.ComboBoxText()

    lbl2 = Gtk.Label(label="Icon Name")
    self.icon_combo = Gtk.ComboBoxText()

    lbl3 = Gtk.Label(label="Wallpaper")
    self.wall = Gtk.Entry()
    btn_browse = Gtk.Button(label="...")
    btn_browse.connect("clicked", self.on_browser_clicked)

    self.ch_grid = Gtk.CheckButton(label="Draw Grid")
    self.ch_power = Gtk.CheckButton(label="Show Power")
    self.ch_quit = Gtk.CheckButton(label="Show Quit")
    self.ch_clock = Gtk.CheckButton(label="Show Clock")
    self.ch_num = Gtk.CheckButton(label="Enable Numlock")

    flow = Gtk.FlowBox()
    flow.add(self.ch_grid)
    flow.add(self.ch_power)
    flow.add(self.ch_quit)
    flow.add(self.ch_clock)
    flow.add(self.ch_num)

    btn = Gtk.Button(label="Apply Changes")
    btn.set_name("apply")
    btn.connect("clicked", self.on_apply_clicked)

    self.image = Gtk.Image()

    hbox1.pack_start(lbl1, False, False, 0)
    hbox1.pack_start(self.theme_combo, False, False, 0)

    hbox2.pack_start(lbl2, False, False, 0)
    hbox2.pack_start(self.icon_combo, False, False, 0)

    hbox3.pack_start(lbl3, False, False, 0)
    hbox3.pack_start(self.wall, True, True, 0)
    hbox3.pack_start(btn_browse, False, False, 0)

    hboxbtn.pack_end(btn, False, False, 0)

    vbox1.pack_start(hbox1, False, False, 0)
    vbox1.pack_start(hbox2, False, False, 0)
    vbox1.pack_start(hbox3, False, False, 0)
    vbox1.pack_start(flow, False, False, 0)
    vbox1.pack_end(hboxbtn, False, False, 0)

    vbox2.pack_end(self.image, True, False, 0)

    main.pack_start(vbox1, False, False, 0)
    main.pack_start(vbox2, True, False, 0)

    vbox.pack_start(hbox4, False, False, 0)
    vbox.pack_start(main, True, True, 0)