__author__ = 'Pevner'

from lighting.control import LightingThread,KeyboardControlThread
from lighting.patterns.Sequence import Sequence

#Create a thread for the lights to run in (the empty list means nothing is pre-queued)
lighting_thread = LightingThread([])
#supply that thread with a pattern (you could put in more, if you liked)
lighting_thread.queue_pattern(Sequence([]))
#attach a controller to that thread
control_thread = KeyboardControlThread(lighting_thread)
#if the lighting thread is dead, the controller probably shouldn't keep your program running
control_thread.daemon = False
#now, let's get those lights running
lighting_thread.start()
#and let's engage that controller
control_thread.start()
#and now you're having fun!

#try running some of the sample patterns by typing them in like it were a command-line, with their name and arguments

#to kill it - oh, haven't implemented that yet!


