PrintUnixDialog
===============
The PrintUnixDialog implements a dialog for platforms which do not provide a native dialog. It provides functionality for setting up the print options such as printer to output the document to, the number of copies, the page orientation, and image quality settings.

===========
Constructor
===========
A PrintUnixDialog is able to be constructed using::

  printunixdialog = Gtk.PrintUnixDialog()

=======
Methods
=======
Retrieval of the selected printer object can be made using the method::

  printunixdialog.get_selected_printer()

The ``.get_selected_printer()`` method returns a :doc:`printer` object.

In some cases, the user will be able to select only a portion of the document to print. The dialog can be told that it should support selections, and provide the option using::

  printunixdialog.set_support_selection(support_selection)

The capabilities of the print dialog can be customised with::

  printunixdialog.set_manual_capabilities(capabilities)

A large number of *capabilities* are offered which change the offered options:

* ``Gtk.PrintCapability.PAGE_SET`` - offer printing of odd/even pages.
* ``Gtk.PrintCapability.COPIES`` - allow setting of number of copies.
* ``Gtk.PrintCapability.COLLATE`` - provide collation of multiple copies.
* ``Gtk.PrintCapability.REVERSE`` - set whether outputted job is done in reverse.
* ``Gtk.PrintCapability.SCALE`` - scale the output.
* ``Gtk.PrintCapability.GENERATE_PDF`` - allow sending of document to PDF output.
* ``Gtk.PrintCapability.GENERATE_PS`` - allow sending of document to PS output.
* ``Gtk.PrintCapability.PREVIEW`` - provide option to preview output.
* ``Gtk.PrintCapability.NUMBER_UP`` - setting to print multiple sheets onto a single page.
* ``Gtk.PrintCapability.NUMBER_UP_LAYOUT`` - setting to allow rearrange multiple sheets onto a single page.

A custom tab can be added to the printing dialog which allows placement of additional widgets::

  printunixdialog.add_custom_tab(child, label)

The *child* parameter indicates the widget to be displayed in the tab, with the *label* parameter identifying the tabs purpose.
