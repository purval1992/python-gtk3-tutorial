#!/usr/bin/env python3

from gi.repository import Gtk

aboutdialog = Gtk.AboutDialog()
aboutdialog.set_name("PyGObject Tutorial")
aboutdialog.set_version("1.0")
aboutdialog.set_comments("New tutorial on using Python with GTK+ 3")
aboutdialog.set_website("http://www.learngtk.org/")
aboutdialog.set_website_label("LearnGTK Website")
aboutdialog.set_authors(["Andrew Steele"])

aboutdialog.run()
aboutdialog.destroy()
