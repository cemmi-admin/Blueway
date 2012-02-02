Welcome to the CRUFT LABS LIGHTING FRAMEWORK!

Pevner's Introduction:
This body of code serves as a framework for programatically controlling the
LEDs once found at Cruft Labs.

I'm not going to pretend like I'm a smart enough person that I had some
overarching design goals that this framework magically fulfills.

I just didn't like running random python scripts, with little live control beyond bash.

Lighting should be more like DJing - something you can interact with freely,
using samples of lighting patterns that you can manipulate on the fly.

Moreover, with the existing stuff, I found inefficient, hard-to-read,
duplicated code,with little thought to extensible design or friendliness to
new users.

To make clear, I don't blame anyone - the shit worked, and it worked well for
its desired goals.  Any coder that pulls that off has earned his or her honor.

Heck, I'm not even going to pretend this stuff is even better -
it's a work-in-progress by a guy who doesn't know python, and mostly does
mathematical coding.

I just hope that it benefits from being heavily influenced by a strange mix of
java and functional design aesthetics, while keeping to the principles that
make pythonic libraries easy-to-use.

Actually, I really just hope that you have fun playing with lights.

-j.l.{pevner} (thepevner@gmail.com)


THE MODULES

O. lighting (main)
Example scripts and documentation live here.

I. core
Basic classes for creating and manipulating lighting patterns.

II. display
Tools for transforming data arrays representing displayable patterns into actual lighting commands.

III. patterns
Well-tested sample lighting patterns, including a sample composite lighting pattern.

IV. control
Threads and utilities for actually running, and controlling, lighting patterns.


TODO (not in order of priority):
Expand the documentation, including this document.
Expand the sample patterns to include all of those used in the original CruftLEDs (and more)
Significantly improve the control abilities of the control module - pausing, rewinding, etc
INPUT - extend this framework to be able to use input beyond time for the lighting patterns
OUTPUT - extend this framework to display to other lighting systems
(this requires a lot of care, mostly due to difficult performance and extensibility trade-offs)
TESTING TESTING TESTING!


Some advice from DMT on Good things to run:

python Quadratic.py Inf 1 1 1 1
this one does some cool fadey stuff

python CrazyColor.py Inf
this one does flashing colors

python TwinklePlusPlus.py Inf 10 100 0.5 0 0.8
Does a nice purple random-twinkle pattern.
0.5 0 0.8 are the RGB values for color

python RollerCoaster.py Inf
this does a white-light chase pattern down the length of the chain.

Pevner's note:
CrazyColor and RollerCoaster haven't been moved in yet.
But I'll totally do that soon.