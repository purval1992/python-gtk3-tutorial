#!/usr/bin/env python3

from gi.repository import Gtk

class Layout(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        layout = Gtk.Layout()
        self.add(layout)

        button = Gtk.Button(label="Button 1")
        layout.put(button, 40, 60)
        button = Gtk.Button(label="Button 2")
        layout.put(button, 120, 95)

window = Layout()
window.show_all()

Gtk.main()
