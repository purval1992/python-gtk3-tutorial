#!/usr/bin/env python3

from gi.repository import Gtk

def on_button_clicked(button, page):
    name = "label%i" % page
    stack.set_visible_child_name(name)

window = Gtk.Window()
window.set_default_size(400, 300)
window.connect("destroy", Gtk.main_quit)

grid = Gtk.Grid()
window.add(grid)

stack = Gtk.Stack()
stack.set_vexpand(True)
stack.set_hexpand(True)
grid.attach(stack, 0, 0, 1, 1)

buttonbox = Gtk.ButtonBox()
buttonbox.set_layout(Gtk.ButtonBoxStyle.START)
grid.attach(buttonbox, 0, 1, 1, 1)

for page in range(1, 4):
    label = Gtk.Label("Stack Content on Page %i" % (page))
    name = "label%i" % page
    stack.add_named(label, name)

    button = Gtk.Button("Page %i" % (page))
    button.connect("clicked", on_button_clicked, page)
    buttonbox.add(button)

window.show_all()

Gtk.main()
