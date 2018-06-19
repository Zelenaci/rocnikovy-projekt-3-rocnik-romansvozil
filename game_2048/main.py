#!/usr/bin/python3
#made_by_roman
#2048

#imports
import random


#global
score = 0

#vytvareni pole (x,y)
def fillMatrix(x,y):
	matrix = []
	for i in range(0,y):
		matrix.append([])
		for j in range(0,x):
			matrix[i].append(0)
	return matrix


#pridani 2/4 do pole
def addBlock(matrix):
	x = whatIsXY(matrix)[0]
	y = whatIsXY(matrix)[1]
	null_matrix = []
	for i in range(0,y):
		for j in range(0,x):
			if matrix[i][j] == 0:
				null_matrix.append([i,j])
				pass

	random_point = null_matrix[random.randint(0,(len(null_matrix) - 1))] 
	matrix[random_point[0]][random_point[1]] = random.choice([2,4])
	return matrix

#zjisti zda je konec hry
def isEnd(matrix):
	for i in range(0,len(matrix)):
		for j in range(1,len(matrix[i]) - 1):
			if ((matrix[i][j] == matrix[i][j - 1]) or (matrix[i][j] == matrix[i][j + 1])):
				
				for k in range(1,len(matrix) - 1):
					for l in range(0,len(matrix[k])):
						if ((matrix[k][l] == matrix[k - 1][l]) or (matrix[k][l] == matrix[k + 1][l])):
							return[0,2]
				return [0,1]
				
	for i in range(1,len(matrix) - 1):
		for j in range(0,len(matrix[i])):
			if ((matrix[i][j] == matrix[i - 1][j]) or (matrix[i][j] == matrix[i + 1][j])):
				return [0,0]
	return [1]
					


#je plno?
def isFull(matrix):
	for i in range(0,len(matrix)):
		for j in range(0,len(matrix[i])):
			if matrix[i][j] == 0:
				return 0
			else: continue
	return 1
						
#pohyb, doleva
def moveLeft(matrix):
	global score
	x = whatIsXY(matrix)[0]
	y = whatIsXY(matrix)[1]
	continue_counter = False
	nonull_matrix = []
	new_matrix = []
	for i in range(0,y):
		nonull_matrix.append([])
		for j in range(0,x):
			if matrix[i][j] != 0:
				nonull_matrix[i].append(matrix[i][j])
	
	for q in range(0,len(nonull_matrix)):
		continue_counter = False
		new_matrix.append([])
		if len(nonull_matrix[q]) == 0:
			continue
		for w in range(0,len(nonull_matrix[q])):
			
			if continue_counter: 
				continue_counter = False
				continue
			try:
				if nonull_matrix[q][w] == nonull_matrix[q][w+1]:
					score += 2* nonull_matrix[q][w]
					new_matrix[q].append(2 * nonull_matrix[q][w])
					continue_counter = True			
				else: 
					new_matrix[q].append(nonull_matrix[q][w])
			except:
					new_matrix[q].append(nonull_matrix[q][w])
	
	for q in range(0,len(new_matrix)):
		null_count = x - len(new_matrix[q])
		new_matrix[q].extend(null_count * [0])
		
	return new_matrix



#smer pohybu
def move(matrix, vector):
	
	if vector == "l":
		return moveLeft(matrix)
		
	elif vector == "u":
		for _ in range(0,3):
			matrix = rotate(matrix)
		matrix = moveLeft(matrix)
		return rotate(matrix)
		
	elif vector == "r":
		for _ in range(0,2):
			matrix = rotate(matrix)
		matrix = moveLeft(matrix)
		for _ in range(0,2):
			matrix = rotate(matrix)
		return matrix
			
		
	elif vector == "d":
		matrix = rotate(matrix)
		matrix = moveLeft(matrix)
		for _ in range(0,3):
			matrix = rotate(matrix)
		return matrix	
			
	

#rotace pole
def rotate(matrix):
    matrix = list(zip(*matrix[::-1]))
    
    new_matrix = []
    for i in range(0, len(matrix)):
    	new_matrix.append([])
    	for j in range(0, len(matrix[i])):
    		new_matrix[i].append(matrix[i][j]) 
    		
    return new_matrix
	
	
	
#zjisti sirku, vysku
def whatIsXY(matrix):
	y = len(matrix) 
	x = len(matrix[0])
	return [x,y]


def main():
	global score
	vertical = horizontal = 1
	score = 0
	size = int(input("size: "))
	matrix = fillMatrix(size,size)
	
	while True:
		matrix = addBlock(matrix)
		
		for i in range(0,len(matrix)):
			print(matrix[i])
		
		print("SCORE: " + repr(score))	
		if isFull(matrix):
			if isEnd(matrix)[0]:
				print("Prohrál si se skórem: " + repr(score))
				exit(0)
			else:
				if isEnd(matrix)[1] == 1:
					vertical = 0
					horizontal = 1
				elif isEnd(matrix)[1] == 0:
					vertical = 1
					horizontal = 0
				else: vertical = horizontal = 1
		else: vertical = horizontal = 1
		while True:
			vector = input("\n")
			if (((vector == "r") or (vector == "l")) and horizontal):
				break
			elif (((vector == "u") or (vector == "d")) and vertical):
				break				
				
		matrix = move(matrix, vector)
		
main()
		
		
