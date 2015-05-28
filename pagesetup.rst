PageSetup
=========
The PageSetup object stores the page size, orientation and margins. These are often retrieved from the page setup dialog which is then passed on to the PrintOperation for printing.

.. note::

  The information relating to margins pertains to the printer margins, which the printer is not able to print within. They do not refer to margins such as those found in a word processor.

=======
Methods
=======
The orientation of a page can be adjusted via::

  pagesetup.set_orientation(orientation)

The *orientation* should be set to one of the PageOrientation constants:

* ``Gtk.PageOrientation.PORTRAIT``
* ``Gtk.PageOrientation.LANDSCAPE``
* ``Gtk.PageOrientation.REVERSE_PORTRAIT``
* ``Gtk.PageOrientation.REVERSE_LANDSCAPE``

Alternatively, the page orientation can be retrieved with::

  pagesetup.get_orientation()

The paper size is settable via a :doc:`papersize` object using::

  pagesetup.set_paper_size(papersize)

Retrieval of the

The margin values can be set on the page with::

  pagesetup.set_top_margin(margin, unit)
  pagesetup.set_bottom_margin(margin, unit)
  pagesetup.set_left_margin(margin, unit)
  pagesetup.set_right_margin(margin, unit)

The *margin* value of each method should be set to the number of pixels reserved for the margin. A *unit* value should also be specified from:

* ``Gtk.Units.POINTS``
* ``Gtk.Units.INCH``
* ``Gtk.Units.MM``

The margin sizes can also be fetched via::

  pagesetup.get_top_margin(unit)
  pagesetup.get_bottom_margin(unit)
  pagesetup.get_left_margin(unit)
  pagesetup.get_right_margin(unit)

As with setting the margin size, a *unit* should also be specified when getting the sizes.

The width and height of the paper can be retrieved via::

  pagesetup.get_paper_width(unit)
  pagesetup.get_paper_height(unit)

The page width and height can also be retrieved using the methods::

  pagesetup.get_page_width(unit)
  pagesetup.get_page_height(unit)
