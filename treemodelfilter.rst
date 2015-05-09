TreeModelFilter
===============
The TreeModelFilter objects provides a way to filter the data displayed in a :doc:`liststore` or :doc:`treestore` via a function, which returns whether the data is shown or not.

===========
Constructor
===========
The TreeModelFilter is typically constructed from an existing model::

  treemodelfilter = model.filter_new()

It can however be constructed itself, with the model being derived from the filter::

  treemodelfilter = Gtk.TreeModelFilter()

=======
Methods
=======
A function is attached to the TreeModelFilter which returns ``True`` or ``False`` depending on whether the row is to be displayed or not. The function is called for each row in the model, and when ``False`` is returned, the row is NOT displayed. The function is set via::

  treemodelfilter.set_visible_func(function, data)

The *data* specifies the data which is being displayed in the TreeModelFilter.

The TreeModelFilter can be refiltered using the method::

  treemodelfilter.refilter()

In some cases, it may be useful to use columns within the data model which indicate whether a row should be displayed. Setting the column type to a Boolean type, the column can be declared with::

  treemodelfilter.set_visible_column(column)

The *column* value should be set to the number of the column containing the visibility information. When the row is set to ``True`` it is displayed.

When retrieving the selected item from the viewing widget, it will return a TreeIter or TreePath for the filter. These need to be converted to correctly access the underlying model::

  treemodelfilter.convert_iter_to_child_iter(treeiter)
  treemodelfilter.convert_path_to_child_path(treepath)

A convenience function can be used to return the model being filtered::

  treemodefilter.get_model()

=======
Example
=======
Below is an example of a TreeModelFilter:

.. literalinclude:: _examples/treemodelfilter.py

Download: :download:`TreeModelFilter <_examples/treemodelfilter.py>`
