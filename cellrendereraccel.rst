CellRendererAccel
=================
A CellRendererAccel is used to render a keyboard accelerator into a cell. The object is editable if required and allows a user to change the accelerator by entering a new combination.

===========
Constructor
===========
The CellRendererAccel can be constructed using the following::

  cellrendereraccel = Gtk.CellRendererAccel()

==========
Properties
==========
The configuration of the CellRendererAccel is made using the property functions::

  cellrendereraccel.set_property("item", value)

The property items available for use with the CellRendererAccel are:

* ``"editable"`` - when specified as ``True``, the accelerator value can be edited by the user.

=======
Signals
=======
The commonly used signals of a CellRendererAccel are::

  "accel-cleared" (cellrendereraccel, path_string)
  "accel-edited" (cellrendereraccel, path_string, accel_key, accel_mods, hardware_keycode)

The ``"accel-cleared"`` signals is emitted when the user presses the :kbd:`Backspace` key. On the other hand, ``"accel-edited"`` is seen when the user changes the accelerator by entering another key combination.

=======
Example
=======
Below is an example of an CellRendererAccel:

.. literalinclude:: _examples/cellrendereraccel.py

Download: :download:`CellRendererAccel <_examples/cellrendereraccel.py>`
