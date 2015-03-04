Stack
=====
The Stack widget is a container which shows a single widget at a time. The widget is similar to a :doc:`notebook` but it provides no means for the user to switch which child is visible.

If there is a requirement for the user to switch which child is visible, a :doc:`stackswitcher` can be used.

===========
Constructor
===========
The Stack can be constructed using::

  stack = Gtk.Stack()

=======
Methods
=======
To add child widgets to the Stack, use the method::

  stack.add_named(child, name)

The *child* parameter is the name of the widget to be displayed in the Stack. The *name* specified is an identifier for the child.

If a StackSwitch is going to be used, a title can also be provided when adding the child widget.

  stack.add_title(child, name, title)

To set the visible child, use::

  stack.set_visible_child(child)
  stack.set_visible_child_name(name)

When using ``.set_visible_child_name()``, the name is the string provided when adding the child to the Stack.

To ensure that the Stack requests the same size for all child widgets call::

  stack.set_homogeneous(homogeneous)

If *homogeneous* is set to ``False``, the Stack will resize to the same size as the child everytime a new child is displayed.

A number of transition types can be set when switching child widgets::

  stack.set_transition_type(transition_type)

The *transition_type* should be set to one of:

* ``Gtk.StackTransitionType.NONE``
* ``Gtk.StackTransitionType.CROSSFADE``
* ``Gtk.StackTransitionType.SLIDE_RIGHT``
* ``Gtk.StackTransitionType.SLIDE_LEFT``
* ``Gtk.StackTransitionType.SLIDE_UP``
* ``Gtk.StackTransitionType.SLIDE_DOWN``
* ``Gtk.StackTransitionType.SLIDE_LEFT_RIGHT``
* ``Gtk.StackTransitionType.SLIDE_UP_DOWN``.

=======
Example
=======
Below is an example of an Stack:

.. literalinclude:: _examples/stack.py

Download: :download:`Stack <_examples/stack.py>`
