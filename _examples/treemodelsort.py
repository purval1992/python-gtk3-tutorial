#!/usr/bin/env python3

from gi.repository import Gtk

window = Gtk.Window()
window.set_default_size(200, -1)
window.connect("destroy", Gtk.main_quit)

liststore = Gtk.ListStore(str)
liststore.append(["Mark"])
liststore.append(["Chris"])
liststore.append(["Tim"])
liststore.append(["David"])
liststore.append(["Keith"])

treemodelsort = Gtk.TreeModelSort(liststore)
treemodelsort.set_sort_column_id(0, Gtk.SortType.ASCENDING)

treeview = Gtk.TreeView()
treeview.set_model(treemodelsort)
window.add(treeview)

cellrenderertext = Gtk.CellRendererText()
treeviewcolumn = Gtk.TreeViewColumn("Name", cellrenderertext, text=0)
treeview.append_column(treeviewcolumn)

window.show_all()

Gtk.main()
