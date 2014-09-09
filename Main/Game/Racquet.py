import pygame 
from pygame.locals import *

from Colors import *

class Racquet:
	def __init__(self, surface, color, position):
		self.layer = surface
		self.color = color
		self.x1 = position[0]
		self.y1 = position[1]
		self.width = position[2]
		self.length = position[3]
		self.change_Y = 5

	''' CREATING RACQUET '''
	def create_Racquet(self):
		self.coordinates = [self.x1,self.y1,self.width,self.length]
		pygame.draw.rect(self.layer,self.color,self.coordinates)
	''' RACQUET MOVEMENT '''
	def moveUp(self):
		self.y1 -= self.change_Y
		if self.y1 <= 16:
			self.y1 += self.change_Y
	def moveDown(self):
		self.y1 += self.change_Y
		if (self.y1+self.length) >= 486:
			self.y1 -= self.change_Y 
	''' RACQUET POSITION '''  
	def get_X(self):
		return {1 : self.x1, 2 : self.x1+self.width}
	def get_Y(self):
		return {1 : self.y1, 2 : self.y1+self.length}
