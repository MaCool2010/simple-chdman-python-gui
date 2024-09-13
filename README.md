explanation of chd files here:
https://retropie.org.uk/docs/CHD-files/

the full chdman command is
chdman createdvd -i game.iso -o game.chd -hs 2048

use createdvd NOT createcd
needs -hs 2048 to work

this script assumes you have rom-tools installed on macos:
brew install rom-tools

not tested on Linux or Windows
