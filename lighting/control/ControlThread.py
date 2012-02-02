from threading import Thread

__author__ = 'Pevner'

class ControlThread(Thread):
    def __init__(self, lighting_thread):
        super(ControlThread, self).__init__()
        self.lighting_thread = lighting_thread

    def acceptable_command(self, command):
        raise NotImplementedError

    def deny_command(self, command):
        raise NotImplementedError

    def perform_command(self, command, args):
        raise NotImplementedError

    def get_input(self):
        raise NotImplementedError

    def run(self):
        while True:
            input = self.get_input()
            command = input[0]
            if self.acceptable_command(command):
                self.perform_command(command, input[-0])
            else:
                self.deny_command(command)