from collections import deque
from threading import Thread

__author__ = 'Pevner'

class LightingThread(Thread):
    queued_patterns = deque()
    current_pattern = None
    end = False


    def __init__(self, patterns):
        super(LightingThread, self).__init__()
        self.queued_patterns.extend(patterns)

    def stop_current_pattern(self):
        if self.current_pattern is not None: self.current_pattern.stop()

    def stop(self):
        self.end = True

    def queue_pattern(self, pattern):
        self.queued_patterns.append(pattern)

    def swap_current_pattern(self, pattern):
        self.queued_patterns.appendLeft(pattern)
        self.stop_current_pattern()

    def run(self):
        while not self.end:
            if self.current_pattern is None:
                if not self.queued_patterns: continue
                self.current_pattern = self.queued_patterns.popleft()
            self.current_pattern.illuminate()





