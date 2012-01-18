from numpy import *;

def load_colormap(file):
    return genfromtxt(file,delimiter=',');
    
MATLAB_COLORMAP = load_colormap('matlab.txt');
HSV_COLORMAP = load_colormap('hsv.txt');
LINES_COLORMAP = load_colormap('lines.txt');

# MATLAB_COLORMAP=zeros([64,3]);
# MATLAB_COLORMAP[24:39,0] = linspace(0,1,15);
# MATLAB_COLORMAP[39:55,0] = 1;
# MATLAB_COLORMAP[55:64,0] = linspace(1,0.5,9);

# MATLAB_COLORMAP[7:23,1] = linspace(0,1,16);
# MATLAB_COLORMAP[39:55,1] = linspace(1,0,16);
# MATLAB_COLORMAP[23:39,1] = 1;

# MATLAB_COLORMAP[0:8,2] = linspace(0.5625,1,8);
# MATLAB_COLORMAP[8:23,2] = 1;
# MATLAB_COLORMAP[23:39,2] = linspace(1,0,16);


BLUE_COLORMAP=zeros([64,3]);
BLUE_COLORMAP[0:64,2] = linspace(0,1,64);

RED_COLORMAP=zeros([64,3]);
RED_COLORMAP[0:64,0] = linspace(0,1,64);

GREEN_COLORMAP=zeros([64,3]);
GREEN_COLORMAP[0:64,1] = linspace(0,1,64);

WHITE_COLORMAP=ones([64,3]);
WHITE_COLORMAP[0:64,0] = linspace(0,1,64);
WHITE_COLORMAP[0:64,1] = linspace(0,1,64);
WHITE_COLORMAP[0:64,2] = linspace(0,1,64);

def solid_colormap(r,g,b):
    CM=ones([64,3]);
    CM[0:64,0] = r*linspace(0,1,64);
    CM[0:64,1] = g*linspace(0,1,64);
    CM[0:64,2] = b*linspace(0,1,64);
    return CM

def i2c(data,CM):
    output = zeros([len(data)*3]);
    for i in range(0,len(data)):
       d = int(floor(data[i]*63));
       if d > 62:
	d = 63;
       elif d < 0:
	d = 0;
       output[3*i] = CM[d,0];    
       output[3*i+1] = CM[d,1];    
       output[3*i+2] = CM[d,2];    
    return output

