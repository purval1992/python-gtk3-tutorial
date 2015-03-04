Getting Started
===============
To begin, the below is a simple example which creates a 200 pixel width by 200 pixel high window. You will not be able to close the window in the traditional way by clicking the X in the corner. Instead you will need to exit the process via kill command.

.. literalinclude:: _examples/gettingstarted.py

Download: :download:`Getting Started <_examples/gettingstarted.py>`

To run the application, open a terminal window and enter::

  python gettingstarted.py

Python files can be run as with a standard application by double-clicking on the file once it has been made executable.

Due to this example having no way to quit via the GUI, we need to use :kbd:`CONTROL+4` to exit. If you click on the X (close) button, you will notice that the terminal does not return to the prompt. The application at this point is still running and consuming CPU/RAM. Running applications from the terminal while developing can allow you to spot issues such as this (as well as see warnings/errors that may appear).

We will look at signals shortly and show how they can be connected to ensure the application works correctly.

===========
Hello World
===========
As with any programming tutorial, there needs to be a 'Hello World' example. We will build on the previous example to create an application that performs a function and produces an output.

.. literalinclude:: _examples/helloworld.py

Download: :download:`Hello World <_examples/helloworld.py>`

Once downloaded, open a terminal and run the application as with the previous example.

========
Comments
========
Comments in Python applications can be specified in two ways:

* Using a ``#`` to designate a single-line comment.
* Using ``'''`` to specify a block comment. The ``'''`` is used both at the beginning and end of the text to specify all text within becomes a comment.

In a number of text editors, commented code will turn a different colour.

It is highly recommended to use comments both when learning to remind yourself of a particular piece of code, and when developing in the future to both guide yourself and others who may utilise your code.
