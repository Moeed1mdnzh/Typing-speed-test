import pygame
import random
pygame.init()



class Board:
	def data(self):
		#our data
		self.texts  = {(100,250):"Bert worked in a factory for several years before he came to sesame street"
		,(190,250):"It was late on a typical Pacific Northwest Spring night"
		,(170,250):"I suspected at least one could be used as an emergency exit"
		,(60,250):"I noticed that the explosion seemed to have been centered on the door across the room"
		,(140,250):"The lionbird is a species of eagle which travels and huntsin prides"
		,(90,250):"They sang to him each morning and he interpreted their songs to his companions"
		,(250,250):"The fighter collapsed on to the dirt floor"
		,(110,250):"Heaving the greatest sigh in his entire existence as a sentient on this planet"
		,(170,250):"Last night I had the strangest dream I never dreamed before"
		,(170,250):"The three little pigs started to feel they needed a real home"
		,(80,250):"It was the wisest little pig that found the tracks of a big wolf in the neighbourhood"}
		self.sentence = random.choice([(100,250),(190,250),(170,250),(60,250),(140,250),(90,250)
			,(250,250),(110,250),(170,250),(170,250),(80,250)])
	def __init__(self,typetest="Typing Test",start="Start typing...",Q_text="Q-Quit",colors=(200,200,0)):
		self.board = pygame.display.set_mode((800,500))	
		self.fonts = [pygame.font.SysFont("arial",70,"light"),pygame.font.SysFont("arial",40)
		,pygame.font.SysFont("arial",22),pygame.font.SysFont("arial",22)]
		self.caption = pygame.display.set_caption(typetest)
		self.colors = colors
		self.data()
		self.xy_Box = [(100,350,600,70),(0,0,70,30)]
		self.thickness = [10,4]
		self.board.fill((20,20,20))
		self.cord,self.sentence = self.sentence,self.texts[self.sentence]
		self.xy_text = [(210,10),(320,290),(7,2),self.cord]
		self.texts =[typetest,start,Q_text,self.sentence]
		self.count = 0
	def boxes(self,color,x_y_w_h,thickness):
		#draws the boxes
		pygame.draw.rect(self.board,color,x_y_w_h,thickness)
	def display(self,text,xy,font,color):
		#draws the texts
		self.board.blit(font.render(text,True,color),xy)
	def update(self):
		#refresh the board
		pygame.display.update()
	def clock(self):
		#delay typing
		pygame.time.delay(50)
	def quit(self):
		#see if the person wants to quit
		for event in pygame.event.get():
			if event == pygame.QUIT:
				pygame.quit()
				quit()
class Blit(Board):
	def blit(self):
		#showing them
		for i in range(2):
			self.boxes(self.colors,self.xy_Box[i],self.thickness[i])
		for i in range(4):
			self.display(self.texts[i],self.xy_text[i],self.fonts[i],(190,190,190))
			if i == 3:
				return self.sentence


