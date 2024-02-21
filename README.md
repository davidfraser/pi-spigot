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

* [A working version of the webpage](https://raw.githack.com/davidfraser/pi-spigot/pi-day-2020/pi-logo.html)
* [The source code for the webpage as printed on the mug](https://raw.githubusercontent.com/j5int/uct-maths-mug/pi-day-2020/pi-logo.html)
* [A vector graphic of the mug](uct-maths-mug-pi-day-2020.svg)

<img src="https://raw.githubusercontent.com/davidfraser/pi-spigot/pi-day-2020/uct-maths-mug-pi-day-2020.svg"/>

Or read on for more information and alternative versions...

Talk at UCT Maths Day
---------------------

The talk David did at the UCT maths day, entitled "Bytes of Pi" (the wit is due to Professor Christopher Gilmore),
is available in an iPython notebook [here](./talk-notes.ipynb). If you follow that link, github should render the
talk notes, and the Python code embedded within it, and show the diagrams and equations generated.

If you want to try out the code yourself, start by following the instructions in the [installation document](./installing.md).
This will allow you to modify any of the code and see what results you get.


Files used to generate the code on the mug
------------------------------------------

* [calcpi.py](calcpi.py) is a Python example of a simple Spigot algorithm from [Rosetta Code](http://rosettacode.org/wiki/Pi#Python)
* This in turn seems to be based on a Java implementation from [Max Hailperin](https://github.com/Max-Hailperin/PiScroll/blob/master/app/src/main/java/edu/gac/mcs/max/piscroll/PiSpigot.java)
* The original mathematical paper describing this algorithm and others is by [Jeremy Gibbons](http://www.cs.ox.ac.uk/people/jeremy.gibbons/publications/spigot.pdf);
  the algorithm is described at the top of page 2. 
* [calcpi.js](calcpi.js) is a Javascript adaptation of this algorithm. As it stands it will not produce more than about 50 digits because of Javascript's internal numeric types
* [calcpibi.js](calcpibi.js) is a modification that has been adapted to use the [jsbn library](http://www-cs-students.stanford.edu/~tjw/jsbn/) for working with big integers in Javascript, and can continue to much higher degrees of precision
* [calcpi.html](calcpi.html) is a full HTML web page that can load in a browser and perform the required calculations to display PI

### Producing an interestingly shaped program-web-page

The layout of the program, showing a circle with the π symbol inside it, was constructed as follows:

* Constructing the image of PI within a circle
  (first as an [SVG scalable vector image](pi-circle.svg), then exporting it to a [bitmap PNG image](./pi-circle.png)). 
* Converting that image to an ASCII layout using the [asciiart program](https://github.com/nodanaonlyzuul/asciiart),
  by running the instructions in [make-layout.sh](make-layout.sh)
* Taking the [calcpi.html](calcpi.html) webpage produced above, and compressing the javascript in it so variable names
  are shorter etc, as [calcpi-compressed.html](calcpi-compressed.html)
* Repeating the following steps until a desirable outcome was obtained:
  - Running a program [layout_code.py](layout_code.py) that takes the HTML source code
    and lays it out based on the text layout in [layout.txt](layout.txt)
  - The resulting code then doesn't work: words, tags and other significant parts of the program are split by spaces, etc, 
    and it no longer a valid HTML page or Javascript program
  - Adjusting both [layout.txt](layout.txt) and [calcpi-compressed.html](calcpi-compressed.html) repeatedly with techniques
    such as adding a layout character here or there, adding insignificant padding to the program,
    splitting variable and function names by changing `object.attribute` to `object['attribute']`, and then splitting
    attribute names as in `object['att'+'tri'+'bute']` to fit in with the short sequences required.
  - Testing that the resulting program both works and achieves the necessary layout.

