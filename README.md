This is a very simple gui for chdman, to convert .iso PlayStation games to .chd.


Theres a good explanation of chd files here:
https://retropie.org.uk/docs/CHD-files/

## Requirements 
Works on macOS, should work on Linux.

This script assumes you have [rom-tools](https://formulae.brew.sh/formula/rom-tools) and [Homebrew](https://formulae.brew.sh/) installed.


### some other things
the full chdman command is
chdman createdvd -i game.iso -o game.chd -hs 2048

use createdvd NOT createcd,
needs -hs 2048 to work


