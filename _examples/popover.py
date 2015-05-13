#!/usr/bin/env python3

from gi.repository import Gtk


def button_clicked(button):
    popover.show_all()

window = Gtk.Window()
window.set_default_size(250, 250)
window.connect("destroy", Gtk.main_quit)

box = Gtk.Box()
box.set_orientation(Gtk.Orientation.VERTICAL)
window.add(box)

button = Gtk.Button("Popover Launcher")
button.connect("clicked", button_clicked)
box.add(button)

popover = Gtk.Popover()
popover.set_position(Gtk.PositionType.RIGHT)
popover.set_relative_to(button)

box = Gtk.Box()
box.set_spacing(5)
box.set_orientation(Gtk.Orientation.VERTICAL)
popover.add(box)

label = Gtk.Label("A Label widget")
box.add(label)

checkbutton = Gtk.CheckButton("A CheckButton widget")
box.add(checkbutton)

window.show_all()

Gtk.main()
