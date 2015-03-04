ComboBox
========
A ComboBox provides a drop-down menu of items which can be selected by the user. It is commonly used when there are more than five items to choose from.

Another function is to provide a way to enter values via the keyboard if the option is required.

===========
Constructor
===========
The ComboBox can be constructed using the following::

  combobox = Gtk.ComboBox(model)

A *model* should be assigned to the ComboBox to provide the list of options which are selectable.

=======
Methods
=======
To set the model on the ComboBox after constructing the widget use::

  combobox.set_model(model)

The model is also retrievable::

  model = combobox.get_model()

In order to return the currently selected item from the ComboBox call::

  active = combobox.get_active()

The *active* value will return the number identifying the item. The first item will return ``0`` as the index number. If no item is selected, ``-1`` will be returned.

Alternatively, to set the item on the ComboBox use::

  combobox.set_active(active)

If the ComboBox contains a large number of items, it is recommended to display the menu spanning multiple columns. This can be set with::

  combobox.set_wrap_width(width)

The *width* value should be set to the number of columns required.

To check whether a ComboBox has an associated text entry::

  has_entry = combobox.get_has_entry()

=======
Signals
=======
The commonly used signals of a ComboBox are::

  "changed" (combobox)
  "popup" (combobox)
  "popdown" (combobox)

A ``"changed"`` event occurs when the selected item within the ComboBox is changed. The signals ``"popup"`` and ``"popdown"`` are emitted when the menu object of the Combobox is shown or hidden by the user.

=======
Example
=======
Below is an example of a ComboBox:

.. literalinclude:: _examples/combobox.py

Download: :download:`ComboBox <_examples/combobox.py>`
