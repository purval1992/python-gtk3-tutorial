Label
=====
A Label widget can be used to display anything from small to large amounts of text. The text can be formatted in a variety of different ways such as bold, italic or underline.

===========
Constructor
===========
The Label can be constructed using the following::

  label = Gtk.Label(label)

The *label* parameter should be set to display the text within the Label widget.

=======
Methods
=======
To set the text of the Label after the construction of the Label, use either::

  label.set_text(label)
  label.set_label(label)

The *label* parameter should be a string. Any other values such as integers or floats should be converted before attempting to display on the Label. Text can also be set within the Label using '\n' and '\t' formatting characters which provide new lines and tab spacing respecitively.

To retrieve the text set on the Label call::

  label.get_text()

If the Label should use markup tags rather than just displaying them as text, this can be enabled with::

  label.set_use_markup(use_markup)

The markup string, as opposed to plain text should be specified within the Label by calling::

  label.set_markup(markup)

Markup allows the text in the Label to be customised, providing markup values similar to those used in HTML. Some examples include:

* <b>Bold</b>
* <i>Italics</i>
* <u>Underline</u>
* <a href="http://www.programmica.com/">Link</a>

By default, text within the Label can not be selected by the user. This can be changed with::

  label.set_selectable(selectable)

When *selectable* is set to ``True``, the user will be able to highlight the text within the Label.

When using multi-line text, the justification can be manipulated using::

  label.set_justify(justify)

The default setting is ``Gtk.Justification.LEFT``, however ``Gtk.Justification.RIGHT``, ``Gtk.Justification.CENTER`` and ``Gtk.Justification.FILL`` can also be used.

If the Label widget is to wrap lines, it may be useful to set how many lines the Label wraps to::

  label.set_lines(lines)

The *lines* value takes an integer value as the number of lines, or ``-1`` if the number of lines is not to be set.

Single line mode can also be enforced on the Label with the call::

  label.set_single_line_mode(mode)

When *mode* is set to ``True``, the text will not be split across multiple lines.

Text can be wrapped in the label if required with::

  label.set_line_wrap(wrap)

The *wrap* setting in ``.set_line_wrap()`` when set to ``True`` enforces line wrapping if the line is too long.

The text within the label can be aligned both horizontally and/or vertically with::

  label.set_xalign(xalign)
  label.set_yalign(yalign)

The *xalign* and *yalign* properties should be a value between ``0.0`` and ``1.0``, with ``0.0`` indicating left or top and ``1.0`` indicating right or bottom.

The alignment can also be retrieved via::

  label.get_xalign()
  label.get_yalign()

By default, the label alignment values are 0.5 (centered) for both horizontal and vertical planes.

Text in a label can be angled, to orient it in a different direction, with the value supplied indicating an angle of orientation::

  label.set_angle(angle)

The *angle* parameter must be a number between ``0`` and ``360``.

Mnemonic keys provide access to widgets via a keyboard shortcut, with an underscore before the key to be used. This is tied to the widget using the method::

  label.set_mnemonic_widget(widget)

The *widget* is another widget in the application associated with the label. Typically this is usually an :doc:`entry` or :doc:`spinbutton`.

Label widgets typically expand to fit the content, however in some cases it may be suitable to set a target width and maximum width in characters with::

  label.set_width_chars(width)
  label.set_max_width_chars(max_width)

As a Label can contain links, it can be configured to remember whether a link has been accessed. This is displayed similar to how a browser does, with the link changing colour::

  label.set_track_visited_links(track_links)

When *track_links* is set to ``True``, the tracking will be enabled for that Label widget.

A URI can be obtained from the Label by calling::

  label.get_current_uri()

The URI returned is often used in the ``"active-link"`` signal or when querying for a :doc:`tooltip`.

=======
Signals
=======
The commonly used signals of a Label are::

  "activate-link" (label, uri)

The *uri* parameter of the signal passes the link when the user clicks on the label.

=======
Example
=======
Below is an example of a Label:

.. literalinclude:: _examples/label.py

Download: :download:`Label <_examples/label.py>`
