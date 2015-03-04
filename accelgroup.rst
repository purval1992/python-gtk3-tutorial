AccelGroup
==========
An AccelGroup represents a group of accelerators which provide access to functions via the keyboard.

===========
Constructor
===========
The AccelGroup can be constructed using::

  accelgroup = Gtk.AccelGroup()

=======
Methods
=======
To allow or prevent changes to the Accelerator's within the AccelGroup use::

  accelgroup.lock()
  accelgroup.unlock()

The AccelGroup can also be checked to see whether it is locked using::

  is_locked = accelgroup.get_is_locked()

If ``True`` is returned to the *is_locked* variable, no accelerators may be added to the AccelGroup.

=======
Example
=======
For an example of an AccelGroup, see the :doc:`accellabel` page.
