Tooltip
=======
A Tooltip is a piece of text which is displayed when hovering over a widget to describe what the function of the widget is.

There are two types of tooltip; basic and advanced. Basic provides only textual information and in most cases will be used. Advanced allows displaying of styled or formatted text and icons.

===========
Constructor
===========
To apply a basic Tooltip to any widget, use the method::

  widget.set_tooltip_text(text)

Alternatively, an advanced Tooltip can be created with::

  tooltip = Gtk.Tooltip()

=======
Methods
=======
.. note::

  The following methods only apply to the advanced Tooltip.

To set the text on the Tooltip use::

  tooltip.set_text(text)

In some cases it may be useful to format the text with markup by calling::

  tooltip.set_markup(markup)

The *markup* parameter should be set to a string, for example "<b>Text in a Tooltip</b>" would be displayed in bold.

Alternatively icons can also be used with::

  tooltip.set_icon(pixbuf)

Specifying a *pixbuf* allows any image in the Pixbuf format to be rendered in the Tooltip.

If widgets are required to be packed into the Tooltip, then use::

  tooltip.set_custom(custom_widget)

This allows packing of child widgets alongside the default Image and Label which are created at construction time.

=======
Signals
=======
The commonly used signals of a Tooltip are::

  "query-tooltip" (widget, x, y, keyboard_mode, tooltip)

The ``"query-tooltip"`` parameter links to a function from which the Tooltip is called. There are several parameters passed to the function. The *widget* value identifies the widget upon which the Tooltip was called. An *x* and *y* are passed to identify the location of the cursor. The *keyboard_mode* value returns ``True`` or ``False`` depending on whether the Tooltip was called by the keyboard. Finally, the *tooltip* value indicates the Tooltip to be passed.

========
Examples
========
Below is an example of a basic Tooltip:

.. literalinclude:: _examples/tooltipbasic.py

Download: :download:`Tooltip Basic <_examples/tooltipbasic.py>`

Alternatively, the advanced Tooltip is displayed below:

.. literalinclude:: _examples/tooltipadvanced.py

Download: :download:`Tooltip Advanced <_examples/tooltipadvanced.py>`
