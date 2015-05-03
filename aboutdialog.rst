AboutDialog
===========
The AboutDialog is found in virtually all non-trivial applications. It provides access to the version number, license, authors, translators and other information relating to the development of the program.

===========
Constructor
===========
The AboutDialog can be constructed using::

  aboutdialog = Gtk.AboutDialog()

=======
Methods
=======
Once constructed, the AboutDialog will be void of information with the exception of the name of the Python script. A variety of information can now be added with::

  aboutdialog.set_program_name(name)
  aboutdialog.set_version(version)
  aboutdialog.set_copyright(copyright)
  aboutdialog.set_comments(comment)
  aboutdialog.set_website(website)
  aboutdialog.set_website_label(label)
  aboutdialog.set_authors([authors])
  aboutdialog.set_documenters([documenters])
  aboutdialog.set_artists([artists])
  aboutdialog.set_logo(filepath)
  aboutdialog.set_wrap_license(wrap)

Most of the options are self-explanatory and take a string of text. The ``.set_comments()`` method is a simple message about what the application is or does. The ``.set_wrap_license()`` method tells the license text to be displayed neatly within the dialog window, and should in most cases will be set to ``True``. The ``.set_authors()``, ``.set_documenters()`` and ``.set_artists()`` methods take a Python list of values, with each persons name separated by a comma and contained within square brackets.

The license used by the program can be set with::

  aboutdialog.set_license_type(license)

The *license* value can be set to a number of built-in license types:

* ``Gtk.License.UNKNOWN``
* ``Gtk.License.CUSTOM``
* ``Gtk.License.GPL_2_0``
* ``Gtk.License.GPL_3_0``
* ``Gtk.License.LGPL_2_1``
* ``Gtk.License.LGPL_3_0``
* ``Gtk.License.BSD``
* ``Gtk.License.MIT_X11``
* ``Gtk.License.ARTISTIC``
* ``Gtk.License.GPL_2_0_ONLY``
* ``Gtk.License.GPL_3_0_ONLY``
* ``Gtk.License.LGPL_2_1_ONLY``
* ``Gtk.License.LGPL_3_0_ONLY``

A new section for credits can be added with::

  aboutdialog.add_credit_section(name, people, people...)

The *name* value determines the name of the section in the display. One or multiple *people* values can be added to each section.

To display, and then subsequently remove the AboutDialog from view use::

  aboutdialog.run()
  aboutdialog.destroy()

When the ``.run()`` method is executed, the AboutDialog enters a loop and will continue to be displayed until the AboutDialog is destroyed. The event to destroy occurs when the X button or Close button is pressed.

.. note::

  If you application only uses a Dialog, the ``Gtk.main()`` call is not required. This is invoked automatically when calling ``aboutdialog.run()``.

By default, the AboutDialog positions itself in the center of the screen rather than the center of the parent window, if there is one. To ensure neatness and position the AboutDialog over the window::

  aboutdialog.set_transient_for(window)

The *window* argument should be the name of the parent window.

=======
Signals
=======
The commonly used signals of an AboutDialog are::

  "activate-link" (aboutdialog, uri)

The ``"activate-link"`` signal emits when the user clicks the website button within the AboutDialog. This allows configuring of what happens when the user clicks this link. If ``"activate-link"`` is not used, the default action is to open the default web browser on the system and navigate to the website.

=======
Example
=======
Below is an example of an AboutDialog:

.. literalinclude:: _examples/aboutdialog.py

Download: :download:`AboutDialog <_examples/aboutdialog.py>`
