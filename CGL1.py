#!/usr/bin/env python

# Arguments:
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

import colorsys
from numpy import *
from LightingPattern import LightingPattern
from teh_display import *

N = 50
M = 24

dt = 0.002

class CGL1(LightingPattern):
    alpha = -1
    beta = -1.5
    speed = 1
    scale = 1
    omega = 0
    CM = colormap.MATLAB_COLORMAP
    data = 1j*zeros([N,M])
    field = 0.1*random.randn(N)

    def __init__(self, args):
        super(CGL1, self).__init__(args)
        if args > 1: self.alpha = float(args[1])
        if args > 2: self.beta = float(args[2])
        if args > 3: self.speed = float(args[3])
        if args > 4: self.scale = float(args[4])
        if args == 6:
            omega = float(args[5])
            if omega == -1: self.CM = 1 - colormap.MATLAB_COLORMAP
            else: self.omega = omega
        if args == 8: self.CM = colormap.solid_colormap(float(args[5]), float(args[6]), float(args[7]))


    #should data not be an argument?
    def dynamics(self, data):
        dA = 1j*zeros([N+2])
        dA[0] = data[N-1]
        dA[N] = data[0]
        dA[1:N+1] = data
        dA = convolve([1,-2,1],dA)
        dA = dA[2:N+2]
        data = data + self.dt * ((1 + self.alpha * 1j) * self.scale * dA + data - (1 + 1j * self.beta) * data * power(abs(data), 2))
        return data

    def display_pattern(self,t):
        for i in range(1,self.speed):
            self.field = self.dynamics(self.field)
        for i in range(1,M-1):
            self.data[:,i] = self.data[:,i-1]
        self.data[:,0] = self.field

        if self.omega:
            h = sin(self.omega*2*pi*t)
            s = sin(self.omega*sqrt(2.0)*pi*t)
            rgb = colorsys.hsv_to_rgb((h+1)/2,(s+1)/2,1)
            self.CM = colormap.solid_colormap(rgb[0],rgb[1],rgb[2])
        teh_displayi(real(self.data+1)/2,self.CM)


    


    

    
    
    
