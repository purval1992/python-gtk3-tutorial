Arrow
=====
Arrow widgets provide the ability to draw four different arrow types within an interface.

===========
Constructor
===========
The Arrow can be constructed using the following::

  arrow = Gtk.Arrow(arrow_type, shadow_type)

The *arrow_type* specifies the direction the arrow will point in; with the choices available being:

* ``Gtk.ArrowType.NONE``
* ``Gtk.ArrowType.UP``
* ``Gtk.ArrowType.DOWN``
* ``Gtk.ArrowType.LEFT``
* ``Gtk.ArrowType.RIGHT``

The *shadow_type* specifies the style the arrow is shown in with:
 
* ``Gtk.ShadowType.NONE``
* ``Gtk.ShadowType.IN``
* ``Gtk.ShadowType.OUT``
* ``Gtk.ShadowType.ETCHED_IN``
* ``Gtk.ShadowType.ETCHED_OUT``

=======
Methods
=======
To change the direction and style of the Arrow after creation use::

  arrow.set_type(arrow_type, shadow_type)

The *arrow_type* and *shadow_type* values should be the same as those listed at construction time.

=======
Example
=======
Below is an example of a Arrow:

.. literalinclude:: _examples/arrow.py

Download: :download:`Arrow <_examples/arrow.py>`
