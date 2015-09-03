#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

buttonbox = Gtk.ButtonBox()
buttonbox.set_orientation(Gtk.Orientation.HORIZONTAL)
buttonbox.set_spacing(2)
window.add(buttonbox)

button = Gtk.Button(label="Sparrow")
buttonbox.add(button)
button = Gtk.Button(label="Wren")
buttonbox.add(button)
button = Gtk.Button(label="Great Spotted Woodpecker")
buttonbox.add(button)

window.show_all()

Gtk.main()
