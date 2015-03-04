SizeGroup
=========
The SizeGroup object providess a mechanism for grouping widgets, and that all widgets within the group equal the same size regardless of content.

===========
Constructor
===========
The SizeGroup can be constructed using the following::

  sizegroup = Gtk.SizeGroup()

=======
Methods
=======
Widgets are added to and removed from the SizeGroup using::

  sizegroup.add_widget(widget)
  sizegroup.remove_widget(widget)

To retrieve a list of widgets which are currently within the SizeGroup use::

  widgets = sizegroup.get_widgets()

A SizeGroup can take the size required and apply it in a variety of directions by calling::

  sizegroup.set_mode(mode)

The *mode* parameter can be set to any of the four following constants; ``Gtk.SizeGroupMode.NONE``, ``Gtk.SizeGroupMode.HORIZONTAL`` which affects the horizontal size, ``Gtk.SizeGroupMode.VERTICAL`` which affects vertical sizing and ``Gtk.SizeGroupMode.BOTH`` which applies the sizing to both horizontal and vertical directions.

To configure whether hidden widgets which are a member of the SizeGroup are taken into account call::

  sizegroup.set_ignore_hidden(ignore_hidden)

When *ignore_hidden* is set to ``True``, the size allocation for the widgets will be re-calculated to account for the hidden widget.

=======
Example
=======
Below is an example of a SizeGroup:

.. literalinclude:: _examples/sizegroup.py

Download: :download:`SizeGroup <_examples/sizegroup.py>`
