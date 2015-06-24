Builder
=======
Building applications manually can be difficult and time-consuming. An alternative method is to use a program such as Glade to build the interface using a graphical application in a "What You See Is What You Get" manner. The resulting file contains all the widgets and associated properties which are then automatically built at runtime.

The use of a WYSIWYG editor is beneficial as it requires less code to be written, interface changes are able to be made quicker, and people with no programming skills can still produce interfaces.

===========
Constructor
===========
The Builder object is constructed using::

  builder = Gtk.Builder()

=======
Methods
=======
Primarily, the interface will be added from the Glade-produced file::

  builder.add_from_file(filename)

Alternatively, it can be added from a string with::

  builder.add_from_string(string)

An individual object can be obtained via::

  builder.get_object(object)

The *object* string should point to a valid item name held within the Glade file.

All the items held by the Builder can be fetched and placed into a list with::

  builder.get_objects()

In combination with a dictionary, the signals can be connected automatically using the method::

  builder.connect_signals(handlers)
