# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    __init__.py                                        :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: ndahib <ndahib@student.1337.ma>            +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/12/13 10:56:08 by ndahib            #+#    #+#              #
#    Updated: 2025/12/15 12:09:15 by ndahib           ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from argparse import ArgumentParser
import sys
import constants
from ransomwarer import Stockholm

class StokholmManager():
    def __init__(self, argv = None):
        self.argv = argv or sys.argv[:]
        self.prog_name = self.argv[0]
        if self.prog_name == "__main__.py":
            self.prog_name = "python -m stokholm"
        pass
    
    def __parse_args(self):
        parser = ArgumentParser(prog=self.prog_name, add_help=True)
        parser.description = "A small programm 'malware' exactly ransomware, that spread through a small portion of local files"
        parser.add_argument("-v",
                            "--version", 
                            action="version",
                            version=constants.VERSION,
                            help="show the version of the program.")
        parser.add_argument("-r", 
                            "--reverse", 
                            type=str, 
                            nargs="?",
                            help="reverse using the key entered as an argument to reverse the infection.")
        parser.add_argument("-s", "--silent",
                            action="store_true",
                            default=False, 
                            help="if this argument exists the programm does not show or produce any output during process")
        args = parser.parse_args(self.argv[1:])
        return parser, args
        
    def execute(self):
        parser, args = self.__parse_args()
            
        return args

def execute_from_command_line():
    stokholm_manager = StokholmManager(sys.argv)
    args = stokholm_manager.execute()
    stokholm_ransomware = Stockholm(args)
    stokholm_ransomware.execute()