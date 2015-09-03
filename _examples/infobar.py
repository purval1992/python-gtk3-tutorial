#!/usr/bin/env python3

from gi.repository import Gtk

def infobar_changed(button, message_type):
    infobar.set_message_type(message_type)
    infobar.show()

def infobar_response(infobar, respose_id):
    infobar.hide()

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

vbox = Gtk.Box()
vbox.set_orientation(Gtk.Orientation.VERTICAL)
vbox.set_spacing(2)
window.add(vbox)

infobar = Gtk.InfoBar()
vbox.pack_start(infobar, True, True, 0)
infobar.add_button("Close", Gtk.ResponseType.CLOSE)
infobar.set_default_response(Gtk.ResponseType.CLOSE)
infobar.connect("response", infobar_response)

label = Gtk.Label("InfoBar example")
content = infobar.get_content_area()
content.add(label)

hbox = Gtk.Box()
hbox.set_orientation(Gtk.Orientation.HORIZONTAL)
hbox.set_spacing(2)
hbox.set_homogeneous(True)
vbox.pack_start(hbox, False, False, 0)

buttonInfo = Gtk.Button(label="_Info", use_underline=True)
buttonInfo.connect("clicked", infobar_changed, Gtk.MessageType.INFO)
hbox.pack_start(buttonInfo, True, True, 0)
buttonWarning = Gtk.Button(label="_Warning", use_underline=True)
buttonWarning.connect("clicked", infobar_changed, Gtk.MessageType.WARNING)
hbox.pack_start(buttonWarning, True, True, 0)
buttonError = Gtk.Button(label="_Error", use_underline=True)
buttonError.connect("clicked", infobar_changed, Gtk.MessageType.ERROR)
hbox.pack_start(buttonError, True, True, 0)
buttonQuestion = Gtk.Button(label="_Question", use_underline=True)
buttonQuestion.connect("clicked", infobar_changed, Gtk.MessageType.QUESTION)
hbox.pack_start(buttonQuestion, True, True, 0)

window.show_all()

Gtk.main()
