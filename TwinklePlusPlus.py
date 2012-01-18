#!/usr/bin/env python


# Arguments:
#
# Duration -- time to run in secs.
# Speed -- Fade rate for lights (they fade in then immediately out), 1-10 reas.
# Arrival Rate -- How quickly to add lights (1 is reasonable).
# 
#
# Then either:
#
# nothing: use WHITE colormap.
#
# R -- Red 
# G -- Green
# B -- Blue for solid colormap (default is Matlab).
#
# Or:
# omega -- Speed to rotate in hue / saturation.

import colorsys
from numpy import *
from LightingPattern import LightingPattern
from teh_display import *
from scipy.stats import poisson
from time import sleep as wakeup

N = 50
M = 24

class TwinklePlusPlus(LightingPattern):
    speed = 1
    mu = 1
    CM = colormap.solid_colormap(1,1,1)
    omega1 = -1


    data = 0.01*random.randn(N,M)
    d0 = zeros([N,M])

    def __init__(self, args):
        super(TwinklePlusPlus, self).__init__(args)

        if len(args) > 1 : self.speed = int(args[1])
        if len(args) > 2 : self.mu = float(args[2])
        if len(args) == 4:
            self.omega1 = float(args[3])
            self.omega2 = sqrt(2.0)*self.omega1
        if len(args) == 5:
            self.omega1 = float(args[3])
            self.omega2 = float(args[4])
        if len(args) == 7:
            self.CM = colormap.solid_colormap(float(args[3]),float(args[4]),float(args[5]))

        self.dt = self.speed*0.005

    def dynamics(self,data):
        dA = self.d0 - data
        data = data + self.dt*dA
        return data

    def display_pattern(self, t):
       if self.omega1 != -1:
          h = cos(self.omega1*2*pi*t)
          s = sin(self.omega2*pi*t+pi/2)
          rgb = colorsys.hsv_to_rgb((h+1)/2,(s+1)/2,1)
          self.CM = colormap.solid_colormap(rgb[0],rgb[1],rgb[2])
       teh_displayi(sin(self.data),self.CM)

       c = poisson.rvs(self.mu,size=1)
       for i in range(0,c):
          x = floor(N*random.rand())
          y = floor(M*random.rand())
          self.d0[x][y] += 3.14159265
    
       self.data = self.dynamics(self.data)
       wakeup(0.005)