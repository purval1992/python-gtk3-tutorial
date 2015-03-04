AppChooserWidget
================
The AppChooserWidget object allows for an application chooser to be added to a window or dialog container, allowing custom interfaces to be built.

In most cases, an :doc:`appchooserdialog` or :doc`appchooserbutton` would be used.

The Widget-variant of the AppChooser family allows for inserting into applications and custom dialogs. If space is short, use :doc:`appchooserbutton` or if a dialog is to be shown to the user use :doc:`appchooserdialog`.

===========
Constructor
===========
The AppChooserWidget can be constructed using the following::

  appchooserwidget = Gtk.AppChooserWidget(content_type)

A *content_type* value can be specified at construction to limit displayed applications only to those which can open the specified file.

=======
Methods
=======
The string of text which is displayed when there are no available applications can be set by::

  appchooserwidget.set_default_text(default_text)

To set the AppChooserWidget to simply show all applications use::

  appchooserwidget.set_show_all(show_all)

When *show_all* is specified as ``True``, all applications are shown in a flat-layout.

To configure whether default, recommended, fallback or other applications are shown which match the mimetype call::

  appchooserwidget.set_show_default(show_default)
  appchooserwidget.set_show_recommended(show_recommended)
  appchooserwidget.set_show_fallback(show_fallback)
  appchooserwidget.set_show_other(show_other)

If *show_default*, *show_recommended*, *show_fallback* or *show_other* are set to ``False``, the widget will not display those categories of application. By default, all four are set to ``True``.

..note :

  The AppChooserWidget utilises the :doc:`appchooser` backend for common methods and functions.

=======
Signals
=======
The commonly used signals of a AppChooserWidget are::

  "application-activated" (application)
  "application-selected" (application)

The ``"application-activated"`` signal is emitted from the widget when the user presses the OK button, or via the keyboard when Return/Enter is pressed to select an application. Alternatively, a ``"application-selected"`` signal emits when an item within the widget is picked from the list.

=======
Example
=======
Below is an example of a AppChooserWidget:

.. literalinclude:: _examples/appchooserwidget.py

Download: :download:`AppChooserWidget <_examples/appchooserwidget.py>`
