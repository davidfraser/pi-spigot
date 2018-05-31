UCT Maths Mug
=============

[j5 International](https://j5int.com/) is a sponsor of the 
[UCT Mathematics Competition](http://www.mth.uct.ac.za/mam/outreach/competition/).

Prizewinners in 2018 received a mug with the competition logo, the j5 logo,
and a printout of the source code for a web page, written in HTML and Javascript.

If this HTML code and opened in a web browser, the web browser will begin computing
the digits of PI sequentially, and write them to the screen.

This repository contains the source code that was written on the mug, and some associated code.

Calculating the digits of PI sequentially
-----------------------------------------

π, defined as the ratio between the radius of a perfect circle and its circumference, is not
a rational number. So any decimal expansion of π is at best an approximation.

The advent of modern computers presented the opportunity for calculating the value of PI to
a previous implausible precision. Various algorithms have been developed; an interesting family
are known as [Spigot algorithms](https://en.wikipedia.org/wiki/Spigot_algorithm) because
they produce digits (in some base) sequentially.

* [calcpi.py](calcpi.py) is a Python example of a simple Spigot algorithm from [Rosetta Code](http://rosettacode.org/wiki/Pi#Python)
* [calcpi.js](calcpi.js) is a Javascript adaptation of this algorithm. As it stands it will not produce more than about 50 digits because of Javascript's internal numeric types
* [calcpibi.js](calcpibi.js) is a modification that has been adapted to use the [jsbn library](http://www-cs-students.stanford.edu/~tjw/jsbn/) for working with big integers in Javascript, and can continue to much higher degrees of precision
* [calcpi.html](calcpi.html) is a full HTML web page that can load in a browser and perform the required calculations to display PI
