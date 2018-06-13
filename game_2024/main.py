#!/usr/bin/python3
#made_by_roman
#2024

#imports
from random import randint
pole = []

def fill_pole(pole,x,y):
	for i in range(0,y):
		pole.append([0])
		for j in range(0,x):
			pole[i].append(0)
	print(pole)


	
fill_pole(pole,4,4)
