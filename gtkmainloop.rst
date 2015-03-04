GTK+ Main Loop
==============
GTK+ is event-driven by nature in that actions or procedures are performed when an event occurs within the application. Take for example the 'Hello World' application from earlier:

.. literalinclude:: _examples/gtkmainloop1.py

Download: :download:`GTK+ Main Loop 1 <_examples/gtkmainloop1.py>`

After the ``HelloWorld()`` class has run, the application loops in the ``Gtk.main()`` line of code. This loop waits for an event in the application to occur such as a click, drag-and-drop, or any other number of events.

A Python application can either work as standalone or part of another application. However, if the application is being used as part of another, the GTK+ Main Loop position will cause a problem as it stands. Therefore, we only need to allow the Main Loop to run if the application is running standalone. We will need to change the code to the following:

.. literalinclude:: _examples/gtkmainloop2.py

Download: :download:`GTK+ Main Loop 2 <_examples/gtkmainloop2.py>`
