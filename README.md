UCT Maths Mug 2019
==================

[j5 International](https://j5int.com/), now part of [Hexagon PPM](https://hexagonppm.com/) is a sponsor of the 
[UCT Mathematics Competition](http://www.uctmathscompetition.org.za/).

Prizewinners in 2019 received a mug with the competition logo, the Hexagon PPM and j5 logos,
and a representation of the *Fibonacci Spiral*.

![UCT Maths Competition 2019 Mug](./uct-maths-mug-2019.svg)

For more information on the Fibonacci Spiral, read on!
If you look carefully, you should also be able to spot a Fibonacci Spiral in the following video, which demonstrates the advantage of being part of a company named after a mathematical shape:

[![Hexagon. Shaping Smart Change.](http://img.youtube.com/vi/ieAvzoANvBI/0.jpg)](http://www.youtube.com/watch?v=ieAvzoANvBI "Hexagon. Shaping Smart Change")

For more information on previous mugs, please see:

* The [2018 mug](https://github.com/j5int/uct-maths-mug/blob/2018/README.md) which contained a program for calculating the digits of PI.

Fibonacci numbers
-----------------

High school mathematicians will hopefully have encountered the [Fibonacci numbers](https://en.wikipedia.org/wiki/Fibonacci_number) already.
These numbers form a sequence, starting with 0 and 1, where each number is the sum of the two preceding ones.
[The sequence is defined](https://artofproblemsolving.com/wiki/index.php/Fibonacci_sequence) as follows:

![F_0 = 0, F_1 = 1](https://latex.codecogs.com/svg.latex?F_0%20%3D%200%2C%20F_1%20%3D%201)

![F_n = F_{n-1} + F_{n-2}, \textup{ for } n > 1](https://latex.codecogs.com/svg.latex?F_n%20%3D%20F_%7Bn-1%7D%20%2B%20F_%7Bn-2%7D%2C%20%5Ctextup%7B%20for%20%7D%20n%20%3E%201)

(Often, the initial zero is omitted and the sequence starts with two 1s, but this makes no difference to the following terms).

The sequence starts with:

* (0), 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...

Fibonacci Spiral
----------------

The _Fibonacci Spiral_ is a geometric construction that starts with two squares of size one, alongside each other.
Each subsequent square is constructed on the side of the two previous squares, so that the length of its side is the same as the sum of the length of their sides.
In this way, the length of the sides of the squares exactly reproduces the Fibonacci sequence.

![Fibonacci Squares](fibonacci-squares.svg)

To generate the spiral, simply inscribe a circular arc in each square, with the center at the vertex of the square in common with the two subsequent squares,
and the arc going between the two closest vertices of the square.

![Fibonacci Spiral](fibonacci-spiral.svg)

Golden Ratios and Spirals
-------------------------

This spiral approximates the [Golden Spiral](https://en.wikipedia.org/wiki/Golden_spiral),
since the ratio between consecutive terms of the Fibonacci sequence tends towards the [Golden Ratio](https://en.wikipedia.org/wiki/Golden_ratio).

This can be seen through [Binet's formula](https://artofproblemsolving.com/wiki/index.php/Binet%27s_Formula) for the Fibonacci sequence:

![\phi = \frac {1 + \sqrt 5} {2}](https://latex.codecogs.com/svg.latex?%5Cphi%20%3D%20%5Cfrac%20%7B1%20%2B%20%5Csqrt%205%7D%20%7B2%7D)

![\psi = \frac {1 - \sqrt 5} {2}](https://latex.codecogs.com/svg.latex?%5Cpsi%20%3D%20%5Cfrac%20%7B1%20-%20%5Csqrt%205%7D%20%7B2%7D)

![F_n = \frac{\phi^n-\psi^n}{\sqrt 5}](https://latex.codecogs.com/svg.latex?F_n%20%3D%20%5Cfrac%7B%5Cphi%5En-%5Cpsi%5En%7D%7B%5Csqrt%205%7D)



