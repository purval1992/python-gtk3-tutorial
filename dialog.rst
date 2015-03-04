Dialog
======
Dialog widgets can be used to prompt or request information from the user. They are commonly used for preference dialogs where a user can configure an application.

===========
Constructor
===========
The Dialog can be constructed using the following::

  dialog = Gtk.Dialog()

=======
Methods
=======
Once the Dialog has been constructed, it can be displayed, and then subsequently destroyed with::

  dialog.run()
  dialog.destroy()

When ``dialog.run()`` is called, GTK+ loops until it receives a response. The response can be clicking on the X of the Dialog window, or clicking one of the Button's. Once the Dialog receives a response, ``dialog.destroy`` is then called.

.. note::

  If you application only uses a Dialog, the ``Gtk.main()`` call is not required. This is invoked automatically when calling ``dialog.run()``.

A Dialog widget already comes pre-packed with several :doc:`box` containers which give it the correct shape and padding. These are known as the content area and the action area. The content area is the place where you add other widgets. The action area is the place where the buttons on the Dialog are placed. Both of these can be retrieved using::

  content_area = dialog.get_content_area()
  action_area = dialog.get_action_area()

The box can then be added to or manipulated using the methods found on the :doc:`box` page.

To set the default response of the Dialog, the following method is usable::

  dialog.set_default_response(response_id)

The *response_id* can be set to any of the following constant values:

* ``Gtk.ResponseType.NONE``
* ``Gtk.ResponseType.OK``
* ``Gtk.ResponseType.CANCEL``
* ``Gtk.ResponseType.YES``
* ``Gtk.ResponseType.NO``
* ``Gtk.ResponseType.CLOSE``
* ``Gtk.ResponseType.REJECT``
* ``Gtk.ResponseType.ACCEPT``
* ``Gtk.ResponseType.DELETE_EVENT``
* ``Gtk.ResponseType.APPLY``
* ``Gtk.ResponseType.HELP``.

Alternatively, an integer value can be specified in place of a constant if none of the provided values are suitable.

In some cases, it may be necessary for one of the Dialog buttons to be as not sensitive (greyed-out). This can be set by calling::

  dialog.set_response_sensitive(response_id, setting)

The *response_id* parameter should be an appropriate response type, with the selection being from those listed above. The *setting* argument should then be a Boolean value, with ``False`` setting the button to insensitive.

By default, the Dialog contains no buttons. These can be added with::

  dialog.add_button(label, response_id)

The *label* should be set to the text which is to be displayed on the Button. A *response_id* should be appropriate for the Button type and be one of those listed above.

Alternatively, multiple buttons can be added via a single method using::

  dialog.add_buttons(label, response_id, ...)

The *label* parameter should be a textual string which will be displayed to the user. The *response_id* should be an integer value identifying the response which the button causes.

The area of the Dialog containing the buttons is known as the Action area. Other widgets can be added to this area using::

  dialog.add_action_widget(child, response_id)

The *child* should be set to the widget which is to be added. The *response_id* determines the output of the child widget when it is triggered.

To find a response which matches a widget, or a widget that matches a response use the methods::

  widget = dialog.get_widget_for_response()
  response_id = dialog.get_response_for_widget()

Setting the title of the dialog after construction is possible by calling::

  dialog.set_title(title)

A parent Window or Dialog can be defined after construction with::

  dialog.set_parent(parent)

=======
Signals
=======
The commonly used signals of a Dialog are::

  "close" (dialog)
  "response" (dialog, response_id)

The ``"close"`` event occurs when the user presses the :kbd:`Escape` button on the keyboard, or the ``Gtk.ResponseType.CLOSE`` response is met. Alternatively, ``"response"`` can be emitted when anything happens within the Dialog. Both events emit the Dialog object with the function, however the ``"response"`` signal also emits a response_id value of the event that occurred within the Dialog.

========
Examples
========
Below is an example of a Dialog:

.. literalinclude:: _examples/dialog.py

Download: :download:`Dialog <_examples/dialog.py>`
