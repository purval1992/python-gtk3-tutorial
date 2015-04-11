TreeModelFilter
===============
The TreeModelFilter objects provides a way to filter the data displayed in a :doc:`liststore` or :doc:`treestore` via a function, which returns whether the data is shown or not.

===========
Constructor
===========
The TreeModelFilter is constructed from the existing model::

  treemodelfilter = model.filter_new()

=======
Methods
=======
A function is attached to the TreeModelFilter which returns ``True`` or ``False`` depending on whether the row is to be displayed or not. The function is called for each row in the model, and when ``False`` is returned, the row is NOT displayed. The function is set via::

  treemodelfilter.set_visible_func(function, data)

The *data* specifies the data which is being displayed in the TreeModelFilter.

The TreeModelFilter can be refiltered using the method::

  treemodelfilter.refilter()

A convenience function can be used to return the model being filtered::

  model = treemodefilter.get_model()
