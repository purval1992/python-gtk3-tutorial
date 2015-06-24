Assistant
=========
An Assistant widget provides a preset dialog which allows moving through pages in a specific order. It is commonly used to retrieve configuration settings for
complex applications.

===========
Constructor
===========
The Assistant can be constructed using the following::

  assistant = Gtk.Assistant()

=======
Methods
=======
There are three methods which can be used to add pages to the widget::

  assistant.insert_page(widget, page)
  assistant.append_page(widget)
  assistant.prepend_page(widget)

The ``.insert()`` method requires a *widget* to be specified which is added to the page. This is commonly a Grid or Box container. The *page* value should be an integer indicating the position at which the page is to be inserted. The ``.append()`` and ``.prepend()`` methods require just a *widget* to be specified, and are added in the ordered they are called.

Pages can also be removed by calling::

  assistant.remove_page(page)

The *page* argument should be the number of the page which is to be removed.

When pages have been added to the Assistant, it is necessary to provide the type of page via::

  assistant.set_page_type(widget, page_type)

The *widget* parameter is the same widget which was specified when calling the ``.insert_page()``, ``.append()``, or ``.prepend()`` methods. The *page_type* constant can be one of:

* ``Gtk.AssistantPageType.INTRO``
* ``Gtk.AssistantPageType.CONTENT``
* ``Gtk.AssistantPageType.PROGRESS``
* ``Gtk.AssistantPageType.CONFIRM``
* ``Gtk.AssistantPageType.SUMMARY``

A title should also be set on the page to describe help identify the content::

  assistant.set_page_title(widget, page_title)

Again, the *widget* parameter must be the same as the one specified when adding the page. The *page_title* is simply a textual string.

To retrieve the current page being viewed in the Assistant call::

  page = assistant.get_current_page()

Alternatively, to set the page in view use::

  assistant.set_current_page(page)

The *page* parameter should be set to an integer, with ``0`` indicating the first page within the Assistant.

To return the number of pages in the Assistant run::

  n_pages = assistant.get_n_pages()

A page title can be added to the header with the method::

  assistant.set_page_title(title)

The area of the Assistant where the buttons are located is known as the action area. Extra buttons can be added and removed from the area area using::

  assistant.add_action_widget(child)
  assistant.remove_action_widget(child)

Pages can be switched programmatically using the methods::

  assistant.next_page()
  assistant.previous_page()

Padding can be applied to the Assistant page via the method::

  assistant.set_page_has_padding(page, padding)

The *page* parameter should be set to the widget being displayed on the page. The *padding* value when set to ``True`` inserts a space around the edge to clean up the display.

=======
Signals
=======
The commonly used signals of an Assistant are::

  "apply" (assistant)
  "closed" (assistant)
  "cancel" (assistant)

The ``"apply"`` signal emits when the user presses the Apply button on a page. A ``"closed"`` signal is emitted when the user explicitly closes the Assistant by pressing a Close button. The ``"cancel"`` signal emits when the user presses the Cancel button, or the X on the titlebar of the Assistant window.

=======
Example
=======
Below is an example of an Assistant:

.. literalinclude:: _examples/assistant.py

Download: :download:`Assistant <_examples/assistant.py>`
