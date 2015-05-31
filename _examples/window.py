#/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_title("Python GTK+ 3 Example")
window.connect("destroy", Gtk.main_quit)
window.show()

Gtk.main()
