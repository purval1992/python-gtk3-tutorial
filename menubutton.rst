Expander
========
The MenuButton widget displays a menu when the button is clicked.

===========
Constructor
===========
The MenuButton can be constructed using the following::

  menubutton = Gtk.MenuButton()

=======
Methods
=======
A MenuButton can have a :doc:`menu` added to it::

  menubutton.set_popup(menu)

By default, the menu appears beneath the MenuButton, however this can be configured::

  menubutton.set_direction(direction)

The *direction* parameter can be set to one of the following:

* ``Gtk.ArrowType.NONE``
* ``Gtk.ArrowType.DOWN``
* ``Gtk.ArrowType.UP``
* ``Gtk.ArrowType.LEFT``
* ``Gtk.ArrowType.RIGHT``

=======
Example
=======
Below is an example of a MenuButton:

.. literalinclude:: _examples/menubutton.py

Download: :download:`MenuButton <_examples/menubutton.py>`
