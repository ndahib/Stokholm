import constants
import os

class Ransomwarer():
    def __init__(self, argv = None):
        self.args = argv
        self.target_dir = constants.TARGET_DIR


    def __open_target_directory(self):
        target_directory = self.target_dir
        if os.path.exists(target_directory) and os.path.isdir(target_directory):
            contents = os.listdir(target_directory)
            for item in contents:
                print(item)

    def execute(self):
        self.__open_target_directory
