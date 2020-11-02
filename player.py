x = 3
y = 3
def move(dir:str):
	global x
	global y
	if dir == 'north':
		if y == 0 or y == 9:
			pass
		else:
			y -= 1
	elif dir == 'south':
		if y == 0 or y == 9:
			pass
		else:
			y +=1
	elif dir == 'east':
		if x == 0 or x == 9:
			pass
		else:
			x += 1
	elif dir == 'west':
		if x == 0 or x == 9:
			pass
		else:
			x -=1
	else:
		pass