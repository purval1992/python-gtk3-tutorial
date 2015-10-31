#!/usr/bin/env python3

from gi.repository import Gtk

class AspectFrame(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.set_default_size(200, 200)
        self.set_border_width(5)
        self.connect("destroy", Gtk.main_quit)

        label = Gtk.Label("Label in an AspectFrame")

        frame = Gtk.AspectFrame(label="AspectFrame",
                                xalign=0.5,
                                yalign=0.5,
                                ratio=1,
                                obey_child=False)
        frame.add(label)
        self.add(frame)

window = AspectFrame()
window.show_all()

Gtk.main()
