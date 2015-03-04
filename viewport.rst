Viewport
========
A Viewport adds the ability to scroll widgets which do not natively support scrolling (e.g. Grid, Box).

===========
Constructor
===========
The Viewport can be constructed using the following::

  viewport = Gtk.Viewport(hadjustment, vadjustment)

The *hadjustment* and *vadjustment* parameters are optional and can be specified :doc:`adjustment` objects.

=======
Methods
=======
Rather than create Adjustment objects manually, these can be retrieved from the Viewport with::

  hadjustment = viewport.get_hadjustment()
  vadjustment = viewport.get_vadjustment()

If you do use manually created Adjustment objects, these can be attached after construction by calling::

  viewport.set_hadjustment(hadjustment)
  viewport.set_vadjustment(vadjustment)

=======
Example
=======
Viewport example currently unavailable.
