#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(400, 300)
window.connect("destroy", Gtk.main_quit)

grid = Gtk.Grid()
window.add(grid)

stack = Gtk.Stack()
stack.set_hexpand(True)
stack.set_vexpand(True)
grid.attach(stack, 1, 0, 1, 1)

stacksidebar = Gtk.StackSidebar()
stacksidebar.set_stack(stack)
grid.attach(stacksidebar, 0, 0, 1, 1)

for page in range(1, 4):
    label = Gtk.Label("Stack Content on Page %i" % (page))
    name = "label%i" % page
    title = "Page %i" % page
    stack.add_titled(label, name, title)

window.show_all()

Gtk.main()
