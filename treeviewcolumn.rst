TreeViewColumn
==============
A TreeViewColumn can be packed into a :doc:`treeview`. It can display a header to describe the content of the column, from which items can be placed within to display the content.

===========
Constructor
===========
The TreeViewColumn can be constructed using the following::

  treeviewcolumn = Gtk.TreeViewColumn(title)

The *title* property is a textual string which is attached to the top of the TreeView and describes the content.

=======
Methods
=======
The column title can also be specified after construction by::

  treeviewcolumn.set_title(title)

Setting the *title* argument is always useful, however the text will only be displayed in the TreeView permits it.

Items can be packed into the column via two methods::

  treeviewcolumn.pack_start(cellrenderer, expand)
  treeviewcolumn.pack_end(cellrenderer, expand)

The *cellrenderer* property should be the name of the CellRenderer which is to be added to the column. The *expand* property can be set to ``True`` which expands the column to fill all available space, or ``False`` which shrinks it to fit the content only.

All the items from a column can be removed using::

  treeviewcolumn.clear()

When multiple CellRenderer widgets are packed into a column, they have no spacing between. This can be modified with::

  treeviewcolumn.set_spacing(spacing)

Configuring whether a column is visible can be set with::

  treeviewcolumn.set_visible(visible)

When *visible* is ``False``, the column is removed from view however still retains any settings specified.

By default, columns can not be resized. Changing this allows the user to set a custom width::

  treeviewcolumn.set_resizable(resizable)

The sizing of the column can also be customised in a number of ways depending on the change in the content by using the method::

  treeviewcolumn.set_sizing(sizing)

The *sizing* argument can be set to ``Gtk.TreeViewColumnSizing.GROW_ONLY`` sets the column to never shrink regardless of the content, ``Gtk.TreeViewColumnSizing.AUTOSIZE`` adjusts the column to be an optimal size and is updated everytime the model changes, and ``Gtk.TreeViewColumnSizing.FIXED`` which sets columns to be a fixed pixel width.

Minimum and maximum column widths can be specified by calling::

  treeviewcolumn.set_min_width(min_width)
  treeviewcolumn.set_max_width(max_width)

Columns within the TreeView can be moved by specifying on each::

  treeviewcolumn.set_reorderable(reorderable)
