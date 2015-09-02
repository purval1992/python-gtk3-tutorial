#!/usr/bin/env python3

from gi.repository import Gtk

def on_show_heading_change(checkbutton):
    calendar.set_property("show-heading", checkbutton.get_active())

def on_show_days_change(checkbutton):
    calendar.set_property("show-day-names", checkbutton.get_active())

def on_prevent_month_change(checkbutton):
    calendar.set_property("no-month-change", checkbutton.get_active())

def on_show_weeks_change(checkbutton):
    calendar.set_property("show-week-numbers", checkbutton.get_active())

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

hbox = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=2)
window.add(hbox)

calendar = Gtk.Calendar()
hbox.pack_start(calendar, True, True, 0)

vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=2)
hbox.pack_start(vbox, False, False, 0)

checkbuttonHeading = Gtk.CheckButton(label="Show Heading")
checkbuttonHeading.set_active(True)
checkbuttonHeading.connect("toggled", on_show_heading_change)
vbox.pack_start(checkbuttonHeading, False, False, 0)

checkbuttonDayNames = Gtk.CheckButton(label="Show Day Names")
checkbuttonDayNames.set_active(True)
checkbuttonDayNames.connect("toggled", on_show_days_change)
vbox.pack_start(checkbuttonDayNames, False, False, 0)

checkbuttonPreventChange = Gtk.CheckButton(label="Prevent Month/Year Change")
checkbuttonPreventChange.connect("toggled", on_prevent_month_change)
vbox.pack_start(checkbuttonPreventChange, False, False, 0)

checkbuttonShowWeeks = Gtk.CheckButton(label="Show Week Numbers")
checkbuttonShowWeeks.connect("toggled", on_show_weeks_change)
vbox.pack_start(checkbuttonShowWeeks, False, False, 0)

window.show_all()

Gtk.main()
