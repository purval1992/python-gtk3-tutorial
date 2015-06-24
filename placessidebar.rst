PlacesSidebar
=============
The PlacesSidebar offers a list of frequently used locations in the file system. It is commonly found in file managers and also seen in the :doc:`filechooser` family of widgets.

===========
Constructor
===========
The PlacesSidebar can be created with::

  placessidebar = Gtk.PlacesSidebar()

=======
Methods
=======
The PlacesSidebar offers a number of flag options to configure how the widget provides links. The use of these flags is also dependant on what the application supports::

  placessidebar.set_open_flags(flags)

The *flags* parameter can be set to one of the following; ``Gtk.Places.OPEN_NORMAL``, ``Gtk.Places.OPEN_NEW_TAB``, or ``Gtk.Places.OPEN_NEW_WINDOW``. The default option is ``Gtk.Places.OPEN_NORMAL`` and tells the application to open the link in usual way.

To set whether the shortcut to the Desktop is shown use::

  placessidebar.set_show_desktop(show_desktop)

When *show_desktop* is set to ``True``, the shortcut will be shown. The default however is for this to be hidden.

An option to configure whether the Connect to Server option is shown can be made with::

  placessidebar.set_show_connect_to_server(show_server)

If *show_server* is set to ``False``, the option is hidden. This is useful if the application implements a way to connect to servers itself in a different way.

The desktop environment is able to determine whether recent items are displayed. This can be overridden via::

  placessiderbar.set_show_recent(show_recent)

When *show_recent* is set to ``False, the recent items are not displayed.

=======
Signals
=======
The common signals of the PlaceSider are::

  "populate-popup" (placessidebar, menu, selected_item, selected_volume)

The ``"populate-popup"`` signal emits when the user invokes the context menu of the PlacesSidebar. A *menu* parameter emits containing the :doc:`menu` widget, which allows appending of custom menu items. The *selected_item* points to the file item, or ``None`` if the item is a volume. The *selected-volume* value points to the volume passed, or ``None`` if the item is a file.

=======
Example
=======
Below is an example of a PlacesSidebar:

.. literalinclude:: _examples/placessidebar.py

Download: :download:`PlacesSidebar <_examples/placessidebar.py>`
