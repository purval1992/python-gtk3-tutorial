TextView
========
A TextView widget is able to display large amounts of text. It can be used to provide both editing capabilities and viewing-only functionality.

===========
Constructor
===========
The TextView can be constructed using the following::

  textview = Gtk.TextView(textbuffer)

The *textbuffer* argument should be set to a :doc:`textbuffer` object.

=======
Methods
=======
A TextBuffer can be set on the TextView with::

  textview.set_buffer(textbuffer)

When constructing a TextView, a TextBuffer is automatically created however not directly usable. To name the TextBuffer and gain access call::

  textbuffer = textview.get_buffer()

Setting the justification type of the text within the TextView can be configured with the method::

  textview.set_justification(justification)

The *justification* value can be set to one of the following constants; ``Gtk.Justification.LEFT``, ``Gtk.Justification.RIGHT``, ``Gtk.Justification.CENTER``, or ``Gtk.Justification.FILL``.

The TextView supports a variety of wrap modes which can be configured with::

  textview.set_wrap_mode(wrap_mode)

The *wrap_mode* value can be set to one of the following constants; ``Gtk.WrapMode.NONE``, ``Gtk.WrapMode.CHAR``, ``Gtk.WrapMode.WORD`` or ``Gtk.WrapMode.WORDCHAR``.

Whether the TextView can be edited or not can be configured using::

  textview.set_editable(editable)

When *editable* is set to ``False``, the user will not be able to add or delete text within the TextView.

Another useful function is to be able to remove the cursor from view::

  textview.set_cursor_visible(visible)

When using ``.set_editable()``, it is recommended to also use ``.set_cursor_visible()`` and set it to ``False`` for usability reasons.

To enable overwrite mode when adding new characters to the TextView, enable with::

  textview.set_overwrite(overwrite)

If *overwrite* is set to ``True``, existing characters will be overwritten with new characters when typed.

Margins can be set within the TextView with::

  textview.set_left_margin(margin)
  textview.set_right_margin(margin)

The *margin* value must be set to an integer value which determines the number of pixels of space within the margin.

Indents within the TextView are defined with the methods::

  textview.set_indent(indent)

The *indent* value should be an integer which indicates how the indent appears for new paragraphs of text.

Spaicing between lines can be modified by specifying the number of pixels::

  textview.set_pixels_above_lines(pixels)
  textview.set_pixels_below_lines(pixels)

=======
Signals
=======
The commonly used signals of a TextView are::

  "move-cursor" (textview, step, count, extend_selection)
  "backspace" (textview)
  "select-all" (textview)
  "unselect-all" (textview)
  "toggle-overwrite" (textview)
  "toggle-cursor-visible" (textview)

The TextView emits the ``"move-cursor"`` signal when the text cursor is moved within the text field. This includes moving the cursor via the keyboard arrows, clicking with the mouse, and pressing :kbd:`Home` and :kbd:`End`. Using the event passes the textview on which the move occurred, the *step* value which indicates the type of move, the *count* which specifies the number of units moved and *extend_selection* which when ``True`` is specified shows that the selection was extended. A ``"backspace"`` event is caused to emit when the :kbd:`Backspace` key is used. The ``"select-all"`` and ``"unselect-all"`` events happen when the user chooses to select or unselect all of the text. When the user indicates they want to switch between insert and overwrite mode, or vice-versa, the ``"overwrite-mode"`` event emits. Finally, the ``"toggle-cursor-visible"`` signal emits from the TextView whenever the cursor is shown or hidden.

=======
Example
=======
Below is an example of a TextView:

.. literalinclude:: _examples/textview.py

Download: :download:`TextView <_examples/textview.py>`
