#!/usr/bin/env python3

from gi.repository import Gtk

dialog = Gtk.Dialog()
dialog.set_title("Dialog Example")
dialog.set_default_size(400, 300)
dialog.add_button("OK", Gtk.ResponseType.OK)
dialog.add_button("Cancel", Gtk.ResponseType.CANCEL)

response = dialog.run()

if response == Gtk.ResponseType.OK:
    print("OK button clicked")
elif response == Gtk.ResponseType.CANCEL:
    print("Cancel button clicked")
else:
    print("Dialog closed")

dialog.destroy()
