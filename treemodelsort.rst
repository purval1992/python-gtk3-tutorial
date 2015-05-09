TreeModelSort
=============
A TreeModelSort object allows the data within a :doc:`liststore` or :doc:`treestore` to be sorted in a variety of different ways. It can be seen as a layer which sits between the model and the viewing widget, such as a :doc:`treeview` or :doc:`combobox` as it sorts the data passed.

===========
Constructor
===========
Constructing the TreeModelSort object is done with::

  treemodelsort = Gtk.TreeModelSort(model)

The *model* parameter is the name of the TreeStore or ListStore which is going to be sorted.

=======
Methods
=======
If required, the model attached to the TreeModelSort can be retrieved via::

  treemodelsort.get_model()

Basic sorting is achievable by using::

  treemodelsort.set_sort_column_id(column, sort_type)

The *column* value is the number of the column to be sorted, with the first column being represented by ``0``. The *sort_type* paraemter is a Gtk constant which indicates the direction of the sorting, and should be set to either ``Gtk.SortType.ASCENDING`` for A-Z, or ``Gtk.SortType.DESCENDING`` for Z-A.

Custom sorting, used typically for the ability of sorting by multiple columns is also available at the cost of being more complex. It requires a function to be defined where the sorting comparison takes place, with the return values from the function indicating to GTK+ whether the item will go above or below the previous one. The custom sorting method is::

  treemodelsort.set_sort_func(column, function, data)

The *column* value specified is the column where the sort function to be applied. The *function* parameter is the name of the function where the sorting comparison will be done. Specifying the *data* parameter can also be done which provides data to be sorted, or alternatively can be left out entirely.

As the TreeModelSort sits between the viewing widget and data model, the correct TreeIter or TreePath for the underlying model is not returned. These need to be converted using::

  treemodelsort.convert_iter_to_child_iter(treeiter)
  treemodelsort.convert_path_to_child_path(treepath)

Both functions return the TreeIter or TreePath for the unsorted model.

=======
Example
=======
Below is an example of a TreeModelSort:

.. literalinclude:: _examples/treemodelsort.py

Download: :download:`TreeModelSort <_examples/treemodelsort.py>`
