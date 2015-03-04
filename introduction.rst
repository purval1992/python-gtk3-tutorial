Introduction
============

==========================
Before using this tutorial
==========================
Prior to working through this tutorial, it is recommended that you have a reasonable grasp of the Python programming language. GUI programming introduces new challenges compared to interacting with the command line. It is necessary for you to know how to create and run Python files, understand basic interpreter errors and warnings, work with strings, integers, floats, and Booleans. For the advanced widgets covered in this tutorial, good knowledge of lists and tuples will also be required.

Prior knowledge of GTK+ is not required.

===================
About this tutorial
===================
This guide assumes that you are using the Python 3.4 series and that you are using GTK+ 3.14 and an as-up-to-date version of Python-GObject as possible. The newer the Python-GObject version, the less likely there are to be issues. Older versions will work for some examples.

To see which version of GTK+ you have installed, run the following script to check the verison number.

Download: :download:`Version <_examples/version.py>`

===========
Deprecation
===========
Deprecation is the process of preparing features within software to be decommisioned and removed. GTK+ deprecates objects by providing warnings both in the GTK+ framework and documentation prior to removal at a later date. This allows developers to change their code before a feature is removed. In many cases however, a feature is not removed until the next major release to prevent mass breakage of applications.

Reasons for deprecation generally include a feature being superseded, or a feature no longer being widely used.

It is highly recommended to not use deprecated features of GTK+ or Python when developing applications, particularly when learning as they can cause problems when understanding other areas of development.

This tutorial does not cover widgets which have been marked as deprecated. Any widgets marked as deprecated by GTK+ in the future will also be removed from future versions of the tutorial.

=======
Credits
=======
The following people/teams deserve credit and provided me with the ability to write this tutorial:

* Guido van Rossum and other developers for creating and maintaining the Python programming language.
* The GTK+ developers for their excellent work on creating the toolkit.
* James Henstridge and other developers for their work on the PyGTK bindings.
* John Finlay, Rafaele Villar Burke and other maintainers of the original (and excellent) PyGTK tutorial.
* The Introspection binding authors.

=======
Contact
=======
Please contact me at andrew@andrewsteele.me.uk to report issues, bugs and provide comments. All suggestions are welcome.

=======
License
=======
* The tutorial text and code examples are released under a `CC0 1.0 Universal <http://creativecommons.org/publicdomain/zero/1.0/>`_ (CC0 1.0) license (this essentially makes them Public Domain).
* The GTK+ logo used for examples and the site favicon is released under the `Creative Commons Attribution-Share Alike 3.0 Unported <http://creativecommons.org/licenses/by-sa/3.0/deed.en>`_ license.
