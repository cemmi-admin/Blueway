#Put a way of making composite patterns here
from bisect import bisect_right
from LightingPattern import LightingPattern

class CompositePattern(LightingPattern):
    transition_times = list()
    transition_patterns = dict()
    cycle_duration = 0

    def __init__(self, lights, args):
        super(CompositePattern, self).__init__(args)

        duration = 0
        for light in lights:
            self.transition_times.append(duration)
            self.transition_patterns[duration] = light
            duration += light.duration
        self.cycle_duration = duration
        if not args: self.duration = duration

    def display_pattern(self,t):
        i = bisect_right(self.transition_times, t % self.cycle_duration)
        self.transition_patterns.get(self.transition_times[i-1]).pattern(t)