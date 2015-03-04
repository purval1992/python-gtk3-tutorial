RadioToolButton
===============
A RadioToolButton provides a widget similar to a :doc:`radiobutton` for use within a :doc:`toolbar`. When used with other RadioToolButton widgets, only one in the group can be active at a single time.

===========
Constructor
===========
The RadioToolButton can be constructed using the following::

  radiotoolbutton = Gtk.RadioToolButton(label, use_underline, group)

The first constructor allows creation of a RadioToolButton with custom text. This is specified via the *label* paramter. When setting the *use_underline* to ``True``, the letter proceeding the underscore in the label string will be used as a mnemonic key. Both constructors use the *group* parameter identifiying the group the RadioToolButton belongs.

=======
Methods
=======
.. note::

  The methods listed below only apply to this widget and those that inherit from it. For more methods, see the :doc:`toolbutton` page. For more information on widget hierarchy, see :doc:`hierarchytheory`.

A group can be applied to the RadioToolButton via::

  radiotoolbutton.set_group(group)

The name of the group which the RadioToolButton is attached to can also be specified with::

  group = radiotoolbutton.get_group()

=======
Example
=======
To view an example for this widget, see the :doc:`toolbar` example.
