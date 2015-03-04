Statusbar
=========
A Statusbar is positioned at the bottom of some application windows to provide status messages and information about an applications current process. For example, it can be used to indicate the line and column number within a text editor or which website a hyperlink directs to.

Messages on a Statusbar are stored in a stack, with the first message pushed on to the Statusbar being the last message to be popped from it.

.. note::

  Statusbar widgets should be used to display messages of low-importance. If a user must see a message, a :doc:`/messagedialog` or :doc:`/infobar` is the recommended widget to use.

===========
Constructor
===========
The Statusbar can be constructed using::

  statusbar = Gtk.Statusbar()

=======
Methods
=======
Before messages can be displayed on the Statusbar, a context identifier needs to be retrieved. This context identifier is a string which identifies particular message types, for example; errors and warnings. This can be retrived with::

  context_id = statusbar.get_context_id(context_string)

To push a message onto the Statusbar call::

  message_id = statusbar.push(context_id, text)

When calling the ``.push()`` method, a *message_id* is returned. This value is unique and identifies a particular message within the Statusbar.

Messages can be popped from the list with::

  statusbar.pop(context_id)

Alternatively, if a message is to be completely removed from the Statusbar stack, call::

  statusbar.remove(context_id, message_id)

The *context_id* is the one specified before calling the ``.push()`` method. The *message_id* must be specified and can be found when pushing messages on the Statusbar.

Alternatively, to remove all messages within a particular context use::

  statusbar.remove_all(context_id)

In some cases, it can be useful to add widgets such as ComboBox's to a Statusbar to provide quick setting selection as well as providing information. To retrieve the container, which can then be added to use::

  message_area = statusbar.get_message_area()

=======
Signals
=======
The commonly used signals of an Statusbar are::

  "text-pushed" (context_id, text)
  "text-popped" (context_id, text)

The *text-pushed* and *text-popped* signals emit when a message is pushed to or popped from the Statusbar. Both signals return the context_id of the message and the textual content.

=======
Example
=======
Below is an example of a Statusbar:

.. literalinclude:: _examples/statusbar.py

Download: :download:`Statusbar <_examples/statusbar.py>`
