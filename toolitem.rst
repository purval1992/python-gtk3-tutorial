ToolItem
========
A ToolItem is the base of all other Toolbar-related widgets. It provides a blank item, from which standard widgets (i.e. :doc:`entry`) can be added to the Toolbar.

The methods contained within a ToolItem can also be used for all other ToolItem-related widgets.

===========
Constructor
===========
The ToolItem can be constructed using::
  
  toolitem = Gtk.ToolItem()

=======
Methods
=======
Widgets can be added and removed from ToolItem via::

  toolitem.add(widget)
  toolitem.remove(widget)

To expand a ToolItem to fill all empty space on the Toolbar use::

  toolitem.set_expand(expand)

In some cases it may be necessary to show or hide the widget based on the orientation of the Toolbar via::

  toolitem.set_visible_vertical(visible_vertical)
  toolitem.set_visible_horizontal(visible_horizontal)

By default, the widget will take its size based only on its own content. To ensure that it stays the same size as other widgets in the Toolbar call::

  toolitem.set_homogeneous(homogeneous)

=======
Example
=======
To view an example for this widget, see the :doc:`toolbar` example.
