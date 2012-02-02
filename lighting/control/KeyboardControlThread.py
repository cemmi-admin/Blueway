import sys
from ControlThread import ControlThread
from lighting.patterns import *

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

class KeyboardControlThread(ControlThread):
    def acceptable_command(self, command):
        return CODE_WORDS.has_key(command)

    def deny_command(self, command):
        print command + " does not match any registered pattern"

    def perform_command(self, command, args):
        pattern = CODE_WORDS.get(command)(args)
        super.lighting_thread.swap_current_pattern(pattern)

    def get_input(self):
        return sys.stdin.readline().split()

