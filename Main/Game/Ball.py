import pygame 
from pygame.locals import *

from Colors import *

class Ball:
	def __init__(self, surface, color, position):
		self.layer = surface
		self.color = color
		self.init_X = position[0]
		self.init_Y = position[1]
		self.var_X = self.init_X
		self.var_Y = self.init_Y
		self.radius = position[2]
		self.width = position[3]
		self.change_X = 5
		self.change_Y = 5

	''' CREATING BALL '''
	def create_Ball(self):
		self.center = [self.var_X, self.var_Y]
		pygame.draw.circle(self.layer,self.color,self.center,self.radius,self.width)
	''' BALL MOVEMENT '''
	def play_ball(self,direction=1):
		self.var_X += self.change_X
		self.var_Y += self.change_Y
	def bounce_backX(self):
		self.change_X *= -1
	def bounce_backY(self):
		self.change_Y *= -1
	def score(self):
		self.var_X = self.init_X
		self.var_Y = self.init_Y
	''' BALL POSITION (CENTER) '''
	def get_Pos(self):
		return {"x" : self.var_X, "y" : self.var_Y}
	''' MANUAL CONTROL FUNCTIONS (DEBUGGING) '''
	def moveUp(self):
		self.var_Y -= self.change_Y
		if self.var_Y <= 16:
			self.var_Y += self.change_Y
	def moveDown(self):
		self.var_Y += self.change_Y
		if (self.var_Y+self.radius) >= 486:
			self.var_Y -= self.change_Y
	def moveLeft(self):
		self.var_X -= self.change_X
		if self.var_X <= 16:
			self.var_X += self.change_X
	def moveRight(self):
		self.var_X += self.change_X
		if (self.var_X+self.radius) >= 566:
			self.var_X -= self.change_X
