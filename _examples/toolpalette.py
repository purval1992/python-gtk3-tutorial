#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", Gtk.main_quit)

toolpalette = Gtk.ToolPalette()
window.add(toolpalette)

toolitemgroup = Gtk.ToolItemGroup(label="Group 1")
toolpalette.add(toolitemgroup)

toolbutton = Gtk.ToolButton()
toolbutton.set_icon_name("gtk-new")
toolitemgroup.insert(toolbutton, 0)
toolbutton = Gtk.ToolButton()
toolbutton.set_icon_name("gtk-open")
toolitemgroup.insert(toolbutton, 1)
toolbutton = Gtk.ToolButton()
toolbutton.set_icon_name("gtk-save")
toolitemgroup.insert(toolbutton, 2)

toolitemgroup = Gtk.ToolItemGroup(label="Group 2")
toolpalette.add(toolitemgroup)

toolbutton = Gtk.ToolButton()
toolbutton.set_icon_name("gtk-about")
toolitemgroup.insert(toolbutton, 0)
toolbutton = Gtk.ToolButton()
toolbutton.set_icon_name("gtk-preferences")
toolitemgroup.insert(toolbutton, 1)

window.show_all()

Gtk.main()
