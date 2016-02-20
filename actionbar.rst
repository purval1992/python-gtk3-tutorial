ActionBar
=========
The ActionBar widget provides a full width bar for widgets such as :doc:`button` and :doc:`label` widgets. It is usually placed below the application content and is commonly used in place of a :doc:`statusbar`.

===========
Constructor
===========
The ActionBar is constructed using::

  actionbar = Gtk.ActionBar()

=======
Methods
=======
Items can be packed into the container at the start (left) or end (right)::

  actionbar.pack_start(child)
  actionbar.pack_end(child)

If required, items can also be placed in the center::

  actionbar.set_center_widget(child)

The center widget can also be retrieved via::

  actionbar.get_center_widget()

==========
Properties
==========
The property items available for use with the ActionBar are:

* ``"pack-type"`` - can be set to either ``Gtk.PackType.START`` or ``Gtk.Pack_type.END`` for left or right placement of child widgets.
* ``"position"`` - specifies the index of the child in the ActionBar.

=======
Example
=======
Below is an example of an ActionBar:

.. literalinclude:: _examples/actionbar.py

Download: :download:`ActionBar <_examples/actionbar.py>`
