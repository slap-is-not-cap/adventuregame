import random
import player
class Biomes:
	def __init__(self, name):
		print ('init')



def createArray(x, y):
	coords = []
	for i in range(0, x):
		coords.append([])
		for j in range(0, y):
			coords[i].append("*")
	return coords

def outputArray(coords):
	e = False
	x_size = len(coords)
	y_size = len(coords[0])
	for j in range(0, y_size):
		for i in range(0, x_size):
			if player.x == i:
				if player.y == j:
					print('p'+'   ', end = '')
					e = True

			else:
				if e == True:
					pass
				else:
					ch = coords[i][j]
					print(ch + "   ", end = '')
				e = False
		print("\n")	


def randomizeMap(coords,x,y):
	x_size = len(coords)
	y_size = len(coords[0])
	for j in range (0,y_size):
		for i in range(0,x_size):
			ch = coords[i][j]
			biomegen = random.randint(x,y)
			coords[i][j] = str(biomegen)
	
			
			