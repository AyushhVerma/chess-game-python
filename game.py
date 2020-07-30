import pygame 
import time
import random

window_width,window_height=800,600

window=pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption('Snake game')
pygame.init()

font=pygame.font.SysFont('comicsansms',30)
font1=pygame.font.Font(None,40)
font2=pygame.font.SysFont('comicsansms',20)

white=(255,255,255)
green=(50,205,50)
black=(0,0,0)
red=(255,0,0)
FPS=20
movement=20

clock=pygame.time.Clock()

def message(msg,color,height=0):
	text=font.render(msg,True,color)
	msg=text.get_rect()
	msg.center=window_width/2,window_height/2+height
	window.blit(text,msg)
	pygame.display.update()

def _score_(score):
	msg=font.render("Score:%s"%score,True,black)
	window.blit(msg,[0,0])

def message_start(msg,color,height=0):
	text=font1.render(msg,True,color)
	msg=text.get_rect()
	msg.center=window_width/2,window_height/2+height
	window.blit(text,msg)
	pygame.display.update()

def  message_level(msg,color,height=0):
	text=font2.render(msg,True,color)
	msg=text.get_rect()
	msg.center=window_width/2,window_height/2+height
	window.blit(text,msg)
	pygame.display.update()

def snake(i,movement):
	pygame.draw.rect(window,green,[i[0],i[1],movement,movement])

def start():
	start_screen=True
	while start_screen:
		window.fill(white)
		message_start('Snake Game',green,-40)
		message_level('Press Space to play or Q to quit',green,10)
		for event in pygame.event.get():
			if event.type==pygame.KEYDOWN:
				if event.key == pygame.K_SPACE:
					start_screen=False
				elif event.key == pygame.K_q:
					pygame.quit()
					quit()
		clock.tick(15)

def game():
	snakehead=pygame.image.load('snake_sprite2.png')
	food=pygame.image.load('food_sprite.png')
	score=0
	img=snakehead
	lead_x,lead_y=window_width/2,window_height/2
	lead_x_change=lead_y_change=0
	play=True
	gameover=False	
	food_x=random.randrange(0,window_width-movement,movement)
	food_y=random.randrange(0,window_height-movement,movement)
	snake_len=1
	head=[]
	while play:
		window.fill(white)
		while gameover:
			message_start('GAME OVER',red,-25)
			message('your score:%s'%score,black,25)
			message_level('Press Space to play again Q to quit',green,70)
			for event in pygame.event.get():
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_SPACE:
						game()
					if event.key==pygame.K_q:
						pygame.quit()
						quit()
			clock.tick(10)
		for event in pygame.event.get():
		
			if event.type==pygame.QUIT:
				pygame.quit()
				quit()
		
			if event.type==pygame.KEYDOWN:
		
				if event.key==pygame.K_LEFT:
					img=pygame.transform.rotate(snakehead,90)
					lead_x_change=-movement
					lead_y_change=0
		
				elif event.key==pygame.K_RIGHT:
					img=pygame.transform.rotate(snakehead,270)
					lead_x_change=movement
					lead_y_change=0
		
				elif event.key==pygame.K_UP:
					img=snakehead
					lead_y_change=-movement
					lead_x_change=0
		
				elif event.key==pygame.K_DOWN:
					img=pygame.transform.rotate(snakehead,180)
					lead_y_change=movement
					lead_x_change=0
		
		lead_x+=lead_x_change
		lead_y+=lead_y_change
		
		if lead_x<0:
			lead_x=0;gameover=True
		if lead_x>=	window_width:
			lead_x=window_width-movement;gameover=True
		if lead_y<0:
			lead_y=0;gameover=True
		if lead_y>=window_height:
			lead_y=window_height-movement;gameover=True
		
		window.fill(white)
		
		pygame.draw.rect(window,red,[food_x,food_y,movement,movement])
		a=[]
		a.append(lead_x)
		a.append(lead_y)
		head.append(a)
		
		if len(head)>snake_len:
			del head[0]
		
		window.blit(img,(head[-1][0],head[-1][1]))
		window.blit(food,(food_x,food_y))
		for i in head[:-1]:
			if i ==a:
				gameover=True
			pygame.draw.rect(window,green,[i[0],i[1],movement,movement])
		pygame.display.update()
		
		if (lead_x==food_x) and (lead_y==food_y) or ([food_x,food_y] in head ):
			food_x=random.randrange(0,window_width-movement,movement)
			food_y=random.randrange(0,window_height-movement,movement)
			score+=10
			snake_len+=1
		_score_(score)
		pygame.display.flip()
		clock.tick(FPS)
start()
game()
