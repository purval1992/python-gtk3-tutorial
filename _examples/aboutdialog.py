#!/usr/bin/env python3

from gi.repository import Gtk, GdkPixbuf

class AboutDialog(Gtk.AboutDialog):
    def __init__(self):
        logo = GdkPixbuf.Pixbuf.new_from_file_at_size("../_resources/gtk.png", 64, 64)

        Gtk.AboutDialog.__init__(self)
        self.set_name("PyGObject Tutorial")
        self.set_version("1.0")
        self.set_comments("New tutorial on using Python with GTK+ 3")
        self.set_website("http://www.learngtk.org/")
        self.set_website_label("LearnGTK Website")
        self.set_authors(["Andrew Steele"])
        self.set_logo(logo)
        self.connect("response", self.on_response)

    def on_response(self, dialog, response):
        self.destroy()

aboutdialog = AboutDialog()
aboutdialog.run()
