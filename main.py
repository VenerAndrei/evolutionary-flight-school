# import pygame
# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True
# rect = pygame.Rect(10,10,10,10);
# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("red")

#     # RENDER YOUR GAME HERE
#     pygame.draw.rect(screen, 'blue', rect, width=0)
#     rect = rect.move(1,1)
#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     clock.tick(60)  # limits FPS to 60

# pygame.quit()

from models.NeuralNetwork import NeuralNetwork
import numpy as np
nn = NeuralNetwork(5,4);
print(nn.feedforward(np.ones((5,1))));