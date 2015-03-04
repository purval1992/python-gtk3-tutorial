RecentChooserMenu
=================
The RecentChooserMenu provides a list of recently opened files which are displayed via a menu.

===========
Constructor
===========
The RecentChooserMenu can be constructed using the following::

  recentchoosermenu = Gtk.RecentChooserMenu()

=======
Methods
=======
To configure whether numbers are displayed on the menu, use::

  recentchoosermenu.set_show_numbers(show_numbers)

When the *show_numbers* attribute is set to ``False``, numbers will not be displayed next to the recently opened files. The numbers also serve as a unique accelerator key to open the files via the keyboard.

.. note:

  Common methods are determined by the :doc:`recentchooser`. See the page for more information on functionality.

=======
Example
=======
Below is an example of a RecentChooserMenu:

.. literalinclude:: _examples/recentchoosermenu.py

Download: :download:`RecentChooserMenu <_examples/recentchoosermenu.py>`
