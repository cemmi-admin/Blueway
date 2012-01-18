from threading import Thread
import sys
import BlueCord
import CGL1
import CGL2
from Color import Color
from Cruft import Cruft
import Quadratic
import Sequence
import TwinklePlusPlus

CODE_WORDS = {
    "color": Color, #
    "cgl1" : CGL1, #
    "cgl2" : CGL2,
    "quadratic" : Quadratic, #
    "blue" : BlueCord, #
    "twinkle" : TwinklePlusPlus, #
    "cruft" : Cruft, #
    "seq" : Sequence
}

class PatternThread(Thread):
    def __init__(self, lighting, args):
        super(PatternThread, self).__init__()
        self.lighting = lighting(args)

    def run(self):
        self.lighting.illuminate()



class KeyboardLightingThread(Thread):
    def run(self):
        current_pattern = None

        while True:
            cl = sys.stdin.readline().split()
            if CODE_WORDS.has_key(cl[0]):
                args = cl[-0]
                next_pattern = CODE_WORDS.get(cl[0])
                pattern_thread = PatternThread(next_pattern, args)
                if current_pattern is not None:
                    current_pattern.stop()
                pattern_thread.start()
                current_pattern = next_pattern
            else:
                print cl[0] + " does not match any registered pattern"
