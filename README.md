UCT Maths "Pi Day" Mug
======================

[Hexagon PPM](https://hexagonppm.com/) is a sponsor of the 
[UCT Mathematics Competition](http://www.mth.uct.ac.za/mam/outreach/competition/),
and David Fraser from the Cape Town office presented at the UCT Mathematics Day
held on Saturday 14  March, 2020 - which is Pi Day in American date notation: 3.14.

Participants received a mug describing the day, and containing 
a printout of the source code for a web page, written in HTML and Javascript.

If this HTML code is opened in a web browser, the web browser will begin computing
the digits of PI sequentially, and write them to the screen.

(Former winners in the 1998 UCT Mathematics Competition in 1998 received a similar mug)
This repository contains the source code that was written on the mug, and some associated code.

You can view:

* [A working version of the webpage](https://cdn.rawgit.com/j5int/uct-maths-mug/pi-day-2020/pi-logo.html)
* [The source code for the webpage as printed on the mug](https://raw.githubusercontent.com/j5int/uct-maths-mug/pi-day-2020/pi-logo.html)

Or read on for more information and alternative versions...

Calculating the digits of PI sequentially
-----------------------------------------

π, defined as the ratio between the radius of a perfect circle and its circumference, is not
a rational number. So any decimal expansion of π is at best an approximation.

The advent of modern computers presented the opportunity for calculating the value of PI to
a previous implausible precision. Various algorithms have been developed; an interesting family
are known as [Spigot algorithms](https://en.wikipedia.org/wiki/Spigot_algorithm) because
they produce digits (in some base) sequentially.

* [calcpi.py](calcpi.py) is a Python example of a simple Spigot algorithm from [Rosetta Code](http://rosettacode.org/wiki/Pi#Python)
* This in turn seems to be based on a Java implementation from [Max Hailperin](https://github.com/Max-Hailperin/PiScroll/blob/master/app/src/main/java/edu/gac/mcs/max/piscroll/PiSpigot.java)
* The original mathematical paper describing this algorithm and others is by [Jeremy Gibbons](http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf);
  the algorithm is described at the top of page 2. 
* [calcpi.js](calcpi.js) is a Javascript adaptation of this algorithm. As it stands it will not produce more than about 50 digits because of Javascript's internal numeric types
* [calcpibi.js](calcpibi.js) is a modification that has been adapted to use the [jsbn library](http://www-cs-students.stanford.edu/~tjw/jsbn/) for working with big integers in Javascript, and can continue to much higher degrees of precision
* [calcpi.html](calcpi.html) is a full HTML web page that can load in a browser and perform the required calculations to display PI