Clipboard
=========
A Clipboard is an invisible object within GTK+ that provides the ability to copy content to and from your application. The content can range from text, images, audio, or video.

.. note::

  A clipboard and its associated methods are quite complex and will require good understanding of GTK+.

===========
Constructor
===========
The Clipboard can be constructed using the following::

  clipboard = Gtk.Clipboard.get(selection)

The selection value should be set to either ``Gdk.SELECTION_CLIPBOARD`` or ``Gdk.SELECTION_PRIMARY``. The ``Gdk.SELECTION_CLIPBOARD`` item allows content to be transferred to and from the general clipboard. Alternatively, ``Gdk.SELECTION_PRIMARY`` is used to capture content when it is highlighted.

.. note:: The use ``Gdk.SELECTION_CLIPBOARD`` or ``Gdk.SELECTION_PRIMARY``, you will need to import the Gdk module before calling a Gdk constant.

=======
Methods
=======
To clear the current contents of the Clipboard use::

  clipboard.clear()

.. note:: The .clear() method will clear the contents of the clipboard regardless of which application stored the data.

Setting text on the Clipboard can be achieved via::

  clipboard.set_text(text, length)

The *text* value is the string of text which is to be stored on the clipboard. The *length* value allows for the number of characters to be limited. If all the content should be stored, use ``-1``.

Images can also be stored using::

  clipboard.set_image(image)

The *image* paramter should be a Pixbuf object representing the image.

By default, when an application closes, any data saved to the clipboard using it will be cleared. To store the data after the application closes call::

  clipboard.store()

=======
Example
=======
Below is an example of a Clipboard:

.. literalinclude:: _examples/clipboard.py

Download: :download:`Clipboard <_examples/clipboard.py>`
