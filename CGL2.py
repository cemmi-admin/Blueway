#!/usr/bin/env python



# Arugments:
#
# Duration -- time to run in secs.
# Alpha -- CGL parameter.
# Beta -- CGL parameter.
# Speed -- Larger means faster (1 is reasonable).
# Scale -- Larger means smoother (1 is reasonable). 
# 
#
# Then either:
#
# nothing: use MATLAB colormap.
#
# R -- Red 
# G -- Green
# B -- Blue for solid colormap (default is Matlab).
#
# Or:
# omega -- Speed to rotate in hue / saturation.

from numpy import *
from scipy.signal import correlate2d
from LightingPattern import LightingPattern
from teh_display import *
import colorsys
from time import sleep as wakeup

N = 50
M = 24

dt = 0.005

class CGL2(LightingPattern):
    alpha = -1
    beta = -1.5
    speed = 1
    scale = 1
    omega1 = -1
    CM = colormap.MATLAB_COLORMAP

    def __init__(self, args):
        super(CGL2, self).__init__(args)
        if len(args) > 1: self.alpha = float(args[1])
        if len(args) > 2: self.beta = float(args[2])
        if len(args) > 3: self.speed = int(args[3])
        if len(args) > 4: self.scale = float(args[4])
        if len(args) == 6:
            self.omega1 = float(args[5])
            self.omega2 = sqrt(2.0)*self.omega1
        if len(args) == 7:
            self.omega1 = float(args[5])
            self.omega2 = float(args[6])
        if len(args) == 8:
            self.CM = colormap.solid_colormap(float(args[5]),float(args[6]),float(args[7]))

        self.data = 1*random.randn(N,M)
    

    def dynamics(self, data, verbose=0):
       dA = correlate2d(data,array([[0,1,0],[1,-4,1],[0,1,0]]),boundary='wrap')
       dA = dA[1:N+1,1:M+1]
       if verbose: print(dA[0:5,0:5])
    
       data = data + dt*((1+self.alpha*1j)*self.scale*dA + data - (1+1j*self.beta)*data*power(abs(data),2));
       return data

    def display_pattern(self,t):
       if self.omega1 != -1:
          h = cos(self.omega1*2*pi*t)
          s = sin(self.omega2*pi*t+pi/2)
          rgb = colorsys.hsv_to_rgb((h+1)/2,(s+1)/2,1)
          self.CM = colormap.solid_colormap(rgb[0],rgb[1],rgb[2])
       teh_displayi(real(self.data+1)/2,self.CM)
       for i in range(0,self.speed):
         self.data = self.dynamics(self.data, self.scale)
       wakeup(0.005)