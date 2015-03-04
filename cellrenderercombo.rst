CellRendererCombo
=================
A CellRendererCombo widget provides a dropdown menu within a :doc:`treeview`. The functionality is similar to that provide by a :doc:`combobox`.

===========
Constructor
===========
The CellRendererCombo can be constructed using the following::

  cellrenderercombo = Gtk.CellRendererCombo()

==========
Properties
==========
The configuration of the CellRendererCombo is made using the property functions::

  cellrenderercombo.set_property("item", value)

The property items available for use with the CellRendererCombo are:

* ``"has-entry"`` - setting to ``True`` enables text to be entered by the user along with selecting a value from a menu.
* ``"model"`` - specifies`the data store which will be used to retrieve values from. This should be set to the name of an appropriate :doc:`liststore` or :doc:`treestore` containing the values.
* ``"text-column"`` - used to set the column from which the values are to be retrieved.

=======
Signals
=======
The common signals of the CellRendererCombo are::

  "changed" (cellrenderercombo, path, treeiter)

The ``"changed"`` signal emits when the user changes which item has been selected. The *path* value is a string which identifies the cell relative to the tree view model. The *treeiter* is the iter of the item selected relative to the combo box model. These items can be put together to return the item from the model.

=======
Example
=======
Below is an example of a CellRendererCombo:

.. literalinclude:: _examples/cellrenderercombo.py

Download: :download:`CellRendererCombo <_examples/cellrenderercombo.py>`
