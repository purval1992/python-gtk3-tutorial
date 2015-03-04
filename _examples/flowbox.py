#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", lambda q: Gtk.main_quit())

flowbox = Gtk.FlowBox()
window.add(flowbox)

window.show_all()

Gtk.main()
