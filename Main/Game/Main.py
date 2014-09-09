import pygame
from pygame.locals import *

from Colors import *

from Racquet import *

from AI import *

from Ball import *

from Arena import *

from Map import *

from Scoreboard import *
pygame.init()

p1_Banner = red
p2_Banner = blue

size = [700,600]
display = pygame.display.set_mode(size)
pygame.display.set_caption("PyPong")
clock = pygame.time.Clock()

player1 = Racquet(display,red,right)
player2 = ai_Racquet(display,blue,left)
ball1 = Ball(display,purple,center)
arena1 = Arena(display,lime_green)
scoreboard1 = Scoreboard(display,orange,p1_Banner,p2_Banner)

done = False
''' -------- Main Program Loop STARTS -------- '''
while done == False:
	display.fill(black)
	''' EVENT PROCESSING STARTS '''
	for event in pygame.event.get():
		if event.type == pygame.QUIT: # If user clicked close
			done = True # Flag that we are done so we exit this loop
	keys_held = pygame.key.get_pressed()
	if keys_held[K_UP]:
		player1.moveUp()
	if keys_held[K_DOWN]:
		player1.moveDown()
	if keys_held[ord('w')]:
		pass
		player2.moveUp()
	if keys_held[ord('s')]:
		pass
		player2.moveDown()
	''' EVENT PROCESSING ENDS '''
	''' GAME LOGIC STARTS '''
	''' BALL-WALL LOGIC STARTS '''
	if ball1.get_Pos()["y"] > 486 or ball1.get_Pos()["y"] < 16:
		ball1.bounce_backY()
	''' BALL-WALL LOGIC ENDS '''
	''' BALL-RACQUET COLLISION TESTING STARTS '''
	if (ball1.get_Pos()["x"] == player1.get_X()[1]) and (player1.get_Y()[1] <= ball1.get_Pos()["y"] <= player1.get_Y()[2]):
		ball1.bounce_backX()
	if (ball1.get_Pos()["x"] == player2.get_X()[2]) and (player2.get_Y()[1] <= ball1.get_Pos()["y"] <= player2.get_Y()[2]):
		ball1.bounce_backX()
	''' BALL-RACQUET COLLISION TESTING ENDS '''
	''' SCORING/SCOREBOARD LOGIC STARTS '''
	if ball1.get_Pos()["x"] > 686: #Player 2 scores
		scoreboard1.player2_Scores()
		ball1.score()
		ball1.bounce_backX()
	if ball1.get_Pos()["x"] < 16: #Player 1 scores
		scoreboard1.player1_Scores()
		ball1.score()
		ball1.bounce_backX()
	''' SCORING/SCOREBOARD LOGIC ENDS '''
	''' Game LOGIC ENDS '''
	''' DRAW CODE STARTS '''
	''' PLAYERS AND BALL '''
	ball1.create_Ball()
	player1.create_Racquet()
	player2.create_Racquet()
	''' GAME ARENA'''
	arena1.create_Arena()
	''' Scoreboard '''
	scoreboard1.create_Arena()
	''' AI '''
	player2.shadow()
	#player2.veil([ball1.get_Pos()["x"],ball1.get_Pos()["y"]])
	#player2.eclipse()
	''' SCREEN UPDATE STARTS '''
	scoreboard1.show_Scores()
	ball1.play_ball()
	pygame.display.flip()
	clock.tick(20)
	''' SCREEN UPDATE ENDS '''
''' -------- Main Program Loop Ends -------- '''
pygame.quit()
