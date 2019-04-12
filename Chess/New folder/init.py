import pygame
import numpy as np
import matplotlib.pyplot as plt

pygame.init()
gameDisplay=pygame.display.set_mode((800,800))
pygame.display.set_caption("Chess")
clock=pygame.time.Clock()

quitGame=False
chessBoard=np.zeros([8,8])
chessBoard[1::2,0::2]=1
chessBoard[0::2,1::2]=1
plt.imshow(chessBoard,cmap='binary')
gameDisplay=plt.show()

while not quitGame:



	for event in pygame.event.get():
			if event.type==pygame.QUIT:
				quitGame=True
				pygame.quit()
				quit()



	pygame.display.update()
	clock.tick(60)
pygame.quit()
quit()