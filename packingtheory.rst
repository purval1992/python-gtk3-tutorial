Packing Theory
==============
Our first 'Hello World' program only contains a single widget. However, in the real word we will require more than one widget per Window. For this purpose, we can use several different widgets to achieve the layout we want. The most commonly used are Box and Grid widgets. These are known as packing, or container widgets, and are invisible to the user. They are placed within a Window and each other to develop a complex interfaces.

For anybody who has used Microsoft Visual Studio, placing widgets in GTK+ (and virtually all other toolkits such as Qt, wx) is different. Microsoft products use a pixel-based system where the widget is dropped in place and adjusted to size as needed. GTK+ uses a packing-based method where widgets are placed in container widgets, and adjusted to the size they are allocated.

The learning curve of the packing-based method is arguably slightly higher, however it allows for rapid development and fluid interface design once the initial learning curve is overcome. People who have worked with HTML and CSS will find the GTK+ packing behaviour similar.

Due to the fluid nature of the packing system, when a container (such as a Window or Grid) is resized, the child content within it is adjusted to fit correctly. If the size is increased, the child content becomes bigger, regardless of what else is contained within. If it is shrunk, the child content becomes as small as possible.

Most widgets have a minimum size which is dependent on their content. For example, a Button can not be made smaller than its Label which means that attempting to make the Window surrounding the Button smaller than the Label within will fail.

================
Height-for-width
================
GTK+ uses a height-for-width system to manage the size to widgets. In the most basic term, the widget can adjust how much vertical space it requires based on the horizontal space it is allocated.

For example, a multi-line text label will shrink its parent widget as it requires fewer lines due to increased width.
