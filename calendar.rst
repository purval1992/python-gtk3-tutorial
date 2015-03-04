Calendar
========
A Calendar widget allows for displaying and retrival of date information. It can be configured in many ways and is a relatively powerful widget.

===========
Constructor
===========
The Calendar can be constructed using the following::

  calendar = Gtk.Calendar()

=======
Methods
=======
The date can be retrieved from the Calendar using::

  date = calendar.get_date()

The *date* will be returned in comma-seperated format. The day value will be between 1 and 31, the month will be between 0 and 11 and the date will be in four-digit number format.

To select a specific day on the Calendar call::

  calendar.select_day(day)

Alternatively, to set a month and year call::

  calendar.select_month(month, year)

To configure the view of the Calendar, the following method can be used::

  calendar.set_display_options(flags)

The *flags* parameter can take the following parameters; ``Gtk.CalendarDisplayOptions.SHOW_HEADING`` configures whether the month and year should be displayed, ``Gtk.CalendarDisplayOptions.SHOW_DAY_NAMES`` specifies whether the three letter day description should be present, ``Gtk.CalendarDisplayOptions.NO_MONTH_CHANGE`` prevents the user from changing the month. ``Gtk.CalendarDisplayOptions.SHOW_WEEK_NUMBERS`` sets the calendar to display the week number down the left-side of the Calendar and ``Gtk.CalendarDisplayOptions.SHOW_DETAILS`` sets the calendar to show an indicator as opposed to the full details text. When multiple flags are required, they should be a seperated by a '|' character.

=======
Signals
=======
The commonly used signals of a Calendar are::

  "day-selected" (calendar)
  "day-selected-double-click" (calendar)
  "month-changed" (calendar)
  "next-month" (calendar)
  "next-year" (calendar)
  "prev-month" (calendar)
  "prev-year" (calendar)

The ``"day-selected"`` and ``"day-selected-double-click"`` signals emit from the Calendar when the user clicks or double clicks on a date. A ``"month-changed"`` signal is emitted when the user changes months and year. The signals ``"next-month"``, ``"next-year"``, ``"prev-month"``, and ``"prev-year"`` emit whenever the users moves back or forward on a month or year basis.

=======
Example
=======
Below is an example of a Calendar:

.. literalinclude:: _examples/calendar.py

Download: :download:`Calendar <_examples/calendar.py>`
