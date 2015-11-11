#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(-1, 200)
window.connect("destroy", Gtk.main_quit)

headerbar = Gtk.HeaderBar()
headerbar.set_title("HeaderBar Example")
headerbar.set_subtitle("HeaderBar Subtitle")
headerbar.set_show_close_button(True)
window.set_titlebar(headerbar)

button = Gtk.Button("Open")
headerbar.pack_start(button)

window.show_all()

Gtk.main()
