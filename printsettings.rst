PrintSettings
=============
The PrintSettings object stores the configuration for the print job. Example settings include use of duplex, output bin, and number of copies amongst others.

===========
Constructor
===========
Construction of the PrintSettings object is done via::

  printsettings = Gtk.PrintSettings()

=======
Methods
=======
The Printer object associated with the PrintSettings can be retrieved with::

  printsettings.get_printer()

A Printer object can also be defined::

  printsettings.set_printer(printer)

A range of print settings can be defined with::

  printsettings.set_n_copies(copies)
  printsettings.set_reverse(reverse)
  printsettings.set_collate(collate)
  printsettings.set_use_color(color)

Print quality options can be defined via the method::

  printsettings.set_quality(quality)

The *quality* value should be set to one of the following constants:

* ``Gtk.PrintQuality.LOW``
* ``Gtk.PrintQuality.NORMAL``
* ``Gtk.PrintQuality.HIGH``
* ``Gtk.PrintQuality.DRAFT``

The current quality setting can also be retrieved if required::

  printsettings.get_quality()

The paper size in use by the printer can be defined with::

  printsettings.set_paper_size(paper_size)

The *paper_size* constant should be set to an appropriate :doc:`papersize` object.

Custom paper sizes can also be entered via::

  printsettings.set_paper_width(width, unit)
  printsettings.set_paper_height(height, unit)

The *width* and *height* arguments should be set to a decimal value. The *unit* determines the measurement and should be set to a constant of:

* ``Gtk.Unit.NONE``
* ``Gtk.Unit.POINTS``
* ``Gtk.Unit.INCH``
* ``Gtk.Unit.MM``
