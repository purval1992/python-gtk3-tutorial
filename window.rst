Window
======
The Window is the basis of most applications created using GTK+. It is the widget which provides the framework on which other widgets can be added; therefore it is known as a container widget.

On its own, a Window can only pack a single widget within its container.

===========
Constructor
===========
The Window can be constructed using::
  
  window = Gtk.Window()

=======
Methods
=======
Widgets can be added to or removed from the Window with the following::

  window.add(widget)
  window.remove(widget)

A title can also be displayed on the Window with::

  window.set_title(text)

By default, the size of the Window is 200x200 pixels when there is no content within the Window. This can be changed at launch with::

  window.set_default_size(width, height)

In some cases, it may only be required to set the width or the height. To set a size dynamically, use -1. This will then size the Window to that of the child content.

To maximize, unmaximize, minimize or unminimize a Window, the following methods can be used::

  window.maximize()
  window.unmaximize()
  window.iconify()
  window.deiconify()

In some cases, it is useful to allow the Window to be made fullscreen. The methods used to make a Window fullscreen or unfullscreened are::

  window.fullscreen()
  window.unfullscreen()

By default, all Windows allow the user to resize them as necessary. This automatically adjusts the content and re-flows it as per the Window size. The ability to allow resizes can be configured with::

  window.set_resizable(resizable)

When *resizable* is set to False, two changes are made to the Window. First, there will be no maximize button on the title bar. Second, the user can now adjust the Window size by grabbing the border of the Window.

A resize grip is positioned in the bottom-right corner of all windows which are resizable. To disable this run::

  window.set_has_resize_grip(resize_grip)

When *resize_grip* is set to ``False``, the resize grip will be removed.

To make your application easily identifiable, you can specify an Window icon to be set with::

  window.set_icon_from_file(file_path)

The *file_path* parameter should be set to that of an image such as a PNG, SVG, JPG, GIF, XPM or BMP (others are supported but those are the most common).

To set the focus of a particular widget at program execution time, use::

  window.set_focus(child)

In some cases, it may be necessary to display a Window on top of another Window, and prevent interaction with the Window on the bottom. This can be achieved by setting the top Window as modal with::

  window.set_modal(modal)
  
When *modal* is set to True, the bottom Window can not be interacted with by the user until the modal Window has been closed.

Another useful feature when working with multiple Window widgets is to make any child Windows related to their parent. This allows for neatness when the Windows are positioned. This can be done by::

  window.set_transient_for(child)

The *child* should be the name of another Window.

When setting a Window to be transient for another, it is also useful to allow the child Window to be destroyed if the parent is with::

  window.set_destroy_with_parent(destroy)

By default, all Window widgets created are decorated with a title bar that often contains icons, the application title and buttons. To control whether the Window Manager decorates the Window, use::

  window.set_decorated(decorated)

When *decorated* is set to False, GTK+ will ask the Window to remove the Window decorations. Depending on the Window Manager in use and the platform being used, this may not have any effect.

Custom title bars can be set on the Window with the following method::

  window.set_titlebar(child)

The *child* is a widget, most likely a :doc:`grid` or :doc:`box` with other child widgets. When this option is in use, GTK+ will tell the window manager not to draw a standard titlebar on the Window.

.. note::

  GTK+ will tell the window manager not to display a titlebar, however the window manager is free to ignore this function if it is not supported.

=======
Signals
=======
The commonly use signals of a Window are::

  "destroy"
  "delete-event"
  "event"
  "add"
  "remove"

The "destroy" signal is emitted when the user requests that the Window be destroyed. This is often emitted from the X button on the Title Bar of the Window. A "delete-event" is much the same as "destroy", however it is a request rather than a command. This is useful when wanting to confirm a close rather than command it. An "event" signal is used to notify on any events relating to the Window. The "add" and "remove" signals emit when child widgets are added to or removed from the Window.

=======
Example
=======
Below is an example of a Window:

.. literalinclude:: _examples/window.py

Download: :download:`Window <_examples/window.py>`
