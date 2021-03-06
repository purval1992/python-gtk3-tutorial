#!/usr/bin/env python3

from gi.repository import Gtk

def font_chooser(fontchooserwidget, font):
    print("Font selected: %s" % font)

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

fontchooserwidget = Gtk.FontChooserWidget()
fontchooserwidget.connect("font-activated", font_chooser)
window.add(fontchooserwidget)

window.show_all()

Gtk.main()
