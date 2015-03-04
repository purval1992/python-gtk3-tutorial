IconView
========
The purpose of the IconView is to displays images in thumbnail format, arranged into a grid format.

===========
Constructor
===========
The IconView can be constructed using the following::

  iconview = Gtk.IconView(model)

The *model* value is optional, however allows a data store to be attached to the IconView at construction.

=======
Methods
=======
To set the model after constructing the widget call::

  iconview.set_model(model)

The *model* parameter should be set to a :doc:`liststore` which is used to hold the associated images, text or tooltip information.

To set the image, text and tooltip columns from the IconView the following calls can be made::

  iconview.set_pixbuf_column(column)
  iconview.set_text_column(column)
  iconview.set_tooltip_column(column)

The *column* parameter indicates the column number within the ListStore, with ``0`` identifying the first column.

To set the width of the image within the IconView use::

  iconview.set_item_width(item_width)

The *item_width* should be specified as an integer with the value specifying the number of pixels in width each image is.

To allow items within the IconView to be reordered use::

  iconview.set_reorderable(reorderable)

When the *reorderable* parameter is set to ``True``, images can be dragged-and-dropped into a new position.

By default, all text names are shown below the image, however this can be configured using::

  iconview.set_item_orientation(orientation)

The *orientation* parameter should be set to one of the following; ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL``. When ``Gtk.Orientation.HORIZONTAL`` is used, text is displayed to the right of the image.

The default setting of the IconView prevents more than one item being selected at any one time, however this can be changed with::

  iconview.set_selection_mode(selection_mode)

The *selection_mode* argument can be set to either ``Gtk.SelectionMode.NONE`` which prevents any selection, ``Gtk.SelectionMode.SINGLE`` that allows only a single item to be selected, ``Gtk.SelectionMode.BROWSE`` allows one selection however at default can allow multiple if required, or ``Gtk.SelectionMode.MULTIPLE`` which allows the user to hold down the :kbd:`Control` key to highlight multiple items.

=======
Signals
=======
The commonly used signals of an IconView are::

  "item-activated" (iconview, path)
  "selection-changed" (iconview)
  "select-all" (iconview)
  "unselect-all" (iconview)
  "move-cursor" (iconview, step, count)

An ``"item-activated"`` signal emits from the IconView widget when the user double-clicks an item or when Return/Enter is pressed. The IconView parameter is passed along with a TreePath identifying the location of the item. The ``"selection-changed"`` is emitted when the highlighted item is changed. An event of ``"select-all"`` or ``"unselect-all"`` occurs when all or none of the items are selected. All three signals emit only the iconview on which the event occurred. Finally, the ``"move-cursor"`` signal occurs when the user initiates a cursor movement. It passes the iconview on which the event run, the step which specifies the type of movement and the count which identifies the number of units the move made.

=======
Example
=======
Below is an exmaple of a IconView:

.. literalinclude:: _examples/iconview.py

Download: :download:`IconView <_examples/iconview.py>`
