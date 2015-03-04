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
  
To store data in the ListStore, the type of data being entered must match the data type specified.

=======
Methods
=======
To remove an item from the TreeStore use::

  treestore.remove(treeiter)

The *treeiter* value should be a TreeIter retrieved using the methods described on that page.

Emptying the TreeStore of all values can be done with the method::

  treestore.clear()

Values contained within the TreeStore can swap position with::

  treestore.swap(position_a, position_b)

The *position_a* and *position_b* arguments should be TreeIter objects relating to each of the rows which are to be swapped.

=======
Example
=======
Below is an example of a TreeStore:

.. literalinclude:: _examples/treestore.py

Download: :download:`TreeStore <_examples/treestore.py>`

.. note::

  The above example makes use of :doc:`treeview` and :doc:`cellrenderertext` widgets, which will be covered in later chapters.
