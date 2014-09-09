import pygame 
from pygame.locals import *

from Colors import *

from Arena import *

class Scoreboard(Arena):
	def __init__(self,surface,color1,color2,color3):
		Arena.__init__(self,surface,color1)
		self.score_font = pygame.font.Font(None, 50)
		self.layer = surface
		self.p1_Score_Count = 0
		self.p1_Color = color2
		self.p2_Score_Count = 0
		self.p2_Color = color3
		self.p1_score = self.score_font.render(str(self.p1_Score_Count),1,red)
		self.p2_score = self.score_font.render(str(self.p2_Score_Count),1,blue)

	''' CREATING BORERS '''
	def create_Left(self):
		pygame.draw.rect(self.layer,self.color,[0,501,10,99]) #Left Border
	def create_Right(self):
		pygame.draw.rect(self.layer,self.color,[700,601,-10,-89]) #Right Border
	def create_Top(self):
		pygame.draw.rect(self.layer,self.color,[700,501,-699,10]) #Top Border
	def create_Bottom(self):
		pygame.draw.rect(self.layer,self.color,[0,590,699,10]) #Bottom Border
	def create_Divider(self):
		pygame.draw.rect(self.layer,self.color,[340,510,10,99]) # Dividing Border
	def create_Arena(self):
		self.create_Left()
		self.create_Bottom()
		self.create_Right()
		self.create_Top()
		self.create_Divider()
	''' CREATING & DISPLAYING SCORES '''
	def player1_Scores(self):
		self.p1_Score_Count += 1
		self.p1_score = self.score_font.render(str(self.p1_Score_Count),1,red)
	def player2_Scores(self):
		self.p2_Score_Count += 1
		self.p2_score = self.score_font.render(str(self.p2_Score_Count),1,blue)
	def show_Scores(self):
		self.layer.blit(self.p1_score,[170,530])
		self.layer.blit(self.p2_score,[525,530])