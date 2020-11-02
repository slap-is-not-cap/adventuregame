from gameloop import Gameloop
import json
import maps
import config

# - one off code (map config, controls config, etc)
#make map (plus random)
grid = maps.createArray(10,10)
maps.randomizeMap(grid,1,4)
maps.outputArray(grid)

playing = True

Gameloop.gameloop()





