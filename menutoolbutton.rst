MenuToolButton
==============
A MenuToolButton provides two functions; a standard :doc:`toolbutton` which can be clicked, and a :doc:`menu` which provides more options relating to the button.

===========
Constructor
===========

  menutoolbutton = Gtk.MenuToolButton(icon_widget, label)
  menutoolbutton = Gtk.MenuToolButton(stock_id)

=======
Methods
=======
A Menu can be attached after constructing with::

  menutoolbutton.set_menu(menu)

The *menu* parameter supplied should be the name of a Menu object. If no Menu object is supplied, the arrow button will be set as insensitive.

Specific text can be set as a tooltip for the menu button via::

  menutoolbutton.set_arrow_tooltip_text(tooltip_text)
  menutoolbutton.set_arrow_tooltip_markup(tooltip_markup)

For unformatted text, it is recommended to use the ``.set_arrow_tooltip_text()`` method. Enhanced, formatted text can be provided via ``.set_arrow_tooltip_markup()``.

=======
Signals
=======
The commonly used signals for the widget are::

  "show-menu" (menutoolbutton)

The ``"show-menu"`` signal emits from the widget when the dropdown arrow is clicked, but before the actual menu is displayed. This allows for on-demand loading of menu items.

=======
Example
=======
To view an example for this widget, see the :doc:`toolbar` example.
