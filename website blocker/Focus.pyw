# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 09:04:55 2020

@author: sanjayc

# This program will enable focus mode in PC by

1. Blocking webisites mentioned in the block.txt file
"""


import sys
from pathlib import Path
import os
from datetime import datetime as dt

cwd = Path.cwd()

sys.stdout = open(cwd / "logging.txt", 'a')



class Block():
    
    def __init__(self, block: int):
        if os.name != 'nt':
            print(str(dt.today()) + ": This program is for windows machine only")
            sys.exit(0)
'        self.status = int(block)
        self._hosts_file_path = Path("C:\Windows\System32\drivers\etc\hosts")
    
    def _read_text_file(self):
        # read the websites from the text file
        text_file_path = Path(cwd / "block_websites.txt")
        with open(text_file_path, 'r') as f:
            sites = f.readlines()
        
        return sites
            
    def execute(self):
        if self.status:
            print(str(dt.today()) + ": Enabling Focus Mode")
            
            block_sites = self._read_text_file()
            
            with open(self._hosts_file_path, 'a') as f:
                for ws in block_sites:
                    f.writelines("127.0.0.1\t" + ws)
                
        else:
            print(str(dt.today()) + ": Disabling Focus Mode")
            unblock_sites = self._read_text_file()
            
            with open(self._hosts_file_path, 'r+') as f:
                content = f.readlines()
                f.seek(0)
                for line in content:
                    
                    if not any(sites in line for sites in unblock_sites ):
                        f.write(line)
                f.truncate()
            
            

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("block argument missing")
    
    else:
        bl = Block(sys.argv[1])
        bl.execute()
    
    
