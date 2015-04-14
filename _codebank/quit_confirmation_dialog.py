#!/usr/bin/env python3

# Provides an example of asking the user to confirm they wish to quit the
# application.

from gi.repository import Gtk


def window_delete_event(window, event):
    messagedialog = Gtk.MessageDialog()
    messagedialog.add_button("Do Not Quit", Gtk.ResponseType.CANCEL)
    messagedialog.add_button("Quit", Gtk.ResponseType.OK)
    messagedialog.set_markup("Quit the program?")

    if messagedialog.run() == Gtk.ResponseType.OK:
        state = False

        Gtk.main_quit()

    messagedialog.destroy()

    return True

window = Gtk.Window()
window.set_default_size(200, 200)
window.connect("delete-event", window_delete_event)
window.show_all()

Gtk.main()
