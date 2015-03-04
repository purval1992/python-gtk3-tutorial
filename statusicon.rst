StatusIcon
==========
A StatusIcon provides quick access to an application by placing an item (usually an icon) in the Notification Area of the desktop (known as the System Tray in Windows).

When a user clicks on the StatusIcon, in most cases a :doc:`menu` will be displayed providing a number of options.

.. note::

  A StatusIcon widget should only be used when it is required for your application to notify the user of an event.

===========
Constructor
===========
The StatusIcon can be constructed using::

  statusicon = Gtk.StatusIcon()

=======
Methods
=======
To set an icon on the StatusIcon, the following methods can be used::

  statusicon.set_from_pixbuf(pixbuf)
  statusicon.set_from_file(file)

Using the ``.set_from_pixbuf()`` allows a Pixbuf to be used as the icon. Finally, ``.set_from_file()`` can be used to load an image directly from disk.

Another useful function after construction is to set the StatusIcon title::

  statusicon.set_title(title)

The *title* parameter should be a string which increases the accessibility of the widget.

The name of the StatusIcon can also be set to provide sorting functionality::

  statusicon.set_name(name)

Setting a :doc:`tooltip` string or markup on the StatusIcon is recommended by using::

  statusicon.set_tooltip_text(tooltip_text)
  statusicon.set_tooltip_markup(tooltip_markup)

In most cases the ``.set_tooltip_text()`` method would be used to provide basic text, with ``.set_tooltip_markup()`` providing more advanced formatting options.

The Tooltip functionality will also need to be activated with::

  statusicon.set_has_tooltip(has_tooltip)

When *has_tooltip* is set to ``True``, the Tooltip is displayed when the user hovers over the StatusIcon with the mouse cursor.

The StatusIcon can be made visible or invisible by::

  statusicon.set_visible(visible)

=======
Signals
=======
The commonly used signals of a StatusIcon are::

  "activate" (statusicon)
  "button-press-event" (statusicon, event)
  "button-release-event" (statusicon, event)
  "popup-menu" (statusicon, button, activate_time)

=======
Example
=======
Below is an example of a StatusIcon:

.. literalinclude:: _examples/statusicon.py

Download: :download:`StatusIcon <_examples/statusicon.py>`
