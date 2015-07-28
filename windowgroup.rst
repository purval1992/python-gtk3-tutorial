WindowGroup
===========
The WindowGroup class allows :doc:`window` objects to behave like separate applications. When added to a group, of which a Window can be a member of one group at any one time, the effect of grabs are restricted.

===========
Constructor
===========
The WindowGroup object is constructed using::

  windowgroup = Gtk.WindowGroup()

=======
Methods
=======
Additions to the group can be made via::

  windowgroup.add_window(window)

A Window object can be removed from the group with::

  windowgroup.remove_window(window)

To list all the Window objects currently associated with a group, call::

  windowgroup.list_windows()
