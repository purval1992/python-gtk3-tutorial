TreeStore
=========
A TreeStore is a data store object which allows data to be stored in a multi-level structure.

===========
Constructor
===========
The TreeStore can be constructed using the following::

  treestore = Gtk.TreeStore(data_types)

The *data_types* parameter can be set to a number of supported types. These includes those from Python; ``str``, ``float``, ``long``, ``int``, ``bool``, and ``object``. Alternatively, GTK provides the following; ``gchar``, ``guchar``, ``gboolean``, ``gint``, ``guint``, ``glong``, ``gulong``, ``gint64``, ``guint64``, ``gfloat``, ``gdouble``, ``gchararray``, and ``GObject``.

.. note::

  There is no preference over which data type to use, however for simplicity it is often easier to use the Python data types.

To store data in the TreeStore, the type of data being entered must match the data type specified.

=======
Methods
=======
Insertion of a row is made using the methods::

  treestore.insert(parent, [data], positon)
  treestore.append(parent, [data])
  treestore.prepend(parent, [data])

The ``.insert()`` method takes a *position* parameter which allows the row to be added to the TreeStore in a particular location. Each method takes the *parent* which can be ``None`` if the data has no parent, or it can specify the TreeIter of the parent which the data will be attached to.

To remove an item from the TreeStore use::

  treestore.remove(treeiter)

The *treeiter* value should be a TreeIter retrieved using the methods described on that page.

Emptying the TreeStore of all values can be done with the method::

  treestore.clear()

Values contained within the TreeStore can swap position with::

  treestore.swap(position_a, position_b)

The *position_a* and *position_b* arguments should be TreeIter objects relating to each of the rows which are to be swapped.

To reorder all the items in a TreeStore call::

  treestore.reorder(parent, [positions])

The *parent* parameter specifies the parent TreeIter of the items to be reordered. The *positions* list passes the new position of each child. The method only works on unsorted TreeStore objects.

An item in the TreeStore can be moved before or after another item with the methods::

  treestore.move_before(treeiter, position)
  treestore.move_after(treeiter, position)

The *treeiter* specifies the TreeIter object of the item to be moved, with the *position* value indicating the position of the item to be moved before or after.

A TreeIter can be checked to ensure it is valid with the method::

  treestore.get_iter_is_valid(treeiter)

If the method returns ``False``, the passed TreeIter is not valid in the TreeStore.

Obtaining the depth of a passed TreeIter can be found with::

  treestore.iter_depth(treeiter)

The method will return ``0`` if the TreeIter is a top level item, with the depth value returned for each item down the tree.

=======
Example
=======
Below is an example of a TreeStore:

.. literalinclude:: _examples/treestore.py

Download: :download:`TreeStore <_examples/treestore.py>`

.. note::

  The above example makes use of :doc:`treeview` and :doc:`cellrenderertext` widgets, which will be covered in later chapters.
