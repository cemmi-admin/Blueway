#!/usr/bin/env python
# 20 seconds is good
import os
from numpy import *
import time
from lighting.display.teh_display import *
from lighting.core import LightingPattern

THIS_DIR = os.path.dirname(__file__)
CRUFT = genfromtxt(os.path.join(THIS_DIR,'cruft.txt'),delimiter=',')

K = shape(CRUFT)[0]
N = 50
M = 24

class Cruft(LightingPattern):
    data = CRUFT

    def __init__(self, args):
        super(Cruft, self).__init__(args)

    def display_pattern(self,t):
        teh_displayi(1-self.data[0:N,:], colormap.WHITE_COLORMAP)
        time.sleep(0.05)
        sv = self.data[0,:]
        for j in range(0,K-1):
            self.data[j,:] = self.data[j+1,:]
            self.data[K-1,:] = sv