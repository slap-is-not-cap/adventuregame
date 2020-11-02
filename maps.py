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
					print(str(ch) + "   ", end = '')
				e = False
		print("\n")	


def randomizeMap(coords:list,x:int,y:int):
	allow = True
	eCycle = False
	sCycle = False
	currentX = 0
	currentY = 0
	start = random.randint(x,y)
	coords[0][0] = start
	x_size = len(coords)
	y_size = len(coords[0])
	for j in range (0,y_size):
		for i in range(0,x_size):
			if allow == False:
				pass
			else:
				percent = random.randint(1,10)
			if eCycle == False:
				if percent == 6:
					if currentX+1 == 9 or currentX ==9:
						pass
					else:
						coords[currentY][currentX+1] = start
						eCycle = True
				else:
					if currentX+1 >= 9 or currentX >= 9:
						pass
					else:
						print (currentY)
						allow = False
						loc = random.randint(x,y)
						coords[currentY+1][currentX] = loc

			if sCycle == False:
				if percent == 6:
					if currentY == 9:
						pass
					else:
						coords[currentY][currentX-1] = start
				else:
					if currentX+1 == 9 or currentX ==9:
						pass
					else:
						if currentY+1 or currentY == 9:
							pass
						else:
							allow = False
							loc = random.randint(x,y)
							print('loc'+str(loc))
							coords[currentY][currentX+1] = loc
			#currentX +=1
			#currentY +=1

			#ch = coords[i][j]
			#biomegen = random.randint(x,y)
			#coords[i][j] = str(biomegen)
	
			
			