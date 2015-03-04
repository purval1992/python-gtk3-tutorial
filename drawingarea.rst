DrawingArea
===========
A DrawingArea is used to create custom interface elements which can be displayed and interacted with by the user. It provides a blank canvas which can be drawn on.

===========
Constructor
===========
The DrawingArea can be constructed using the following::

  drawingarea = Gtk.DrawingArea()

=======
Methods
=======
The size of the DrawingArea can be set with::

  drawingarea.set_size_request(width, height)

A *width* and *height* value can be specified to indicate the number of pixels in size the widget should take.
