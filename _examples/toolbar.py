#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(500, -1)
window.connect("destroy", Gtk.main_quit)

toolbar = Gtk.Toolbar()
window.add(toolbar)

toolbutton = Gtk.ToolButton()
toolbutton.set_is_important(True)
toolbutton.set_icon_name("gtk-new")
toolbar.add(toolbutton)

toggletoolbutton = Gtk.ToggleToolButton()
toggletoolbutton.set_icon_name("gtk-media-play")
toolbar.add(toggletoolbutton)

menu = Gtk.Menu()
menuitem = Gtk.MenuItem(label="MenuItem")
menu.append(menuitem)

menutoolbutton = Gtk.MenuToolButton()
menutoolbutton.set_menu(menu)
menutoolbutton.set_icon_name("gtk-open")
toolbar.add(menutoolbutton)

separatortoolitem = Gtk.SeparatorToolItem()
toolbar.add(separatortoolitem)

radiotoolbutton1 = Gtk.RadioToolButton()
radiotoolbutton1.set_icon_name("gtk-media-rewind")
toolbar.add(radiotoolbutton1)
radiotoolbutton2 = Gtk.RadioToolButton(group=radiotoolbutton1)
radiotoolbutton2.set_icon_name("gtk-media-forward")
toolbar.add(radiotoolbutton2)

separatortoolitem = Gtk.SeparatorToolItem()
toolbar.add(separatortoolitem)

toolitem = Gtk.ToolItem()
entry = Gtk.Entry()
toolitem.add(entry)
toolbar.add(toolitem)

menuitem.show()
window.show_all()

Gtk.main()
