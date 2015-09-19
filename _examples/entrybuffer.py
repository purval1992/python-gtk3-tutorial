#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

box = Gtk.Box()
box.set_orientation(Gtk.Orientation.VERTICAL)
box.set_spacing(5)
window.add(box)

entrybuffer = Gtk.EntryBuffer()
entrybuffer.set_text("Text in EntryBuffer", -1)

entry = Gtk.Entry()
entry.set_buffer(entrybuffer)
box.pack_start(entry, True, True, 0)
entry = Gtk.Entry()
entry.set_buffer(entrybuffer)
box.pack_start(entry, True, True, 0)
entry = Gtk.Entry()
entry.set_buffer(entrybuffer)
box.pack_start(entry, True, True, 0)

window.show_all()

Gtk.main()
