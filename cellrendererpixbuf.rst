CellRendererPixbuf
==================
A CellRendererPixbuf provides a way to display images and icons within a TreeView cell.

===========
Constructor
===========
The CellRendererPixbuf can be constructed using the following::

  cellrendererpixbuf = Gtk.CellRendererPixbuf()

==========
Properties
==========
The configuration of the CellRendererPixbuf is made using the property functions::

  cellrendererpixbuf.set_property("item", value)

The property items available for use with the CellRendererPixbuf are:

* ``"pixbuf"`` - the pixbuf value sets the location of the Pixbuf image format to display in the cell.

=======
Example
=======
Below is an example of an CellRendererPixbuf:

.. literalinclude:: _examples/cellrendererpixbuf.py

Download: :download:`CellRendererPixbuf <_examples/cellrendererpixbuf.py>`
