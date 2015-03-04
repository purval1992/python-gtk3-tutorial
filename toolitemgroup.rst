ToolItemGroup
=============
A ToolItemGroup is used to contain icons with a similar purpose within a :doc:`toolpalette`. The group provides a title which identifies the child items, and also allows the group to be expanded or collapsed based on user-preference.

===========
Constructor
===========
The ToolItemGroup can be constructed using the following::

  toolitemgroup = Gtk.ToolItemGroup(label)

Setting the *label* to a string of text attaches it to the top of the group.

=======
Methods
=======
To set the title of the group which names the group, use::

  toolitemgroup.set_label(label)

Items should be added to the ToolItemGroup with the method::

  toolitemgroup.insert(toolitem, position)

The *toolitem* parameter is to be set to the name of a ToolItem to be added to the group. The *position* parameter should be set to the positional value where the item is inserted to, with ``0`` indicating the first position.

A ToolItem position can also be changed with::

  toolitemgroup.set_item_position(toolitem, position)

Alternatively, items can be removed from the group using::

  toolitemgroup.remove(toolitem)

By default, all ToolItemGroup objects are set as expanded and all icons visible. However, it may be necessary in some cases to collapse some groups programatically::

  toolitemgroup.set_collapsed(collapsed)

=======
Example
=======
For an example of the ToolItemGroup, see the :doc:`toolpalette` page.
