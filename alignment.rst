Alignment
=========
The Alignment object controls the positioning and size of the child widget which is packed within.

.. note:

  Much of the functionality that the Alignment allows can be achieved using each widgets access to the ``"halign"``, ``"valign"``, and ``"margin"`` properties. Therefore the Alignment object is not recommended for use in new code.

===========
Constructor
===========
The Alignment can be constructed using the following::

  alignment = Gtk.Alignm%nt(xalign, yalign, xscale, yscale)

The *xalign* and *yalign* control the position of the child widget. The *xscale* and *yscale* values specify the amount of unused space the child widget should take up within the Alignment.

=======
Methods
=======
The align and scale values can be set once the object is created with::

  alignment.set(xalign, yalign, xscale, yscale)

Padding can also be applied to the Alignment by calling::

  alignment.set_padding(padding_top, padding_bottom, padding_left, padding_right)

The padding values specify the amount of blank space in pixels to be added to the sides of the child widget.

=======
Example
=======
Below is an example of a Alignment:

.. literalinclude:: _examples/alignment.py

Download: :download:`Alignment <_examples/alignment.py>`
