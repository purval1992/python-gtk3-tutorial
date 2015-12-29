ListStore
=========
A ListStore is a flat-layout storage model which allows the storage of a range of data including textual strings, integer and floating values, images and Boolean values. It is used as the storage area for a range of widgets including TreeView, IconView and ComboBox.

===========
Constructor
===========
The ListStore can be constructed using the following::

  liststore = Gtk.ListStore(data_types)

The *data_types* parameter can be set to a number of supported types. These includes those from Python; ``str``, ``float``, ``long``, ``int``, ``bool``, and ``object``. Alternatively, GTK provides the following; ``gchar``, ``guchar``, ``gboolean``, ``gint``, ``guint``, ``glong``, ``gulong``, ``gint64``, ``guint64``, ``gfloat``, ``gdouble``, ``gchararray``, and ``GObject``.

.. note::

  There is no preference over which data type to use, however for simplicity it is often easier to use the Python data types.

To store data in the ListStore, the type of data being entered must match the data type specified. For example, if you attempt to insert an integer into a string, you will receive an error.

=======
Methods
=======
Values can be inserted into the ListStore in a few ways::

  liststore.insert([data], position)
  liststore.append([data])
  liststore.prepend([data])

The ``.insert()`` method requires two arguments; the *position* of where to enter the data and a list containing the data. The ``.append()`` and ``.prepend()`` methods add data to the back or front of the ListStore depending on the order the code is written.

An item can be removed by calling::

  liststore.remove(treeiter)

The *treeiter* parameter should be a TreeIter object retrieved using the methods specified on the page.

The values currently held in the ListStore can be cleared using::

  liststore.clear()

Values contained within the ListStore can swap position with::

  liststore.swap(position_a, position_b)

The *position_a* and *position_b* arguments should be TreeIter objects relating to each of the rows which are to be swapped.

To reorder all the items in a ListStore call::

  liststore.reorder([positions])

The *positions* list passes the new position of each child. The method only works on unsorted ListStore objects.

An item in the ListStore can be moved before or after another item with the methods::

  liststore.move_before(treeiter, position)
  liststore.move_after(treeiter, position)

The *treeiter* specifies the TreeIter object of the item to be moved, with the *position* value indicating the position of the item to be moved before or after.

A TreeIter can be checked to ensure it is valid with the method::

  liststore.get_iter_is_valid(treeiter)

If the method returns ``False``, the passed TreeIter is not valid in the ListStore.

=======
Example
=======
Below is an example of a ListStore:

.. literalinclude:: _examples/liststore.py

Download: :download:`ListStore <_examples/liststore.py>`

.. note::

  The above example makes use of :doc:`treeview` and :doc:`cellrenderertext` widgets, which will be covered in later chapters.
