#!/usr/bin/env python3

# Shows how to allow closing of tabs within a Notebook widget via
# middle-clicking, as seen in the Firefox Web Browser and Thunar File Manager.

from gi.repository import Gtk


def construct_tab(count):
    title = "Tab %i" % (count)

    eventbox = Gtk.EventBox()
    tab_label = Gtk.Label(title)
    eventbox.add(tab_label)

    page_label = Gtk.Label(title)

    notebook.insert_page(page_label, eventbox, count)
    eventbox.connect("button-press-event", close_tab, page_label)

    tab_label.show()

def close_tab(widget, event, child):
    if event.button == 2:
        page = notebook.page_num(child)
        notebook.remove_page(page)

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("destroy", Gtk.main_quit)

notebook = Gtk.Notebook()
window.add(notebook)

for count in range(5):
    construct_tab(count)

window.show_all()

Gtk.main()
