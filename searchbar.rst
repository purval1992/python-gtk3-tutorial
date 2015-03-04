SearchBar
=========
The SearchBar widget provides an animated container, which provides an :doc:`entry` or :doc:`searchentry` for the user.

===========
Constructor
===========
The SearchBar is constructed using the following::

  searchbar = Gtk.SearchBar()

=======
Methods
=======
Items can be added to the SearchBar using::

  searchbar.add(child)

Most commonly the child should be a SearchEntry, or a standard Entry widget.

An Entry or SearchEntry needs to be connected to the SearchBar with::

  searchbar.connect_entry(entry)

To display whether the SearchBar is visible to the user, call::

  searchbar.set_search_mode(search_mode)

If the *search_mode* parameter is ``True``, the SearchBar will show. When set to ``False``, it will be hidden again.

To configure whether a close button is shown on the Search call::

  searchbar.set_show_close_button(show_button)

If *show_button* is ``True``, the SearchBar will have a close button. The default however is ``False``, and the close button is not shown.

=======
Example
=======
Below is an example of a SearchBar:

.. literalinclude:: _examples/searchbar.py

Download: :download:`SearchBar <_examples/searchbar.py>`
