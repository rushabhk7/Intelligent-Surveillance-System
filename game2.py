import random,pygame,sys
from pygame.locals import *
import numpy as np

WINDOWWIDTH = 1400
WINDOWHEIGHT = 1300
BOXSIZE = 100
GAPSIZE = 200


GRAY = (100, 100, 100)
NAVYBLUE = (60 ,60,100)
WHITE = (255,255,255)
RED = (255,0,0) 
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0) # walking value = 0
ORANGE = (255,128,0) #walking_down value = 1
PURPLE = (255,0,255) # walking_up value = 2 
CYAN = (0,255,255) # laying value = 3 
SILVER = (192,192,192) #standing  value = 4
TEAL = (0,128,128) #sitting value = 5


BGCOLOR = NAVYBLUE
BOXCOLOR = RED
LINECOLOR = GREEN
BOX_LENGTH = 100
BOX_WIDTH = 50
BOX1_TOP_LEFT_X = 300
BOX1_TOP_LEFT_Y = 150
BOX2_TOP_LEFT_X = 300
BOX2_TOP_LEFT_Y = 750
BOX3_TOP_LEFT_X = 900
BOX3_TOP_LEFT_Y = 150
BOX4_TOP_LEFT_X = 900
BOX4_TOP_LEFT_Y = 750
BOX1_CENTRE_X = 350
BOX1_CENTRE_Y = 175
BOX3_CENTRE_X = 350
BOX3_CENTRE_Y = 775
BOX2_CENTRE_X = 950
BOX2_CENTRE_Y = 175
BOX4_CENTRE_X = 950
BOX4_CENTRE_Y = 775

STATE_1 = -1
STATE_2 = -1
STATE_3 = -1
STATE_4 = -1
reached_1 = False
reached_2 = False
reached_3 = False
reached_4 = False

def main() :
	FPS = 50
	global fpsClock,DISPLAYSURF
	pygame.init()
	fpsClock = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT),0,32)
	

	test1 = np.loadtxt('test0.txt',delimiter=',')
	test2 = np.loadtxt('test1.txt',delimiter =',')
	test3 = np.loadtxt('test2.txt',delimiter=',')
	test4 = np.loadtxt('test3.txt',delimiter=',')
	pygame.display.set_caption('Surveillance System')
	
	test1 = test1.astype(int)
	test2 = test2.astype(int)
	test3 = test3.astype(int)
	test4 = test4.astype(int)	

	DISPLAYSURF.fill(BGCOLOR)
	TOTAL_TESTS = 2947
	test_case = 0	
	
	POS1_X = BOX1_CENTRE_X
	POS1_Y = BOX1_CENTRE_Y
	POS2_X = BOX2_CENTRE_X
	POS2_Y = BOX2_CENTRE_Y
	POS3_X = BOX3_CENTRE_X
	POS3_Y = BOX3_CENTRE_Y
	POS4_X = BOX4_CENTRE_X
	POS4_Y = BOX4_CENTRE_Y

#	test1 = [1,2,3,4]
#	test2 = [1,2,3,4]
#	test3 = [1,2,3,4]
#	test4 = [1,2,3,4]
	STATE_1 = test1[0]
	STATE_2 = test2[0]
	STATE_3 = test3[0]
	STATE_4 = test4[0]
#	print 1
#	print STATE_1	
	while test_case < TOTAL_TESTS :
	
		if(test_case > TOTAL_TESTS) :
			break
		draw_building(test_case)
		
		 
		POS1_X,POS1_Y,reached_1 = check_1(POS1_X,POS1_Y,STATE_1)
		POS2_X,POS2_Y,reached_2 = check_2(POS2_X,POS2_Y,STATE_2)
		POS3_X,POS3_Y,reached_3 = check_3(POS3_X,POS3_Y,STATE_3)
		POS4_X,POS4_Y,reached_4 = check_4(POS4_X,POS4_Y,STATE_4)
		print (reached_1)
		print (reached_2)
		
		
		if reached_1 and reached_2 and reached_2 and reached_4 :
			test_case += 1
			STATE_1 = test1[test_case]
			STATE_2 = test2[test_case]
			STATE_3 = test3[test_case]
			STATE_4 = test4[test_case]
			
			POS1_X = BOX1_CENTRE_X
			POS1_Y = BOX1_CENTRE_Y
			POS2_X = BOX2_CENTRE_X
			POS2_Y = BOX2_CENTRE_Y
			POS3_X = BOX3_CENTRE_X
			POS3_Y = BOX3_CENTRE_Y
			POS4_X = BOX4_CENTRE_X
			POS4_Y = BOX4_CENTRE_Y
		for event in pygame.event.get() :
			if event.type == QUIT :
				pygame.quit()
				sys.exit()
		pygame.display.update()
		fpsClock.tick(1000000000000)


def draw_building(test_case) :
	pygame.draw.rect(DISPLAYSURF,RED,(BOX1_TOP_LEFT_X,BOX1_TOP_LEFT_Y,BOX_LENGTH,BOX_WIDTH))
	pygame.draw.rect(DISPLAYSURF,RED,(BOX2_TOP_LEFT_X,BOX2_TOP_LEFT_Y,BOX_LENGTH,BOX_WIDTH))
	pygame.draw.rect(DISPLAYSURF,RED,(BOX3_TOP_LEFT_X,BOX3_TOP_LEFT_Y,BOX_LENGTH,BOX_WIDTH))
	pygame.draw.rect(DISPLAYSURF,RED,(BOX4_TOP_LEFT_X,BOX4_TOP_LEFT_Y,BOX_LENGTH,BOX_WIDTH))
#	pygame.draw.line(DISPLAYSURF,GREEN,(BOX1_TOP_LEFT_X +50 ,BOX1_TOP_LEFT_Y + 50),(BOX1_TOP_LEFT_X + 50,BOX2_TOP_LEFT_Y ),4)
#	pygame.draw.line(DISPLAYSURF,GREEN,(BOX1_TOP_LEFT_X + 100,BOX1_TOP_LEFT_Y + 25),(BOX2_TOP_LEFT_X , BOX1_TOP_LEFT_Y + 25),4)
#	pygame.draw.line(DISPLAYSURF,GREEN,(BOX3_TOP_LEFT_X + 50,BOX3_TOP_LEFT_Y + 50), (BOX4_TOP_LEFT_X + 50,BOX4_TOP_LEFT_Y ),4)
#	pygame.draw.line(DISPLAYSURF,GREEN,(BOX2_TOP_LEFT_X + 100,BOX2_TOP_LEFT_Y + 25), (BOX4_TOP_LEFT_X , BOX4_TOP_LEFT_Y + 25),4)
	pygame.draw.line(DISPLAYSURF,GREEN,(350,200),(350,750),4)
	pygame.draw.line(DISPLAYSURF,GREEN,(400,175),(900,175),4)
	pygame.draw.line(DISPLAYSURF,GREEN,(950,200),(950,750),4)
	pygame.draw.line(DISPLAYSURF,GREEN,(400,775),(900,775),4)
	fontObj = pygame.font.Font('freesansbold.ttf', 32)
	s = str(test_case +1)
	textSurfaceObj = fontObj.render(s, True, GREEN, BLUE)
	textRectObj = textSurfaceObj.get_rect()
	textRectObj.center = (200, 150)

def move_up(posx,posy) :
	posy -= 5
	return (posx,posy)

def move_down(posx,posy) :
	posy += 5
	return (posx,posy)
def move_right(posx,posy) :
	posx += 5
	return (posx,posy)
def move_left(posx,posy) :
	posx -= 5
	return (posx,posy)

def draw_circle(posx,posy,COLOR) :
	pygame.draw.circle(DISPLAYSURF,COLOR,(posx,posy),20,0)
	print (1)

def check_1(posx,posy,STATE_1) :	
	print (STATE_1)
	fpsClock.tick(1000000000000)
	if(STATE_1 == 0) :
		if(posx != BOX2_CENTRE_X) :
			posx,posy = move_right(posx,posy)
			draw_circle(posx,posy,YELLOW)
			print (False)
			return posx,posy,False
		else :	
			return posx,posy,True
	if(STATE_1 == 1) :
		print (posy)
		if(posy != BOX3_CENTRE_Y) :
			print (posx)
			print (False)
			posx,posy = move_down(posx,posy)
			draw_circle(posx,posy,ORANGE)
			return posx,posy,False
		else :
			return posx,posy,True
	if(STATE_1 == 2) :
		posx,posy = move_up(posx,posy)
		draw_circle(posx,posy,PURPLE)
		return posx,posy,True
	if(STATE_1 == 3) :
		draw_circle(posx,posy,CYAN)
		return posx,posy,True
	if(STATE_1 == 4) :
		draw_circle(posx,posy,SILVER)
		return posx,posy,True
	if(STATE_1 == 5) :
		draw_circle(posx,posy,TEAL)
		return posx,posy,True



	

def check_2(posx,posy,STATE_2):
	fpsClock.tick(1000000000000)
	if(STATE_2 == 0) :
		if(posx != BOX1_CENTRE_X) :
			posx,posy = move_left(posx,posy)
			draw_circle(posx,posy,YELLOW)
			return posx,posy,False
		else:
			return posx,posy,True
	if(STATE_2 == 1) :
		if(posy != BOX4_CENTRE_Y) :
			posx,posy = move_down(posx,posy)
			draw_circle(posx,posy,ORANGE)
			return posx,posy,False
		else:
			return posx,posy,True
	if(STATE_2 == 2) :
		posx,posy = move_up(posx,posy)
		draw_circle(posx,posy,PURPLE)
		return posx,posy,True
	if(STATE_2 == 3):
		draw_circle(posx,posy,CYAN)
		return posx,posy,True
	if(STATE_2 == 4) :
		draw_circle(posx,posy,SILVER)
		return posx,posy,True
	if(STATE_2 == 5) :	
		draw_circle(posx,posy,TEAL)
		return posx,posy,True

		
def check_3(posx,posy,STATE_3):
	fpsClock.tick(1000000000000)
	if(STATE_3 == 0) :
		if(posx != BOX1_CENTRE_X) :
			posx,posy = move_left(posx,posy)
			draw_circle(posx,posy,YELLOW)
			return posx,posy,False
		else:
			return posx,posy,True
	if(STATE_3 == 1) :
		posx,posy = move_down(posx,posy)
		draw_circle(posx,posy,ORANGE)
		return posx,posy,True
	if(STATE_3 == 2) :
		if(posy != BOX1_CENTRE_Y):
			posx,posy = move_up(posx,posy)
			draw_circle(posx,posy,PURPLE)
			return posx,posy,False
		else:
			return posx,posy,True
	if(STATE_3 == 3) :
		draw_circle(posx,posy,CYAN)
		return posx,posy,True
	if(STATE_3 ==4) :
		draw_circle(posx,posy,SILVER)
		return posx,posy,True
	if(STATE_3 ==5) :
		draw_circle(posx,posy,TEAL)	
		return posx,posy,True
	
		
def check_4(posx,posy,STATE_4):
	fpsClock.tick(1000000000000)
	if(STATE_4 == 0) :
		if(posx != BOX3_CENTRE_X) :
			posx,posy = move_left(posx,posy)
			draw_circle(posx,posy,YELLOW)
			return posx,posy,False
		else:
			return posx,posy,True
	if(STATE_4 == 1) :
		posx,posy = move_down(posx,posy)
		draw_circle(posx,posy,ORANGE)
		return posx,posy,True
	if(STATE_4 == 2) :	
		if(posy != BOX2_CENTRE_Y) :
			posx,posy = move_up(posx,posy)
			draw_circle(posx,posy,PURPLE)
			return posx,posy,False
		else :
			return posx,posy,True
	if(STATE_4 == 3) :
		draw_circle(posx,posy,CYAN)
		return posx,posy,True
	if(STATE_4 == 4) :
		draw_circle(posx,posy,SILVER)
		return posx,posy,True
	if(STATE_4 == 5) :
		draw_circle(posx,posy,TEAL)
		return posx,posy,True

	
def move_up(posx,posy) :
	posy -= 10
	return (posx,posy)

def move_down(posx,posy) :
	posy += 10
	return (posx,posy)

def move_right(posx,posy) :
	posx += 10
	return (posx,posy)

def move_left(posx,posy) :
	posx -= 10
	return (posx,posy)


if __name__ == '__main__':
	main()
