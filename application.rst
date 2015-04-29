Application
===========
<<<<<<< HEAD
An Application class handles various common functions for creating a program, such as integration with the desktop, session management and initialisation. It is not required
=======
An Application class handles various common functions for creating a program, such as integration with the desktop, session management and initialisation.
>>>>>>> 94961f22f021dce2e8842f145fd12668a21ba179

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

<<<<<<< HEAD
A menubar can be defined for the Application after it has been initialised::

  application.set_menubar(menubar)

The *menubar* object needs to be a :doc:`menumodel` object.

Another type of menu is the App Menu, which contains some common functions such as Quit or Preferences. This can be added using::

  application.set_app_menu(menu)

Again, the *menu* object specified should be a :doc:`menumodel`.

=======
Signals
=======
The commonly used signals of an Application are::

  "window-added" (application, window)
  "window-removed" (application, window)

The ``"window-added"`` and ``"window-removed"`` signals emit from the Application when the ``.add_window()`` and ``.remove_window()`` methods are called.

=======
>>>>>>> 94961f22f021dce2e8842f145fd12668a21ba179
=======
Example
=======
Below is an example of a Application:

.. literalinclude:: _examples/application.py

Download: :download:`Application <_examples/application.py>`
