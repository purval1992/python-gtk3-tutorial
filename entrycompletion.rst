EntryCompletion
===============
An EntryCompletion can be attached to an Entry widget to provide suggestions which match the characters entered.

===========
Constructor
===========
The EntryCompletion can be constructed using the following::

  entrycompletion = Gtk.EntryCompletion()

=======
Methods
=======
Once the EntryCompletion has been constructed, a model needs to be attached. This is used to store the potential values which can be matched::

  entrycompletion.set_model(model)

The *model* should be the name of a ListStore object.

The text column must also be set which refers to which column within the ListStore the potentially matches should be listed::

  entrycompletion.set_text_column(column)

To prevent completion lookups occuring before a certain number have characters have been entered, the following method can be used::

  entrycompletion.set_minimum_key_length(length)

The *length* parameter should be set to an integer value.

To cycle through the position completions within the Entry::

  entrycompletion.set_inline_completion(inline)

When *inline* is set to ``True``, the user can cycle through the matching completions by tabbing.

Alternatively, there is an option to provide a list of completions popped up in a popup window with::

  entrycompletion.set_popup_completion(popup)

=======
Example
=======
Below is an example of a EntryCompletion:

.. literalinclude:: _examples/entrycompletion.py

Download: :download:`EntryCompletion <_examples/entrycompletion.py>`
