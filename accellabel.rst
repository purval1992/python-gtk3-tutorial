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

The associated accelerator widget is fetchable with::

  accellabel.get_accel_widget()

An accelerator can also be specified by using::

  accellabel.set_accel(key, modifier)

The *key* parameter indicates the accelerator key to use, with an integer value accepted. The *modifier* sets the key such as :kbd:`Control` or :kbd:`Alt` and should be set to ``None`` if not required, or:

* ``Gdk.ModifierType.CONTROL_MASK`` - the Control key.
* ``Gdk.ModifierType.SHIFT_MASK`` - the Shift key.
* ``Gdk.ModifierType.MOD1_MASK`` - typically the Alt key.
* ``Gdk.ModifierType.LOCK_MASK`` - a lock key such as the Caps or Num lock.
* ``Gdk.ModifierType.BUTTON1_MASK`` - mouse button 1.
* ``Gdk.ModifierType.BUTTON2_MASK`` - mouse button 2.
* ``Gdk.ModifierType.BUTTON3_MASK`` - mouse button 3.

An accelerator can also be retrieved via::

  accellabel.get_accel()

=======
Example
=======
Below is an example of a AccelLabel:

.. literalinclude:: _examples/accellabel.py

Download: :download:`AppChooserButton <_examples/accellabel.py>`
