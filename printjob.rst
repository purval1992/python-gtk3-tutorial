PrintJob
========
The PrintJob object represents a print job sent to the printer.

===========
Constructor
===========
The constructor for the PrintJob is::

  printjob = Gtk.PrintJob(title, printer, printsettings, pagesetup)

=======
Methods
=======
The title of the PrintJob can be retrieved with::

  printjob.get_title()

The number of pages to be printed is settable using::

  printjob.set_pages(pages)

A number of features about the print output can be fetched using::

  printjob.get_reverse()
  printjob.get_collate()
  printjob.get_rotate()
  printjob.get_num_copies()

The print settings are also settable via::

  printjob.set_reverse(reverse)
  printjob.set_collate(collate)
  printjob.set_rotate(rotate)
  printjob.set_num_copies(copies)

Retrieval of a print job status is done with the method::

  printjob.get_status()

The :doc:`printsettings` or :doc:`printer` objects can be requested using::

  printjob.get_settings()
  printjob.get_printer()
