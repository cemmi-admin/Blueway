#!/usr/bin/env python

import socket
import threading, Queue
import colormap;
from numpy import shape,zeros,minimum,maximum,ravel;

from socket import socket,AF_INET,SOCK_DGRAM

def connect(ip, port=6038):
   sock = socket(AF_INET, SOCK_DGRAM, 0)
   sock.connect((ip, port))
   return sock

def make_sockets(Ds):
    return [connect('10.32.0.{0}'.format(i)) for i in Ds];

def display(data, sock, chan=1):
   xmit = zeros(174, 'ubyte')
   xmit[:8], xmit[20:24] = [4, 1, 220, 74, 1, 0, 8, 1], [150, 0, 255, 15]
   xmit[16], xmit[24:] = chan, minimum(maximum(256 * ravel(data), 0), 255)
   sock.sendall(xmit)

def displayi(data,sock,chan=1,CM=colormap.MATLAB_COLORMAP):
   display(colormap.i2c(data,CM),sock,chan)

def imdisplay(data,socks,mapping):
   sz = len(socks);
   for i in range(0,sz):
     display(data[:,mapping[2*i]-1],socks[i],1)
     display(data[:,mapping[2*i+1]-1],socks[i],2)

def imdisplayi(data,socks,mapping,CM=colormap.MATLAB_COLORMAP):
   sz = len(socks);
   for i in range(0,sz):
     displayi(data[:,mapping[2*i]-1],socks[i],1,CM)
     displayi(data[:,mapping[2*i+1]-1],socks[i],2,CM)

