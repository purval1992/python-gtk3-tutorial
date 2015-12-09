Statusbar
=========
A Statusbar is positioned at the bottom of some application windows to provide status messages and information about an applications current process. For example, it can be used to indicate the line and column number within a text editor or which website a hyperlink directs to in a web browser.

Messages on a Statusbar are stored in a stack, with the first message pushed on to the Statusbar being the last message to be popped from it.

.. note::

  Statusbar widgets should be used to display messages of low-importance. If a user must see a message, a :doc:`messagedialog` or :doc:`infobar` is the recommended widget to use.

===========
Constructor
===========
The Statusbar can be constructed using::

  statusbar = Gtk.Statusbar()

=======
Methods
=======
Before messages can be displayed on the Statusbar, a context identifier needs to be retrieved. This context identifier is a string which identifies particular message types, for example; errors and warnings. This can be retrived with::

  statusbar.get_context_id(context)

The *context* parameter is simply a string describing the context (purpose) of the message. The method returns the context id which is used to push, pop and remove messages.

To push a message onto the Statusbar call::

  statusbar.push(context, text)

When calling the ``.push()`` method, a message id is returned. This value is unique and identifies a particular message within the Statusbar.

Messages can be popped from the list with::

  statusbar.pop(context)

Alternatively, if a message is to be completely removed from the Statusbar stack, call::

  statusbar.remove(context, message)

The *context* is the one specified before calling the ``.push()`` method. The *message* parameter takes the message id for the message to be removed, and must be specified.

Alternatively, to remove all messages within a particular context use::

  statusbar.remove_all(context)

In some cases, it can be useful to add widgets such as ComboBox widgets to a Statusbar to provide quick setting selection as well as providing information. To retrieve the container, which can then be added to use::

  statusbar.get_message_area()

The ``.get_message_area()`` method returns a :doc:`box` with horizontal orientation.

=======
Signals
=======
The commonly used signals of an Statusbar are::

  "text-pushed" (context, text)
  "text-popped" (context, text)

The *text-pushed* and *text-popped* signals emit when a message is pushed to or popped from the Statusbar. Both signals return the context id of the message and the textual content.

=======
Example
=======
Below is an example of a Statusbar:

.. literalinclude:: _examples/statusbar.py

Download: :download:`Statusbar <_examples/statusbar.py>`
