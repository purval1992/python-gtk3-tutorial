Application
===========
An Application class handles various common functions for creating a program, such as integration with the desktop, session management and initialisation.

===========
Constructor
===========
The Application can be constructed using the following::

  application = Gtk.Application()

=======
Methods
=======
A :doc:`window` can be added to and removed from an Application via::

  application.add_window(window)
  application.remove_window(window)

To retrieve a list of Window's attached to an application call::

  windows = application.get_windows()

The active window can be found using::

  active = application.get_active_window()

=======
Example
=======
Below is an example of a Application:

.. literalinclude:: _examples/application.py

Download: :download:`Application <_examples/application.py>`
