RadioToolButton
===============
A RadioToolButton provides a widget similar to a :doc:`radiobutton` for use within a :doc:`toolbar`. When used with other RadioToolButton widgets, only one in the group can be active at a single time.

===========
Constructor
===========
The RadioToolButton can be constructed using the following::

  radiotoolbutton = Gtk.RadioToolButton(label, group)

The first constructor allows creation of a RadioToolButton with custom text. This is specified via the *label* paramter. The constructor also uses the *group* parameter identifiying the group the RadioToolButton belongs.

=======
Methods
=======
.. note::

  The methods listed below only apply to this widget and those that inherit from it. For more methods, see the :doc:`toolbutton` page. For more information on widget hierarchy, see :doc:`hierarchytheory`.

A group can be applied to the RadioToolButton via::

  radiotoolbutton.set_group(group)

The name of the group which the RadioToolButton is attached to can also be specified with::

  radiotoolbutton.get_group()

An active RadioToolButton can be set programatically using::

  radiotoolbutton.set_active(active)

If *active* is set to ``True``, the RadioToolButton will appear checked, while others in the group will be unchecked.

To check whether a RadioToolButton is active use the method::

  radiotoolbutton.get_active()

If the method returns ``True``, the RadioToolButton in the group is currently active.

=======
Signals
=======
The commonly used signals of an RadioToolButton are::

  "toggled" (radiotoolbutton)

When the user clicks on the RadioToolButton and the state is changed to active or inactive, the ``"toggled"`` signal is emitted.

=======
Example
=======
To view an example for this widget, see the :doc:`toolbar` example.
