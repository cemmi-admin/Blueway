from lighting.patterns import BlueCord, Color, CGL2, Cruft, CGL1, Quadratic, TwinklePlusPlus
from lighting.core import CompositePattern

PATTERN_COLLECTION = [
    Color([ 1, 0, 1, 1]),
    Color([ 1, 1, 0, 1]),
    Color([ 0, 1, 1, 1]),
    Color([ 0, 0, 1, 1]),
    Color([ 0, 1, 0, 1]),
    Color([ 1, 0, 0, 1]),
    CGL1([ 900, 2, -2, 10, 4, -1]),
    CGL1([ 900, 2, -2, 10, 1]),
    CGL1([ 900, 2, -2, 10, 1, -1]),
    Quadratic([ 300,]),
    Quadratic([ 300,]),
    BlueCord([900]),
    CGL2([ 900, 0,  -3, 10]),
    CGL2([ 900, 0,  -3, 2, 4]),
    CGL2([ 900, 0,  -3, 2, 0,.1]),
    CGL2([ 900, 0,  -3, 10, 0,.1]),
    CGL2([ 900, 0,  -3, 5, 1, 0,.05]),
    #These two failed in recent testing, unclear if this always occurs and why
    #CGL2([ 300, 2 -2, 20, 1, 1, 0, 0,]),
    #CGL2([ 900, 2 -2, 10, 1, 0, .2, 0, .2, 1]),
    CGL2([ 100, 10, 0, 40, 0,.1, 0,.05]),
    CGL2([ 900, 10, 0, .5, 40, 0,.1, 0,.05]),
    CGL2([ 300, 2 -2, 20, 1, 0, 1, 0,]),
    CGL2([ 300, 2 -2, 20, 4, 1, 0, 1]),
    TwinklePlusPlus([  900, 4, 5, 0,.05]),
    TwinklePlusPlus([  100, 4, 1, 0,.05]),
    TwinklePlusPlus([  300, 4, 10, 0,.05]),
    TwinklePlusPlus([  100, 100,  50, 1]),
    TwinklePlusPlus([  20, 100, 10, 0,.05]),
    Cruft([ 20])
]

class Sequence(CompositePattern):
    def __init__(self, args):
        super(Sequence, self).__init__(PATTERN_COLLECTION, args)
