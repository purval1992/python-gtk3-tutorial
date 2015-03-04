FileChooser
===========
The FileChooser is an interface which is used by :doc:`filechooserbutton`, :doc:`filechooserwidget`, and :doc:`filechooserdialog` and is constructed when those objects are constructed.

.. note:

  This widget would generally not be called by the application directly. However, the methods it offers are common among the three objects :doc:`fontchooserwidget`, :doc:`fontchooserdialog`, and :doc:`fontbutton`.

=======
Methods
=======
The default action of the FileChooser is to provide functionality to open files.

  filechooser.set_action(action)

The *action* value can be set to one of the following; ``Gtk.FileChooserAction.OPEN``, ``Gtk.FileChooserAction.SAVE``, ``Gtk.FileChooserAction.SELECT_FOLDER``, or ``Gtk.FileChooserAction.CREATE_FOLDER``.

By default, the FileChooser allows selection of a single file only. This can be configured with::

  filechooser.set_select_multiple(select_multiple)

The *select_multiple* can be set to ``True`` which allows the user to hold down :kbd:`Control` and select the items with the mouse.

Retreival of the selected filename or uniform resource identifier (URI) is done via::

  filename = widget.get_filename()
  uri = widget.get_uri()

Alternatively, if you have provided the ability for multiple files to be selected, you must use::

  filenames = widget.get_filenames()
  uris = widget.get_uris()

Another useful function, particular when saving files is to predefine a filename for the file, for example "Unsaved Document".

  filename.set_filanme(filename)

To configure whether the button to create new folders is visible, call::

  widget.set_create_folders(create_folders)

The *create_folders* option should be set to ``False`` if the button is to be hidden.

.. note:

  The ``.set_create_folders()`` option does not apply when the action ``Gtk.FileChooserAction.OPEN parameter is used.

=======
Signals
=======
The common signals of the FileChooser are as follows::

  "file-activated" (filechooser)

The ``"file-activated"`` signal emits when the user double-clicks a file, or selects a file and presses :kbd:`Enter`.

=======
Example
=======
To view an example for this widget, see the :doc:`filechooserwidget`, :doc`filechooserdialog`, or :doc:`filechooserbutton` examples.
