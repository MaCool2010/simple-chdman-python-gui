import subprocess
import os
from tkinter import filedialog
from tkinter import *
"""
explanation of chd files here:
https://retropie.org.uk/docs/CHD-files/

the full chdman command is
chdman createdvd -i game.iso -o game.chd -hs 2048

use createdvd NOT createcd
needs -hs 2048 to work

this script assumes you have rom-tools installed on macos:
brew install rom-tools

not tested on Linux or Windows

"""

# cd to a directory
root = Tk()
root.withdraw()
dir = filedialog.askdirectory()

os.chdir(dir)

while True:
  # get file name
  filename = str(input("file name (without extenstion): "))
  iso = filename + ".iso"
  chd = filename + ".chd"

  # run chdman command
  subprocess.Popen(f'chdman createdvd -i {iso} -o {chd} -hs 2048', shell=True)
  input("continue: ")

