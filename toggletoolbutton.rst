ToggleToolButton
================
A ToggleToolButton is similar to a :doc:`togglebutton` in functionality however it should be applied to a :doc:`toolbar`.

===========
Constructor
===========
The ToggleToolButton can be constructed using the following::

  toggletoolbutton = Gtk.ToggleToolButton(label)

=======
Methods
=======
.. note::

  The methods listed below only apply to this widget and those that inherit from it. For more methods, see the :doc:`toolbutton` page. For more information on widget hierarchy, see :doc:`hierarchytheory`.

To flip the active or inactive state, use the method::

  toggletoolbutton.set_active(active)

When *active* is set to ``True``, the ToggleToolButton will appear depressed.

To retrieve the current state of the ToggleToolButton call::

  toggletoolbutton.get_active()

=======
Signals
=======
The commonly used signals of an ToggleToolButton are::

  "toggled" (toggletoolbutton)

When the user clicks on the ToggleToolButton and the state is changed to active or inactive, the ``"toggled"`` signal is emitted.

=======
Example
=======
To view an example for this widget, see the :doc:`toolbar` example.
