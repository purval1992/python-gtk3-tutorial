
Overlay
=======
An Overlay widget provides a container which a child widget can be packed into. The widget is displayed over a larger, background widget to provide a floating object.

===========
Constructor
===========
The Overlay can be constructed using the following::

  overlay = Gtk.Overlay()

=======
Methods
=======
The background or larger item can be added to the overlay with the method::

  overlay.add(widget)

Overlay widgets can be then added using::

  overlay.add_overlay(widget)

=======
Example
=======
Below is an example of a Overlay:

.. literalinclude:: _examples/overlay.py

Download: :download:`Overlay <_examples/overlay.py>`
