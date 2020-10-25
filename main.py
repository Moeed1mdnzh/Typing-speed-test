import pygame
import board
import keyboard as kb
import threading
b = (board.Board(),board.Blit())


class Choice:
	###SEE IF THE PLAYER WANTS TO KEEP TYPING OR NOT
	def __init__(self,WPM):
		self.wpm = WPM
		self.fonts = [pygame.font.SysFont("arial",25),pygame.font.SysFont("arial",60)]
		self.texts = [self.fonts[0].render("R-Replay        Q-QUIT",True,(230,230,230)),
		self.fonts[1].render("WPM : %s"%self.wpm,True,(240,240,240))]
		self.stay = True
	def getChoice(self):
		global b
		while self.stay:
			b[0].board.blit(self.texts[0],(300,300))
			b[0].board.blit(self.texts[1],(290,150))
			if self.replay():
				b = (board.Board(),board.Blit())
				keys()
				t = type()
				t.show()
			elif self.Quit():
				self.stay = False
			self.keep_Screen()
			self.update()
			b[0].board.fill((20,20,20))
	def update(self):
		pygame.display.update()
	def replay(self):
		if pygame.key.get_pressed()[pygame.K_r]:
			return True
	def Quit(self):
		if pygame.key.get_pressed()[pygame.K_q]:
			return True
	def keep_Screen(self):
		for event in pygame.event.get():
			if event == pygame.QUIT:
				pygame.quit()
				quit()





class keys:
	def __init__(self,key=kb.is_pressed):
		self.key = key
		self.c_time = 0
		self.font_size = 22
		self.size_limit = 30
		self.typed_words = ''
		self.font = pygame.font.SysFont("arial",self.font_size)
		self.color = (230,230,230)
		self.count = 0
		self.y = 370
		self.spaces = 0
		self.wpm = None
		self.end = False
		self.seconds = 0
		self.mins = 0
		self.limit = 1000
		self.wanted_to_quit = False
		self.sentence = b[1].blit()
	def Key_press(self,Thread,sentence):
		#keyboard input
		try:
			Thread.start()
			self.key = kb.is_pressed
			s = sentence[self.count]
			if s.isupper():
				if self.key(s.lower()):
					self.typed_words += s
					self.count += 1
			elif sentence[self.count] == ' ':
				if pygame.key.get_pressed()[pygame.K_SPACE]:
					self.typed_words += ' '
					self.count += 1
					self.spaces += 1
			elif not s.isupper(): 
				if self.key(s):
					self.typed_words += s
					self.count += 1
			if pygame.key.get_pressed()[pygame.K_q]:
				self.wanted_to_quit = True
				self.end = True
		except IndexError:
			self.WPM(self.time)
class type(keys):
	def WPM(self,seconds):
		#calculates the wpm
		self.wpm = (self.mins*60)+self.seconds
		self.wpm = str(int((self.spaces/self.wpm)*60))
		self.end = True
	def Time(self):
		#getting the time
		self.time = pygame.time.get_ticks()
		if self.time > self.limit:
			self.seconds += 1
			self.limit += 1000
		if self.seconds == 60:
			self.mins += 1
			self.seconds = 0
		return self.seconds,self.time

	def clean(self,Object):
		#cleaning the board
		Object.board.fill((20,20,20))
	def keep(self):
		#don't let the sentence go out of the box
		if len(self.typed_words) >= self.size_limit:
			self.font_size -= 2
			self.size_limit += 30
			self.font = pygame.font.SysFont("arial",self.font_size)
			self.y += 1
	def show(self):
		##################
		###start typing###
		##################
		global b
		while not self.end:
			self.Time()
			self.thread = threading.Thread(target=b[0].clock())
			self.Key_press(self.thread,self.sentence)
			b[1].blit()
			b[0].display(self.typed_words,(120,self.y),self.font,self.color)
			self.keep()
			b[0].quit()
			b[0].update()
			self.clean(b[0])
		if not self.wanted_to_quit:
			self.c = Choice(self.wpm)
			self.c.getChoice()



if __name__ == "__main__":
	k = keys()
	t = type()
	t.show()

