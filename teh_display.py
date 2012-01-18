
import colormap;
from display import *;

Ds = ['3','4','5','6','12','13','14','36','19','20','15','16'];
mapping = [11,10,7,5,2,1,3,4,13,16,15,14,9,12,8,6,24,23,21,22,18,20,17,19];
sockets = make_sockets(Ds);

def teh_displayi(data,CM=colormap.MATLAB_COLORMAP):
	imdisplayi(data,sockets,mapping,CM);

def teh_display(data):
	imdisplay(data,sockets,mapping);

