import os

class MainDirectory():
    
    def __init__(self, directory):
        self.directory = directory
        os.chdir(self.directory)
        