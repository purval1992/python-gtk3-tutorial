PageSetupUnixDialog
===================
The PageSetupUnixDialog provides a dialog for platforms which don't provide a native alternative, and offers options on setting up pages for printing. Its features allow for modifying the paper size or the page output orientation.

===========
Constructor
===========
The construction of the PageSetupUnixDialog dialog is done with::

  pagesetupunixdialog = Gtk.PageSetupUnixDialog()

=======
Methods
=======
The :doc:`pagesetup` object can be attached to the dialog via::

  pagesetupunixdialog.set_page_setup(pagesetup)

The PageSetup can also be retrieved using::

  pagesetupunixdialog.get_page_setup()

A :doc:`printsettings` object can also be specified with::

  pagesetupunixdialog.set_print_settings(printsettings)

Retrieval of the PrintSettings can also be fetched via::

  pagesetupunixdialog.get_print_settings()
