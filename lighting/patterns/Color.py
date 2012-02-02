#!/usr/bin/env python

from time import sleep
from numpy import *
from lighting.display.teh_display import *
from lighting.core import LightingPattern

N = 50
M = 24

class Color(LightingPattern):
    data = zeros([3 * N, M])
    sleep_time = 0

    def __init__(self, args):
        super(Color, self).__init__(args)
        if len(args) == 5:
            #this was initially args[1], with the ones below it args[2], [3], [4] wtf?
            self.sleep_time = float(args[4])

        rgb = array([float(args[1]), float(args[2]), float(args[3])])
        for i in range(0, N):
            for j in range(0, M):
                for k in range(0, 3):
                    self.data[3 * i + k, j] = rgb[k]


    def display_pattern(self,t):
        teh_display(self.data)
        if self.sleep_time:
            sleep(self.sleep_time)
    

    
