#!/usr/bin/env python

from time import sleep
from numpy import *
from LightingPattern import LightingPattern
from teh_display import *

N = 50
M = 24

class Color(LightingPattern):
    data = zeros([3 * N, M])
    sleep_time = 0

    def __init__(self, args):
        super(Color, self).__init__(args)
        if len(args) == 5:
            self.sleep_time = float(args[1])

        rgb = array([float(args[2]), float(args[3]), float(args[4])])
        for i in range(0, N):
            for j in range(0, M):
                for k in range(0, 3):
                    self.data[3 * i + k, j] = rgb[k]


    def display_pattern(self,t):
        teh_display(self.data)
        if self.sleep_time:
            sleep(self.sleep_time)
    

    
