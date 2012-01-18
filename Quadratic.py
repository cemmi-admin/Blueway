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
from LightingPattern import LightingPattern
from teh_display import *
from time import sleep as wakeup

N = 50
M = 24
CM = 1-colormap.MATLAB_COLORMAP

class Quadratic(LightingPattern):
    theta = 0
    theta_array = [0]
    data = 1*random.randn(N,M)

    def __init__(self, args):
        super(Quadratic, self).__init__(args)
        X = zeros([N, M])
        Y = zeros([N, M])

        for i in range(0, N):
            X[i, :] = (i - (N / 2.0)) / (M / 2.0)
        for i in range(0, M):
            Y[:, i] = (i - (M / 2.0)) / (M / 2.0)

        X = reshape(X, [1, N * M])
        Y = reshape(Y, [1, N * M])
        self.G = concatenate((X, Y))


    def dynamics(self):
       dt = 0.1
       self.theta_array[0] += dt
       self.theta = self.theta_array[0]
       R = matrix([[cos(self.theta),-sin(self.theta)],[sin(self.theta),cos(self.theta)]])
       I = R*self.G
       V = matrix([1,-1])*(array(I)*array(I))
       data = reshape(V,[N,M])
       return data

    def display_pattern(self,t):
        teh_displayi((1+self.data/5)/2,CM)
        self.data = self.dynamics()
        wakeup(0.005)