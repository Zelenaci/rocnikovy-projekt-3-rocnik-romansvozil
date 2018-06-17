#!/usr/bin/python3
#made_by_roman
#2048

#imports
import random

#vytvareni pole (x,y)
def fillArray(x,y):
	array = []
	for i in range(0,y):
		array.append([0])
		for j in range(0,x - 1):
			array[i].append(0)
	return array


#pridani 2/4 do pole
def addBlock(array):
	x = whatIsXY(array)[0]
	y = whatIsXY(array)[1]
	null_array = []
	for i in range(0,y):
		for j in range(0,x):
			if array[i][j] == 0:
				null_array.append([i,j])
				pass
			else:
				pass
				
	random_point = null_array[random.randint(0,(len(null_array) - 1))] 
	array[random_point[0]][random_point[1]] = random.choice([2,4])
	return array

#pohyb, doleva
def move(array):
	x = whatIsXY(array)[0]
	y = whatIsXY(array)[1]
	continue_counter = False
	nonull_array = []
	new_array = []
	for i in range(0,y):
		nonull_array.append([])
		for j in range(0,x):
			if array[i][j] != 0:
				nonull_array[i].append([array[i][j],[i,j]])
	
	print(nonull_array)
	for q in range(0,len(nonull_array)):
		continue_counter = False
		new_array.append([])
		if len(nonull_array[q]) == 0:
			continue
		for w in range(0,len(nonull_array[q])):
			
			if continue_counter: 
				continue_counter = False
				continue
			try:
				if nonull_array[q][w][0] == nonull_array[q][w+1][0]:
					new_array[q].append(2 * nonull_array[q][w][0])
					continue_counter = True			
				else: 
					new_array[q].append(nonull_array[q][w][0])
			except:
					new_array[q].append(nonull_array[q][w][0])
				
	
	print(new_array)
	
	for q in range(0,len(new_array)):
		null_count = x - len(new_array[q])
		new_array[q].extend(null_count * [0])
	print(new_array)
		
	
	
	return
	

#zjisti sirku, vysku
def whatIsXY(array):
	y = len(array) 
	x = len(array[0])
	return [x,y]


array = fillArray(4,4)	
print(array)
#print(Whatis_x_y(array))
for _ in range(0,8):
	array = addBlock(array)

for i in range(0, len(array)):
	print(array[i])
	
print(whatIsXY(array))

move(array)

