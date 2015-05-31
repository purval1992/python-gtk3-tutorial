#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

linkbutton = Gtk.LinkButton(uri="http://learngtk.org", label="LearnGTK")
window.add(linkbutton)

window.show_all()

Gtk.main()
