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

Input made on the Overlay widget can be passed through to the unlying widget with::

  overlay.set_overlay_pass_through(widget, pass_through)

The *widget* parameter should be set to the underlying widget which will receive input. The *pass_through* parameter should be set to ``True`` or ``False`` as to whether this functionality is enabled or not.

=======
Example
=======
Below is an example of a Overlay:

.. literalinclude:: _examples/overlay.py

Download: :download:`Overlay <_examples/overlay.py>`
