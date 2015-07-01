RadioMenuItem
=============
A RadioMenuItem is the menu-based equivalent of a :doc:`radiobutton`, but is also very similar to a :doc:`checkmenuitem` with the exception that it can be added to a group. With the group specified, only one RadioMenuItem in the group can be active at any one time.

===========
Constructor
===========
The RadioMenuItem can be constructed using the following::

  radiomenuitem = Gtk.RadioMenuItem(label, group, use_underline)

The *label* parameter should be set to a string of text which identifies the function of the RadioMenuItem. A *group* must also be declared to allow the RadioMenuItem to function. For the first RadioMenuItem in the group, this would be set to ``None``, with all subsequent widgets being added to the group being the name of the first widget added. The *use_underline* value can also be set as ``True`` to provide a mnemonic key which provides accessibility via the keyboard.

=======
Methods
=======
The label text of the RadioMenuItem can be specified after creation with::

  radiomenuitem.set_label(label)

A group can also be defined after construction of the widget::

  radiomenuitem.join_group(group)

To retrieve the group which the RadioMenuItem is attached::

  radiomenuitem.get_group()

=======
Signals
=======
The commonly used signals of the RadioMenuItem are::

  "toggled" (radiomenuitem)
  "group-changed" (radiomenuitem)

A ``"toggled"`` signal is emitted by the RadioMenuItem whenever the widget is made active or inactive. The ``"group-changed"`` signal is emitted when the RadioMenuItem group is changed, or it is removed from the group entirely.

=======
Example
=======
For an example of the RadioMenuItem see the :doc:`menu` page.
