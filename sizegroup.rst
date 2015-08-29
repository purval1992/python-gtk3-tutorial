SizeGroup
=========
The SizeGroup object providess a mechanism for grouping widgets, and that all widgets within the group equal the same size regardless of content. It is similar in some ways to the :doc:`buttonbox` widget.

===========
Constructor
===========
The SizeGroup can be constructed using the following::

  sizegroup = Gtk.SizeGroup(mode)

The *mode* constant determines how the SizeGroup displays the widgets and should be set to:

* ``Gtk.SizeGroup.NONE`` - do not size equally.
* ``Gtk.SizeGroup.HORIZONTAL`` - size equally horizontally.
* ``Gtk.SizeGroup.VERTICAL`` - size equally vertically.
* ``Gtk.SizeGroup.BOTH`` - size equally both horizontally and vertically.

=======
Methods
=======
Widgets are added to and removed from the SizeGroup using::

  sizegroup.add_widget(widget)
  sizegroup.remove_widget(widget)

To retrieve a list of widgets which are currently within the SizeGroup use::

  sizegroup.get_widgets()

The SizeGroup mode can also be set after construction with::

  sizegroup.set_mode(mode)

The *mode* parameter should be set with one of the constants defined in the construction section.

To configure whether hidden widgets which are a member of the SizeGroup are taken into account call::

  sizegroup.set_ignore_hidden(ignore_hidden)

When *ignore_hidden* is set to ``True``, the size allocation for the widgets will be re-calculated to account for the hidden widget.

=======
Example
=======
Below is an example of a SizeGroup:

.. literalinclude:: _examples/sizegroup.py

Download: :download:`SizeGroup <_examples/sizegroup.py>`
