Scale
=====
A Scale widget is used to display the progress or amount on a sliding scale. The Scale can be adjusted to change the value as desired.

===========
Constructor
===========
A Scale can be constructed using the following::

  scale = Gtk.Scale(orientation, adjustment)

The *orientation* parameter should be set to either ``Gtk.Orientation.HORIZONTAL`` or ``Gtk.Orientation.VERTICAL``. The *adjustment* parameter should be set to specify the minimum, maximum and incremental values.

=======
Methods
=======
A Scale can be oriented in two directions; horizontal and vertical. To change the orientation after construction::

  scale.set_orientation(orientation)

The *orientation* parameter should be set with the same values as those at construction.

By default, the Scale shows the value above the slider. This can be configured using::

  scale.set_draw_value(draw_value)

When *draw_value* is set to False, the value is not displayed above the slider.

To change the position of where the value is displayed, use::

  scale.set_value_pos(position)

The *position* value should be set to one of the following; ``Gtk.PositionType.TOP``, ``Gtk.PositionType.BOTTOM``, ``Gtk.PositionType.LEFT`` or ``Gtk.PositionType.RIGHT``. By default ``Gtk.PositionType.TOP`` is used.

To adjust the number of decimal points displayed when drawing the value::

  scale.set_digits(digits)

The *digits* parameter should be an integer figure, with 1 meaning 1.0, 2 meaning 1.00, etc. Setting the number of digits also causes the value to be rounded off.

To highlight the change between the initial value and the current value, the following method can be used to indicate the difference:

  scale.set_has_origin(has_origin)

In some cases it may be useful to place a marker on the Scale to identify a particular position::

  scale.add_mark(value, position, markup)

The *value* parameter should specify the value at which the mark is to be drawn. The *position* can also be specified, with one of the values previously mentioned accepted. The *markup* parameter can be set to a string of text which is also displayed on the scale next to the mark. This parameter is optional however.

All the marks can be cleared from the Scale with::

  scale.clear_marks()

=======
Signals
=======
The common signals of a Scale widget are::

  "format-value" (value)

The ``"format value"`` signal allows the way the value is displayed.

=======
Example
=======
Below is an example of a Scale:

.. literalinclude:: _examples/scale.py

Download: :download:`Scale <_examples/scale.py>`
