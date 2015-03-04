SearchEntry
===========
The SearchEntry widget provides a tailored interface for searching. Essentially, it is a stardard :doc:`entry` with a find icon when the search field is empty, that then changes to a clear icon when text has been entered.

===========
Constructor
===========
The SearchEntry can be constructed using the following::

  searchentry = Gtk.SearchEntry()

=======
Methods
=======
The text can be retrieved from the SearchEntry::

  text = searchentry.get_text()

Placeholder text can be added to the SearchEntry to describe the function of the widget::

  searchentry.set_placeholder_text(text)

=======
Signals
=======
The commonly used signals of a SearchEntry are::

  "search-changed" (searchentry)

The ``"search-changed"`` signal emits each time the user enters a character into the search field.  

=======
Example
=======
Below is an example of a SearchEntry:

.. literalinclude:: _examples/searchentry.py

Download: :download:`SearchEntry <_examples/searchentry.py>`
