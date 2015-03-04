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

  text = label.get_text()

If the Label should use markup tags rather than just displaying them as text, this can be enabled with::

  label.set_use_markup(use_markup)

The markup string, as opposed to plain text should be specified within the Label by calling::

  label.set_markup(markup)

Markup allows the text in the Label to be customised. Some examples include:

* <b>Bold</b>
* <i>Italics</i>
* <u>Underline</u>
* <a href="http://learngtk.org/">Link</a>

By default, text within the Label can not be selected by the user. This can be changed with::

  label.set_selectable(selectable)

When *selectable* is set to ``True``, the user will be able to highlight the text within the Label.

When using multi-line text, the justification can be manipulated using::

  label.set_justify(justify)

The default setting is ``Gtk.Justification.LEFT``, however ``Gtk.Justification.RIGHT``, ``Gtk.Justification.CENTER`` and ``Gtk.Justification.FILL`` can also be used.

If the Label widget is to wrap lines, it may be useful to set how many lines the Label wraps to::

  label.set_lines(lines)

The *lines* value takes an integer value as the number of lines, or ``-1`` if the number of lines is not to be set.

Text can be wrapped in the label if required with::

  label.set_line_wrap(wrap)

The *wrap* setting in ``.set_line_wrap()`` when set to ``True`` enforces line wrapping if the line is too long.

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
