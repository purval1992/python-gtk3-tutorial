#!/usr/bin/env python3

from gi.repository import Gtk


class FlowBoxExample(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.connect("destroy", Gtk.main_quit)

        flowbox = Gtk.FlowBox()
        self.add(flowbox)

        button = Gtk.Button("Start")
        flowbox.insert(button, 0)

        checkbutton1 = Gtk.CheckButton("Active")
        flowbox.insert(checkbutton1, 1)
        checkbutton2 = Gtk.CheckButton("Sensitive")
        flowbox.insert(checkbutton2, 2)

        label = Gtk.Label("GTK+ is a multi-platform widget toolkit used to create graphical applications.")
        flowbox.insert(label, 3)

        self.show_all()

FlowBoxExample()
Gtk.main()
