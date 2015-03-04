AccelLabel
==========
An AccelLabel is used to display an Accelerator which displays a keyboard combination which can be used to activate a described function.

===========
Constructor
===========
The AccelLabel can be constructed using the following::

  accellabel = Gtk.AccelLabel(label)

A *label* should be specified for the Label which indicates the function of the accelerator.

=======
Methods
=======
To monitor a particular widget for an accelerator use::

  accellabel.set_accel_widget(accel_widget)

The *accel_widget* value should be set to the name of a widget which is to be monitored for an accelerator. When one is applied to a child widget the AccelLabel is updated to display the accelerator combination.

=======
Example
=======
Below is an example of a AccelLabel:

.. literalinclude:: _examples/accellabel.py

Download: :download:`AppChooserButton <_examples/accellabel.py>`
