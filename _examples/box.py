#/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

box = Gtk.Box()
box.set_orientation(Gtk.Orientation.HORIZONTAL)
box.set_spacing(5)
window.add(box)

label = Gtk.Label(label="Label 1")
box.pack_start(label, True, True, 0)
label = Gtk.Label(label="Label 2")
box.pack_start(label, True, True, 0)
label = Gtk.Label(label="Label 3")
box.pack_start(label, True, True, 0)

window.show_all()

Gtk.main()
