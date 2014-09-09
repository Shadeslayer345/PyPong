import pygame 
from pygame.locals import *

from Colors import *

class Arena:
	def __init__(self,surface,color):
		self.layer = surface
		self.color = color
		
	''' CREATING BORDERS '''
	def create_Left(self):
		pygame.draw.rect(self.layer,self.color,[0,0,10,499]) #Left Goal
	def create_Right(self):
		pygame.draw.rect(self.layer,self.color,[700,500,-10,-499]) #Right Goal
	def create_Top(self):
		pygame.draw.rect(self.layer,self.color,[700,0,-699,10]) #Top
	def create_Bottom(self):
		pygame.draw.rect(self.layer,self.color,[0,500,699,-10]) #Bottom
	def create_Arena(self):
		self.create_Left()
		self.create_Bottom()
		self.create_Right()
		self.create_Top()
