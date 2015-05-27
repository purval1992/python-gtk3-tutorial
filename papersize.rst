PaperSize
=========
The PaperSize object handles paper sizing, and is commonly used with the printing framework of GTK+.

===========
Constructor
===========
The PaperSize is constructed using::

  papersize = Gtk.PaperSize(name)

The *name* parameter specifies the size of the paper object to be created using the PWG 5101.1-2002 paper name convention. This is parsed by GTK+ to set the values for the object. Common examples include "a4", "a3", "na_letter", etc.

If the appropriate size is not available, custom values can be specified with::

  papersize = Gtk.PaperSize(name, display_name, width, height, unit)

The *name* object is the paper name to be used by this object, while *display_name* is a human-readable name. The *width* and *height* values indicate the size of the paper object created while the *unit* parameter sets the units used by the width and height. This should be set to one of:

* ``Gtk.Unit.POINTS``
* ``Gtk.Unit.INCH``
* ``Gtk.Unit.MM``

=======
Methods
=======
Setting the size of the paper is done via::

  papersize.set_size(width, height, unit)

The *width* and *height* parameters indicate the size of the paper. The *unit* should be set to one of:

* ``Gtk.Unit.POINTS``
* ``Gtk.Unit.INCH``
* ``Gtk.Unit.MM``

Retrieval of the specified width and height is done by calling::

  papersize.get_width()
  papersize.get_height()

The name and display name used by the PaperSize object can be fetched after construction with::

  papersize.get_name()
  papersize.get_display_name()

An existing PaperSize can be copied to a new object with::

  papersize.copy(size)

To check if two PaperSize objects are equal, use::

  papersize.is_equal(size1, size2)
