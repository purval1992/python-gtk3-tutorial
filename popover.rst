Popover
=======
A Popover widget provides a bubble-like context window which is attached to a widget. It is also commonly used for menus in place of a :doc:`menu`.

===========
Constructor
===========
The Popover is constructed by calling::

  popover = Gtk.Popover()

Alternatively, the Popover can be attached to the widget which will launch it by::

  popover = Gtk.Popover(relative_to)

When the Popover is to be used as a replacement for a Menu widget, it can be built with a :doc:`menumodel` listing the menu items::

  popover = Gtk.Popover.new_from_model(model)

=======
Methods
=======
Items are added to the Popover with::

  popover.add(child)

The *child* parameter should be set to name of the widget to be added to the Popover. Typically this will be a container such as a :doc:`box` or :doc:`grid` from which further widgets can be added.

The Popover is attached to the widget::

  popover.set_relative_to(relative_to)

The *relative_to* parameter should be set to the widget the Popover is to be attached to.

The position of the Popover menu can be set using the method::

  popover.set_position(position)

The *position* value can be set to one of the following:

* ``Gtk.PositionType.TOP``
* ``Gtk.PositionType.BOTTOM``
* ``Gtk.PositionType.LEFT``
* ``Gtk.PositionType.RIGHT``

In some cases, it may be required to ensure that when the Popover is displayed, it is the focus of the input until closed. This is set with::

  popover.set_modal(modal)

When *modal* is set to ``True``, the Popover will have the keyboard focus.

=======
Example
=======
Below is an example of a Popover:

.. literalinclude:: _examples/popover.py

Download: :download:`Popover <_examples/popover.py>`
