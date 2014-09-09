import pygame 
from pygame.locals import *

from Colors import *

from Racquet import *

from Ball import *

from Map import *

class ai_Racquet(Racquet):
	def __init__(self,surface,color,position):
		Racquet.__init__(self,surface,color,position)
		self.mid = self.y1 + self.length
	''' AI MOVEMENT '''
	def moveTp(self,zone=[]):
		zone_Midpoint = zone[(len[zone]-1)/2]
		if self.y1 not in zone:
			self.change_Y *= 1.5
			if zone_Midpoint > self.mid: # The Ball is below the zone
				if self.change_Y < 0: # The Ball is moving toward the zone, no action needed
					pass
				else: # The Ball is moving away from the zone, reverse the direction
					self.change_Y *= -1
			else: # The Ball is above the zone
				if self.change_Y < 0: # The Ball is away from the zone, reverse direction
					self.change_Y *= -1
				else: # The Ball is moving toward the zone, no action needed
					pass
	def oscillate(self,t_Param = b_North[0],b_Param = b_South[len(b_South)-9],arena_Top = b_North[0],arena_Botom = b_South[len(b_South)-9]):
		self.moveDown()
		''' STAYING WITHIN BOUNDS OF THE ARENA & PASSED PARAMETERS '''
		if (self.y1 == arena_Top) or (self.y1 == arena_Botom):
			self.change_Y *= -1
		else:
			if self.y1 == t_Param:
				print "y1 is equal to top Parameter"	
				if self.change_Y < 0: # This condition is true if the racquet is moving up
					self.change_Y *= -1
				elif self.change_Y > 0: # This condition is true if the racquet is moving down
					pass				
			if self.y1 == b_Param:
				if self.change_Y < 0: # This condiditon is true if the racquet is moving up			
					pass
				elif self.change_Y > 0:
					self.change_Y *= -1
	''' LOW DIFFICULTY ''' # For the Easy difficulty the AI will move up and down with no pattern
	def shadow(self):
		self.oscillate()
	''' Medium DIFFICULTY ''' # For the Medium difficulty the AI will move to the region that the ball is in and oscillate (in respect to the y-axis) in that region
	def veil(self,coordinates):
		ball_X = coordinates[0]
		ball_Y = coordinates[1]
		if ball_X in b_West:
			if ball_Y in b_North:	# Ball is in the North-East Region
				if self.y1 not in b_North:
					pass
				self.oscillate(b_North[0],b_North[len(b_North)-9])
			elif ball_Y in b_South: # Ball is in the South-East Region
				if self.y1 not in b_South:
					pass
				self.oscillate(b_South[0],b_South[len(b_South)-9])
	''' Hard DIFFICULTY '''
	def eclipse(self,coordinates): # For the Hard difficulty the AI will act in the same manner as the Medium difficulty but 
		pass
	''' INSANE(WALL) DIFFICULTY ''' # For the Insane difficulty the AI will move to the exact position of the ball, but after a certain number of cycles the program will glitch itself allowing the player a small window of opportunity to score!! This mode is mostly for practicing as the AI will return most balls
