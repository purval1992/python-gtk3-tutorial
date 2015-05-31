#!/usr/bin/env python3

from gi.repository import Gtk

def button_clicked(button):
    print("Button has been clicked!")

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

button = Gtk.Button(label="Button")
button.connect("clicked", button_clicked)
window.add(button)

window.show_all()

Gtk.main()
