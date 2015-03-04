MenuBar
=======
A MenuBar provides the basis of a application menu, with access to menus such as File, Edit, Help, etc being displayed within the MenuBar.

===========
Constructor
===========
The MenuBar can be constructed using the following::

  menubar = Gtk.MenuBar()

=======
Methods
=======
Items can be added to the MenuBar after construction with::

  menubar.append(menuitem)
  menubar.prepend(menuitem)
  menubar.insert(menuitem, position)

The ``.append()`` method packs items as they are called. The ``.prepend()`` method adds items to the front of the MenuBar in the order they are called. Using the ``.insert()`` method allows for the insertion of MenuItem widgets to a particular location within the MenuBar.

By default, items are packed to the left of the MenuBar. This can be changed via the method::

  menubar.set_pack_direction(pack_direction)

The *pack_direction* can be set to ``Gtk.PackDirection.RTL`` which pushes items to the right, ``Gtk.PackDirection.TTB`` which stacks widgets beneath the previous one, or ``Gtk.PackDirection.BTT`` which stacks widgets on top of one another. The default value is ``Gtk.PackDirection.LTR``.

=======
Example
=======
For an example of the MenuBar see the :doc:`menu` page.
