Box
===
A Box object is an invisible container which allows packing of child widgets in two modes; vertically-packed and horizontally-packed.

For more information on packing and the theory behind it using GTK+, see the :doc:`packingtheory` page.

..note ::

  The :doc:`grid` widget is recommended in many cases where a Box would have traditionally been used.

===========
Constructor
===========
The Box can be constructed using the following::

  box = Gtk.Box(orientation, spacing)

The *orientation* parameter should be set to one of the following values; ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL``. By default, the Box is constructed with the ``Gtk.Orientation.HORIZONTAL`` orientation. The *spacing* value must be an integer value which indicates the amount of pixels between each of the child widgets.

=======
Methods
=======
Items can be packed using two methods; packing at the start of the container or packing at the end. When using a vertical Box, items using ``.pack_start()`` are packed from to the top. If using a horizontal box, packing using ``.pack_start()``, child widgets are added to the left. This is done with::

  box.pack_start(child, expand, fill, padding)
  box.pack_end(child, expand, fill, padding)

The *child* parameter should be the name of the child widget that is being added to the Box. The *expand* property when set to ``True`` indicates that the child should be given extra space if the Box has room for it. When *fill* is set to ``True``, the child widget is allocated the full horizontal or vertical space. The *padding* parameter should be set to an integer value which indicates how much space is put between it and other child widgets in the Box.

Items can also be removed from the Box with::

  box.remove(child)

To reorder child widgets based on position use::

  box.reorder_child(child, position)

The *position* value should be an integer, with ``0`` indicating the first position within the container. Alternatively, negative numbers can be entered which indicates a position from the end of the container.

The orientation of the Box can be changed after construction by::

  box.set_orientation(orientation)

Again, the *orientation* value must be set to either ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL``.

Child widgets can be reordered within the Box using::

  box.reorder_child(child, position)

The *child* value should be the name of the widget which is to be moved. The *position* value should be an integer value which designates the new position of the child. ``0`` designates the first position in the box.

To ensure that all child widgets are set to an equal size regardless of their content, use::

  box.set_homogeneous(homogeneous)

By default, *homogeneous* is set to ``False`` and all child widgets are sized based on their content.

The Box spacing can be set after construction with::

  box.set_spacing(spacing)

=======
Example
=======
Below is an example of a Box:

.. literalinclude:: _examples/box.py

Download: :download:`Box <_examples/box.py>`
