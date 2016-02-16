Adjustment
==========
An Adjustment is an object which stores values relating to minimum, maximum and current values. It is invisible to the user and is used as a backend to other widgets such as the SpinButton or Scale.

This object is used in conjunction with a :doc:`spinbutton`, :doc:`scale`, :doc:`scalebutton`, or :doc:`scrollbar`.

===========
Constructor
===========
The Adjustment can be constructed using the following::

  adjustment = Gtk.Adjustment(value, lower, upper, step_increment, page_increment, page_size)

The *value* is the initial number which the Adjustment starts with. The *lower* and *upper* values are the limits which the Adjustment allows. A *step_increment* is the standard number which the value is adjusted by whereas the *page_increment* value is the major number to adjust by. The *page_size* is only used by some widgets and determines the viewable area. In most cases, this will be set to ``0`` as it is not required.

=======
Methods
=======
To set the value of the Adjustment::

  adjustment.set_value(value)

Retrieval of the value from the Adjustment is done with::

  adjustment.get_value()

There are a range of functions which can be used to retrieve the configuration values from the Adjustment::

  adjustment.get_lower()
  adjustment.get_upper()
  adjustment.get_step_increment()
  adjustment.get_page_increment()
  adjustment.get_page_size()

The configuration values can also be set after construction of the object with::

  adjustment.set_lower(lower)
  adjustment.set_upper(upper)
  adjustment.set_step_increment(step_increment)
  adjustment.set_page_increment(page_increment)
  adjustment.set_page_size(page_size)

Adjustment values can also be set using a single method similar to the constructor with the call::

  adjustment.configure(value, lower, upper, step_increment, page_increment, page_size)

The ``.configure()`` method will ensure that the ``"changed"`` signal is emitted once, rather than multiple times as is caused by the setting methods above.

=======
Signals
=======
The commonly used signals of an Adjustment are::

  "changed" (adjustment)
  "value-changed" (adjustment)

The ``"changed"`` signal emits from the Adjustment when any of the values are changed. Alternatively, the ``"value-changed"`` signal is emitted when just the value of the Adjustment has been modified. In both cases, the signals pass the Adjustment parameter.

=======
Example
=======
An example of an Adjustment in use can be seen with other widgets such as SpinButton, Scale, ScaleButton, or Scrollbar.
