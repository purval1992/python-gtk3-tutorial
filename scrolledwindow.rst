ScrolledWindow
==============
A ScrolledWindow provides scrolling functionality for widgets which are larger than their container. A ScrolledWindow automatically provides :doc:`scrollbar` widgets automatically and would be used in most cases.

===========
Constructor
===========
The ScrolledWindow can be constructed using the following::

  scrolledwindow = Gtk.ScrolledWindow(hadjustment, vadjustment)

The *hadjustment* and *vadjustment* parameters are optional, but can be used to specify the :doc:`adjustment` objects for scrolling a widget.

=======
Methods
=======
Content can be added to the ScrolledWindow with::

  scrolledwindow.add(child)
  scrolledwindow.add_with_viewport(child)

The ``.add()`` method must be used with widgets that support scrolling such as TextView, TreeView or IconView. Alternatively, ``.add_with_viewport()`` should be used for widgets that do not natively allow scrolling such as Box or Grid.

Child widgets can be removed if needed by calling::

  scrolledwindow.remove(child)

By default, the scrollbars are both displayed regardless of whether they are active or not. To configure this policy use::

  scrolledwindow.set_policy(hscrollbar_policy, vscrollbar_policy)

Both parameters can be setting to one of the following; ``Gtk.PolicyType.ALWAYS``, ``Gtk.PolicyType.AUTOMATIC`` or ``Gtk.PolicyType.NEVER``. When ``Gtk.PolicyType.ALWAYS`` is used, the scrollbars are always shown. ``Gtk.PolicyType.NEVER`` sets the scrollbars to never show, even if the content is larger than the container. The ``Gtk.PolicyType.AUTOMATIC`` constant sets the scrollbar to display if the content is larger than the container, otherwise it is not shown.

The *hadjustment* and *vadjustment* methods can be added after construction using::

  scrolledwindow.set_hadjustment(adjustment)
  scrolledwindow.set_vadjustment(adjustment)

The default setting is that the scrollbars should be positioned on the right and along the bottom. In most cases this should be sufficient, however to change the position of the scrollbar objects use::

  scrolledwindow.set_placement(window_placement)

The *window_placement* argument should be configured to one of the following; ``Gtk.CornerType.TOPLEFT``, ``Gtk.CornerType.TOPRIGHT``, ``Gtk.CornerType.BOTTOMLEFT`` or ``Gtk.CornerType.BOTTOMRIGHT``.

The placement can be unset if required::

  scrolledwindow.unset_placement()

To prevent content shrinking to a size which is deemed too small, call::

  scrolledwindow.set_min_content_height(height)
  scrolledwindow.set_min_content_width(width)

The *width* value should be specified in pixels.

=======
Example
=======
Below is an example of an ScrolledWindow:

.. literalinclude:: _examples/scrolledwindow.py

Download: :download:`ScrolledWindow <_examples/scrolledwindow.py>`
