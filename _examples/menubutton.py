#!/usr/bin/env python3

from gi.repository import Gtk

class MenuButton(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self)
        self.connect("destroy", Gtk.main_quit)

        menubutton = Gtk.MenuButton("MenuButton")
        self.add(menubutton)

        menu = Gtk.Menu()
        menubutton.set_popup(menu)

        for count in range(1, 6):
            menuitem = Gtk.MenuItem("Item %i" % (count))
            menu.append(menuitem)

        menu.show_all()

window = MenuButton()
window.show_all()

Gtk.main()
