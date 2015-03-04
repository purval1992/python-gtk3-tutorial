Scrollbar
=========
A Scrollbar provides the ability to navigate through content that is larger than the container it is positioned within.

In most cases a :doc:`scrolledwindow` would be preferably as it automatically determines whether scrollbars are required, and the size they should be set to.

===========
Constructor
===========
The Scrollbar can be constructed using the following::

  scrollbar = Gtk.Scrollbar(orientation, adjustment)

The *orientation* parameter indicates the direction of the Scrollbar and should be set to either ``Gtk.Orientation.VERTICAL`` or ``Gtk.Orientation.HORIZONTAL``. An *adjustment* can also be specified which provides the values relating to the size of the content.

=======
Example
=======
Below is an example of a Scrollbar:

.. literalinclude:: _examples/scrollbar.py

Download: :download:`Scrollbar <_examples/scrollbar.py>`
