
import sys

import pygame

class Keys:
	"""overall overall class to mange screen behaviour"""
	def __init__(self):
		"""initializes class and creates its resource"""
		pygame.init()
		self.screen = pygame.display.set_mode((600,600))
		self.bg_color = (220,220,220)
		pygame.display.set_caption("Keys")


	def run_keys(self):
		"""starts the main loop"""
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					print(event.key)

			self.screen.fill(self.bg_color)
			pygame.display.flip()

if __name__ == '__main__':
	key = Keys()
	key.run_keys()
