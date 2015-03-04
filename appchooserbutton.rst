AppChooserButton
================
An AppChooserButton allows the selection of applications via a dropdown menu. The use of an AppChooserButton is useful in applications which have limited space available.

===========
Constructor
===========
The AppChooserButton can be constructed using the following::

  appchooserbutton = Gtk.AppChooserButton(content_type)

Setting the *content_type* to a MIME type allows the AppChooserButton to limit the applications shown to those which are able to open the content type specified.

=======
Methods
=======
By default, the AppChooserButton is displayed as a basic dropdown menu. To enable the advanced dropdown and associated dialog functionality, from which items are chosen use::

  appchooserbutton.set_show_dialog_item(show_dialog_item)

If *show_dialog_item* is set to ``True``, applications matching the MIME type are displayed in a dialog.

..note :

  The AppChooserButton utilises the :doc:`appchooser` backend for common methods and functions.

=======
Signals
=======
The commonly used signals of a AppChooserButton are::

  "changed" (appchooserbutton)

The ``"changed"`` signal emits from the AppChooserButton when the user changes the application which is to open the item.

=======
Example
=======
Below is an example of a AppChooserButton:

.. literalinclude:: _examples/appchooserbutton.py

Download: :download:`AppChooserButton <_examples/appchooserbutton.py>`
