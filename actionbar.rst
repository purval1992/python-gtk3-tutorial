ActionBar
=========
The ActionBar widget provides a full width bar for items such as :doc:`button` and :doc:`label` widgets. It is usually placed below the application content and is commonly used in place of a :doc:`statusbar`.

===========
Constructor
===========
The ActionBar is constructed using::

  actionbar = Gtk.ActionBar()

=======
Methods
=======
Items can be packed into the container at the start (left) or end (right)::

  actionbar.pack_start(child)
  actionbar.pack_end(child)

If required, items can also be placed in the center::

  actionbar.set_center_widget(child)

The center widget can also be retrieved via::

  child = actionbar.get_center_widget()
