Printer
=======
The Printer object represents a physical or virtual printer. Dealing with it directly is only required if the non-portable :doc:`printunixdialog` is being used.

Use of the object allows information to be retrieved such as location, description, number of queued jobs, etc. It is also used in conjunction with :doc:`printjob` to create a print job.

=======
Methods
=======
To return the assigned name of the printer call::

  printer.get_name()

Other useful information can be obtained with::

  printer.get_location()
  printer.get_description()

To obtain the status message for the printer use::

  printer.get_state_message()

The number of queued jobs can be obtained from the device via::

  printer.get_job_count()

Checking whether the printer is currently active or paused is done by::

  printer.is_active()
  printer.is_paused()

A method is also available to check whether the printer is currently accepting jobs by::

  printer.is_accepting_jobs()

To check whether the printer is set as the default device for the user call::

  printer.is_default()

Functions are also available to check whether the printer accepts PDF or PS formats using::

  printer.accepts_pdf()
  printer.accepts_ps()

Both *methods* will return ``True`` if they accept the format.

A list of paper types which the printer accepts can be obtained using the method::

  printer.list_papers()

If the paper types supported by the printer are not available, the returned list will be empty.
