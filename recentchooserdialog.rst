RecentChooserDialog
===================
A RecentChooserDialog provides selection of recently opened documents from a dialog.

===========
Constructor
===========
The RecentChooserDialog can be constructed using the following::

  recentchooserdialog = Gtk.RecentChooserDialog(manager, (buttons))

Setting the *manager* parameter to a :doc:`recentmanager` object allows for increase control over the content of the RecentChooserDialog. Finally, the *buttons* parameter should be a tuple of buttons which are to be displayed on the dialog.

.. note::

  A RecentManager is not required to be added if only basic functions of the RecentChooserWidget are required. The RecentManager simply provides more options on working with files.

=======
Methods
=======
Once the RecentChooserDialog has been created, use the following to run and then destroy the widget::

  recentchooserdialog.run()
  recentchooserdialog.destroy()

GTK+ will loop in the ``.run()`` method until it receives a response, upon which any code that needs to be run is executed (for example, responding to the users request). After completion, the ``.destroy()`` method will remove the RecentChooserDialog.

A title can be set on the RecentChooserDialog with::

  recentchooserdialog.set_title(title)

To ensure the dialog is positioned correctly over the parent window, it is recommended to set parent with::

  recentchooserdialog.set_parent(parent)

.. note:

  Common methods are determined by the :doc:`recentchooser`. See the page for more information on functionality.

=======
Signals
=======
The commonly used signals of a RecentChooserDialog are::

  "response" (dialog, response_id)
  "close" (dialog)

The ``"close"`` event occurs when the user presses the :kbd:`Escape` button on the keyboard, or the ``Gtk.ResponseType.CLOSE`` response is met. Alternatively, ``"response"`` can be emitted when anything happens within the RecentChooserDialog. Both events emit the RecentChooserDialog object with the function, however the ``"response"`` signal also emits a response_id value of the event that occurred within the RecentChooserDialog.

=======
Example
=======
Below is an example of a RecentChooserDialog:

.. literalinclude:: _examples/recentchooserdialog.py

Download: :download:`RecentChooserDialog <_examples/recentchooserdialog.py>`
