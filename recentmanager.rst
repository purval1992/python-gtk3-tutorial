RecentManager
=============
The RecentManager object is the backend of the RecentChooser family, and allows for management of the files that are displayed there.

===========
Constructor
===========
The RecentManager can be constructed using the following::

  recentmanager = Gtk.RecentManager()

=======
Methods
=======
Items can be added to the RecentManager by specifying the URI and calling the method::

  recentmanager.add_item(uri)

They can also be removed based on the URI as well by using::

  recentmanager.remove_item(uri)

Recent items can be retrieved from the RecentManager by calling::

  items = recentmanager.get_items()

This method returns a list of all the URIs within the RecentManager.

To check whether the RecentManager contains a specific URI use::

  item = recentmanager.has_item()

If the specified URI was found, ``True`` is returned.
