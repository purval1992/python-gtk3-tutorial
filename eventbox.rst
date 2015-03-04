EventBox
========
An EventBox is an invisible widget which can be used to detect events which occur within it. For example, it can be used to make a Label clickable.

===========
Constructor
===========
The EventBox can be constructed using the following::

  eventbox = Gtk.EventBox()

=======
Methods
=======
A child widget should be added to the EventBox with::

  eventbox.add(child)

Child widgets can also be removed by calling::

  eventbox.remove(child)

In some cases, it may be necessary to configure the position of the EventBox relative to the child.

  eventbox.set_above_child(above_child)

If *above_child* is ``True``, the EventBox will receive all input. When set to the ``False``, the EventBox will receive events after they have gone to the child widget.

=======
Signals
=======
The EventBox can take a large number of events with the most common being::

  "event"
  "button-press-event"
  "button-release-event"
  "scroll-event"
  "query-tooltip"
  "show"
  "hide"
  "enter-notify-event"
  "leave-notify-event"

=======
Example
=======
Below is an example of an EventBox:

.. literalinclude:: _examples/eventbox.py

Download: :download:`EventBox <_examples/eventbox.py>`
