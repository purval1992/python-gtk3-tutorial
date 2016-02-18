MenuToolButton
==============
A MenuToolButton provides two functions; a standard :doc:`toolbutton` which can be clicked, and a :doc:`menu` which provides more options relating to the button.

===========
Constructor
===========
The MenuToolButton is constructed with the call::

  menutoolbutton = Gtk.MenuToolButton(label, icon_widget, icon_name)

The *label* parameter defines the string of text to be displayed on the MenuToolButton. In all circumstances this should be set. The *icon_widget* allows a widget such as an :doc:`image` to be added, however can be omitted if not required. The *icon_name* allows the name of an icon to be used, which is then loaded from the current theme. This may also be omitted if not needed.

=======
Methods
=======
.. note::

  The methods listed below only apply to this widget and those that inherit from it. For more methods, see the :doc:`toolbutton` page. For more information on widget hierarchy, see :doc:`hierarchytheory`.

A Menu can be attached after constructing with::

  menutoolbutton.set_menu(menu)

The *menu* parameter supplied should be the name of a Menu object. If no Menu object is supplied, the arrow button will be set as insensitive.

The Menu object associated with the MenuToolButton can be retrieved if required with::

  menutoolbutton.get_menu()

Specific text can be set as a tooltip for the menu button via::

  menutoolbutton.set_arrow_tooltip_text(tooltip_text)
  menutoolbutton.set_arrow_tooltip_markup(tooltip_markup)

For unformatted text, it is recommended to use the ``.set_arrow_tooltip_text()`` method. Enhanced, formatted text can be provided via ``.set_arrow_tooltip_markup()``.

=======
Signals
=======
The commonly used signals for the widget are::

  "clicked" (menutoolbutton)
  "show-menu" (menutoolbutton)

Use of the ``"clicked"`` signal is made when the button portion of the MenuToolButton is clicked. The ``"show-menu"`` signal emits from the widget when the dropdown arrow is clicked, but before the actual menu is displayed, allowing for on-demand loading of menu items.

=======
Example
=======
To view an example for this widget, see the :doc:`toolbar` example.
