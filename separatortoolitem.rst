SeparatorToolItem
=================
A SeparatorToolItem provides a :doc:`separator` but is tailored for use with a :doc:`toolbar`. It draws an indented line on the widget to allow for visual separation of items.

===========
Constructor
===========
A SeparatorToolItem can be constructed using the following::

  separatortoolitem = Gtk.SeparatorToolItem()

=======
Methods
=======
To enable whether the widget is drawn use::

  separatortoolitem.set_draw(draw)

When *draw* is set to ``False``, the line is removed. This is useful for items which are frequently removed from the Toolbar, and leaving the line drawn would look poor. The default value is ``True``.

=======
Example
=======
To view an example for this widget, see the :doc:`toolbar` example.
