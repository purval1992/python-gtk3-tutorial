#!/usr/bin/env python3

from gi.repository import Gtk

products = (("Apple", "Fruit", "£0.20"),
            ("Bleach", "Cleaning", "£1.20"),
            ("Bird Seed", "Pets", "£2.50"),
            ("Banana", "Fruit", "£0.35"),
            ("Beer", "Alcohol", "£2.75"),
            ("Cornflakes", "Cereal", "£1.10"),
            ("Pineapple", "Fruit", "£0.75"),
           )

def category_changed(combobox):
    treemodelfilter.refilter()

def filter_visible(model, treeiter, data):
    show = False

    if model[treeiter][1] == combobox.get_active_text():
        show = True
    elif combobox.get_active_text() == "All":
        show = True

    return show

window = Gtk.Window()
window.connect("destroy", Gtk.main_quit)

grid = Gtk.Grid()
grid.set_row_spacing(5)
window.add(grid)

scrolledwindow = Gtk.ScrolledWindow()
scrolledwindow.set_vexpand(True)
scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.NEVER)
grid.attach(scrolledwindow, 0, 0, 1, 1)

liststore = Gtk.ListStore(str, str, str)
treemodelfilter = liststore.filter_new()
treemodelfilter.set_visible_func(filter_visible, products)

combobox = Gtk.ComboBoxText()
combobox.append_text("All")
combobox.set_active(0)
combobox.connect("changed", category_changed)
grid.attach(combobox, 0, 1, 1, 1)

for product in products:
    liststore.append(product)

    combobox.append_text(product[1])

treeview = Gtk.TreeView()
treeview.set_model(treemodelfilter)
scrolledwindow.add(treeview)
cellrenderertext = Gtk.CellRendererText()
treeviewcolumn = Gtk.TreeViewColumn("Product", cellrenderertext, text=0)
treeview.append_column(treeviewcolumn)
treeviewcolumn = Gtk.TreeViewColumn("Category", cellrenderertext, text=1)
treeview.append_column(treeviewcolumn)
treeviewcolumn = Gtk.TreeViewColumn("Price", cellrenderertext, text=2)
treeview.append_column(treeviewcolumn)

window.show_all()

Gtk.main()
