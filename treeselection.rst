TreeSelection
=============
A TreeSelection is an object that allows for management of selections within a :doc:`treeview`.

=======
Methods
=======
To set the type of selection which the TreeSelection allows, call::

  treeselection.set_mode(mode)

The *mode* can be set to one of the following; ``Gtk.SelectionType.NONE`` which prevents a selection, ``Gtk.SelectionType.SINGLE`` that allows only a none or one item to be selected, ``Gtk.SelectionType.BROWSE`` enforces a single item to be selected, or ``Gtk.SelectionType.MULTIPLE`` which allows selecting of multiple items by holding the :kbd:`Control` key or by click-and-drag. By default, ``Gtk.SelectionType.SINGLE`` is the default selection mode.

The selection mode can be gathered with the method::

  mode = treeselection.get_mode()

Retrieval of the selected item when ``Gtk.SelectionType.SINGLE`` or ``Gtk.SelectionType.BROWSE`` is used can be made with::

  selected = treeselection.get_selected(model, treeiter)

The *model* value should be set to the :doc:`liststore` or :doc:`treestore` of the current data store. The *treeiter* value also identifies the specific row which is selected.

To select or unselect all the items in the TreeSelection call::

  treeselection.select_all()
  treeselection.unselect_all()

Counting the number of selected rows which the TreeSelection has can be done with the method::

  count = treeselection.count_selected_rows()

The TreeView which is associated with the TreeSelection can be found via::

  treeview = treeselection.get_tree_view()

=======
Signals
=======
The common signals of the TreeSelection are

  "changed" (treeselection)

When the currently selected items within the TreeSelection are changed, the ``"changed"`` signal is emitted.
