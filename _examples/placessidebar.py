#!/usr/bin/env python3

from gi.repository import Gtk
from gi.repository import Gio

def open_link(placessiderbar, location, flags):
    location = placessidebar.get_location()

    print(GLocalFile.get_uri(location))

fp = Gio.File.new_for_uri("/mnt/test")

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

placessidebar = Gtk.PlacesSidebar()
placessidebar.add_shortcut(fp)
placessidebar.connect("open-location", open_link)
window.add(placessidebar)

window.show_all()

Gtk.main()
