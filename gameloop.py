import maps
import player
playing = True
class Gameloop:

	def gameloop():
		mapX=10
		mapY=10
		grid = maps.createArray(mapX,mapY)
		maps.randomizeMap(grid,1,4)

		while playing == True:
			maps.outputArray(grid)
			main = input('> ')
			if main == 'go east':
				player.move('east')
			elif main == 'go north':
				player.move('north')
			elif main == 'go south':
				player.move('south')
			elif main == 'go west':
				player.move('west')
		