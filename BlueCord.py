import scipy
from numpy import *
from LightingPattern import LightingPattern
from teh_display import *

__author__ = 'Pevner'

N = 50
M = 24
K = 3*N
class BlueCord(LightingPattern):
    data = zeros([K,M])

    def __init__(self, args):
        super(BlueCord, self).__init__(args)
        self.blue = len(args) < 2 | int(args[1]) != 0

        a = scipy.linspace(0, 2 * scipy.pi, K)
        q1 = scipy.sqrt(scipy.cos(a) ** 2)

        rgb = []

        for i in range(0,K):
            rgb.append([q1[i],q1[i],q1[i]])

        for i in range(0,N):
            for j in range(0,M):
                for k in range(0,3):
                    self.data[3*i+k,j] = rgb[i][k]

    def display_pattern(self,t):
        if self.blue:
            teh_display(self.data)

            sv = self.data[0:2,:]
            self.data[0:K-4,:] = self.data[3:K-1,:]
            self.data[K-3:K-1,:] = sv

        else:
            teh_display(self.data)
            sv = self.data[0:3,:]
            self.data[0:K-3,:] = self.data[3:K,:]
            self.data[K-3:K,:] = sv



