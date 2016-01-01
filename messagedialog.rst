MessageDialog
=============
A MessageDialog is used to display information or ask questions of the user. These messages are displayed within the Window that the user is working.

The MessageDialog is similar in use case to the :doc:`infobar` widget.

===========
Constructor
===========
The MessageDialog can be constructed using the following::

  messagedialog = Gtk.MessageDialog(message_type, message_format)

The *message_type* indicates the type of message which the MessageDialog will be displayed for. Setting an appropriate message type for the MessageDialog is important to ensure that the user quickly understands the context of the message. The options for this value are:

* ``Gtk.MessageType.INFO`` - used to display information messages.
* ``Gtk.MessageType.WARNING`` - used to display warning messages.
* ``Gtk.MessageType.QUESTION`` - used to display question messages.
* ``Gtk.MessageType.ERROR`` - used to display error messages.
* ``Gtk.MessageType.OTHER`` - used to display other messages.

The *message_format* should be set to the text which is to be displayed within the MessageDialog.

=======
Methods
=======
After the MessageDialog has been constructed, it can be run and destroyed with::

  messagedialog.run()
  messagedialog.destroy()

GTK+ will loop in the ``.run()`` method until it receives a response, upon which any code that needs to be run is executed (for example, responding to the users request). After completion, the ``.destroy()`` method will remove the MessageDialog.

Normal or markup-based text can be added to the MessageDialog via::

  messagedialog.set_markup(text)

By default a MessageDialog only has one line of text. To add a second level of text or markup use::

  messagedialog.format_secondary_text(text)
  messagedialog.format_secondary_markup(markup)

When secondary text is in use, the primary text entered at construction time is made bold and enlarged. The secondary text then takes the place of the primary text. The use case for this is to provide a quick overview with the primary, and a further explanation with the secondary.

The title of the MessageDialog can be set after construction via::

  messagedialog.set_title(title)

A MessageDialog should also be attached to a parent::

  messagedialog.set_transient_for(parent)

The *parent* value is the name of the parent window which called the MessageDialog.

.. note::

  If no transient (parent) window is defined, GTK+ will display a warning message that a parent should be defined. When a parent window is defined, the dialog is centered in the center of the parent window, and is destroyed when the parent is destroyed.

Buttons are attached to the MessageDialog with the method::

  messagedialog.add_button(label, response)

The *button* value should be set to a string of text identifying the function of the button. The *response* indicates the response the button emits.

Alternatively, multiple buttons can be added to the MessageDialog in a single method::

  messagedialog.add_buttons(label, response, label, response, ...)

A default button can be selected on the MessageDialog with::

  messagedialog.set_default_response(response)

The *response* type must be defined via the added buttons, otherwise it will be ignored. It should be set appropriately such that the user does not lose any data (e.g. a delete operation), but is favourable to the purpose (e.g. a continue operation).

A response can be set sensitive if required with the method::

  messagedialog.set_response_sensitive(response, sensitive)

When the *sensitive* parameter is set to ``False``, the defined *response* will be "greyed-out". This is not typically seen on a MessageDialog except when an additional widget is included which must be handled prior to continuing.

==========
Properties
==========
The message type can be set with the property::

  messagedialog.set_property("message-type", message_type)

The *message_type* can be set to ``Gtk.MessageType.INFO``, ``Gtk.MessageType.WARNING``, ``Gtk.MessageType.QUESTION``, ``Gtk.MessageType.ERROR``, or ``Gtk.MessageType.OTHER`` depending on the desired output.

The main text of the dialog can be configured using::

  messagedialog.set_property("text", text)

=======
Example
=======
Below is an example of a MessageDialog:

.. literalinclude:: _examples/messagedialog.py

Download: :download:`MessageDialog <_examples/messagedialog.py>`
