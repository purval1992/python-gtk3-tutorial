ComboBoxText
============
A ComboBoxText provides a simple variant of :doc:`combobox` which is suited to text-only values.

===========
Constructor
===========
The ComboBoxText can be constructed using the following::

  comboboxtext = Gtk.ComboBoxText()

Alternatively, if you wish to allow the user to enter text as well as selecting from the pre-defined list, use::

  comboboxtext = Gtk.ComboBoxText.new_with_entry()

=======
Methods
=======
Items can be added to the dropdown with the following methods::

  comboboxtext.insert(position, id, text)
  comboboxtext.append(id, text)
  comboboxtext.prepend(id, text)

All the items can be removed from the dropdown menu::

  comboboxtext.remove_all()

Alternatively, single items can be deleted::

  comboboxtext.remove(position)

The *position* parameter is the location where the item is located within the dropdown, with ``0`` indicating the first item.

To retrieve the text which has been selected call::

  text = comboboxtext.get_active_text()

Setting a default selected item can be achieved with::

  comboboxtext.set_active(position)

The *position* value must be an integer number representing the location of the item in the dropdown menu.

=======
Example
=======
Below is an example of a ComboBoxText:

.. literalinclude:: _examples/comboboxtext.py

Download: :download:`ComboBoxText <_examples/comboboxtext.py>`
