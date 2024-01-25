# CyberBlaze
CyberBlaze is a space simulator meant to run fully in the terminal

The project is fully open source and any additions welcomed!


To run the game, first make sure you have Python 3.0 or newer installed. 
Download the files and put them all into the same folder. 
On Windows, run cyberblaze.py in your terminal. On Linux, run Python3 cyberblaze.py

Current premise and what has been done:
1. Start a new game, buy a ship and send it on an expedition.


To Do:
1. Fix known bug with purchasing ships. Currently if you purchase a ship one of multiple things happens:
  1. First purchase of the first ship works. And credits are taken from the inventory as they should.
  2. Trying to purchase the first ship without the right amount of credits results in the call for "insufficient credits" works, but the ship is still added to inventory.
  3. Trying to purchase ship 2 or 3 results in the correct thing happening, ships can't be purchased.
  4. Selling items for more credits works, but you are unable to purchase ship 2 or 3 even with the correct amount of credits.


Future additions:
1. Make ships take damange from random events.
2. Make ships selectable in inventory so you can get a list of stats, make repairs, make upgrades.
3. Add a system for creating new items or upgrades from loot found on expeditions.
4. More random events.
