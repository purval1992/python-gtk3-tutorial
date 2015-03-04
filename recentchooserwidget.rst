RecentChooserWidget
===================
A RecentChooserWidget allows the selection of documents and files which have previously been opened. The widget-variant can be placed inside a Window or Dialog container.

===========
Constructor
===========
The RecentChooserWidget can be constructed using the following::

  recentchooserwidget = Gtk.RecentChooserWidget(manager)

Setting the *manager* parameter to a :doc:`recentmanager` object allows for increase control over the content of the RecentChooserWidget.

.. note::

  A RecentManager is not required to be added if only basic functions of the RecentChooserWidget are required. The RecentManager simply provides more options on working with files.

=======
Methods
=======

.. note:

  Common methods are determined by the :doc:`recentchooser`. See the page for more information on functionality.

=======
Example
=======
Below is an example of a RecentChooserWidget:

.. literalinclude:: _examples/recentchooserwidget.py

Download: :download:`RecentChooserWidget <_examples/recentchooserwidget.py>`
