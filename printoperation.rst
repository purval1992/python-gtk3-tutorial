PrintOperation
==============
The PrintOperation object is a key part of the printing functionality of GTK+, and connects to each of the other printing functionality such as the dialogs, settings, and page setup details.

===========
Constructor
===========
The PrintOperation is constructed via::

  printoperation = Gtk.PrintOperation()

=======
Methods
=======
The job name is settable using::

  printoperation.set_job_name(name)

A job name is useful for the end user to identify the document being printed. If no job name is specified, GTK+ picks a default one based on numbering of successive jobs.

The printing functionality supports exporting the print job to file (e.g. PDF) rather than an actual device. The default filename of the exported document can be set with::

  printoperation.set_export_filename(filename)

The units used by the print job for sizing purposes can be set with::

  printoperation.set_unit(unit)

The *unit* parameter should be set to one of the following:

* ``Gtk.Unit.NONE``
* ``Gtk.Unit.POINTS``
* ``Gtk.Unit.INCH``
* ``Gtk.Unit.MM``

The print settings associated with the job can be attached by calling::

  printoperation.set_print_settings(settings)

The *settings* parameter should be set to the :doc:`printsettings` object for the job, which contains information such as paper size and orientation, whether to use colour, or the number of copies.

To configure whether the progress of the print job is shown, use::

  printoperation.set_show_progress(show_progress)

When *show_progress* is set to ``True``, a progress bar will be shown within a dialog.

Displaying status messages on the state of the printer can be important in some cases. The status can be tracked via::

  printoperation.set_track_print_status(track_status)

When *track_status* is set to ``True``, the status of the job queue may be reported back. For instance, this could be used to display "Out of paper".
