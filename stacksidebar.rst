StackSidebar
============
The StackSidebar provides a way to switch between :doc:`stack` objects via a list. The list is automatically populated with the children held by the Stack container.

Common use cases of the StackSidebar include preference screens, or other displays with many options which should be grouped together.

===========
Constructor
===========
The StackSidebar is constructed using::

  stacksidebar = Gtk.StackSidebar()

=======
Methods
=======
To attach the Stack container to the StackSidebar, call::

  stacksidebar.set_stack(stack)

The Stack associated with the StackSidebar can also be retrieved via::

  stacksidebar.get_stack()

========
Property
========
The Stack object can also be handled by the properties::

  stacksidebar.get_property("stack")
  stacksidebar.set_property("stack", stack)

=======
Example
=======
Below is an example of an StackSidebar:

.. literalinclude:: _examples/stacksidebar.py

Download: :download:`StackSidebar <_examples/stacksidebar.py>`
