Separator
=========
A Separator widget is an ornamental widget which is used to split or group content within an interface. The Separator is a line drawn on the interface with a shadow to make it appear sunken.

===========
Constructor
===========
The Separator can be constructed using::

  separator = Gtk.Separator(orientation)

The *orientation* parameter should be set to either ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL`` depending on the requirements. If no orientation is set, the default orientation used is set vertically.

=======
Methods
=======
The orientation can also be set after construction with::

  seperator.set_orientation(orientation)

========
Examples
========
Below is an example of a Separator:

.. literalinclude:: _examples/separator.py

Download: :download:`Separator <_examples/separator.py>`
