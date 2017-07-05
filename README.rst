juggo
=====

Series of experiments around the `Jug Problem`_. The Jug
Problem asks the following: you are given *n* jugs of varying
capacities, with no measuring marks, an infinite source of
water, and a ground where you can dispose of the water in
the jug(s). Find a series of operations (which all involve
either filling the jugs with the water source, pouring water
between jugs, or pouring water away), that will lead you to
achieve some target amount of water in some specific jug.

Generally the approach is to model the state of the jugs (the
amount of liquid currently stored inside them) as a vector.
There are a number of operations that can be performed on the
state vector, and these operations can be seen as a graph with
the edges being transitions between one state to another. A
BFS (which guarantees the shortest solution) is performed on
the graph and then the solution is plotted.

The classic die hard version:

- Initial: ``[0, 0]``
- Target:  ``[2, *]``
- Capacities: ``[4, 3]``

.. image:: images/graph3.png
   :width: 400px

- Initial: ``[0, 0, 0]``
- Target:  ``[2, 0, 0]``
- Capacities: ``[5, 4, 3]``

.. image:: images/graph.png

- Initial: ``[0, 0, 0]``
- Target:  ``[2, 1, 0]``
- Capacities: ``[5, 4, 3]``

.. image:: images/graph2.png


.. _`Jug Problem`: http://www.math.tamu.edu/~dallen/hollywood/diehard/diehard.htm
