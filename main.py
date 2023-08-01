import pygame
import numpy as np
from models.Baloon import Body
from models.NeuralNetwork import NeuralNetwork
from physics.Vector2D import Vector2D
from visuals.NeuralNetworkVisualizer import NeuralNetVisualizer
from visuals.ScreenZone import Screen

def baloonLogic(baloon):
    # Air friction Direct proportional with speed
    baloon.applyForce(baloon.velocity*-0.01)

    # Gravity
    baloon.applyForce(Vector2D(0,1))

    if(baloon.position.y > HEIGHT - 20):
         baloon.position.y = HEIGHT - 20
         baloon.velocity.y = -baloon.velocity.y

def clearScreens():
    screen.fill((255, 255, 255))
    playgroundScreen.surface.fill((100, 100, 100))
    infoScreen.surface.fill((0, 0, 0))
    neuralNetworkScreen.surface.fill((0, 0, 255)) 



# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
running = True

# Screen dimensions
WIDTH, HEIGHT = 1600, 900

# Create the main screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neural Network using Genetic Algorithms for optimization")

# Create mini-screens
playgroundScreen = Screen((WIDTH//2, HEIGHT))
infoScreen = Screen((WIDTH//2, HEIGHT//2))
neuralNetworkScreen = Screen((WIDTH//2, HEIGHT//2))

#Baloon Object
nn = NeuralNetwork(2,3);
baloon = Body(playgroundScreen.surface, nn, Vector2D(100,100));

nnVisualizer = NeuralNetVisualizer(baloon.neuralNetwork)
baloon.neuralNetwork.feedforward(np.array([[0],[0]]));

print(baloon.neuralNetwork.outputValues);
target = Vector2D(WIDTH//4,100);

errSum = 0
# Main game loop
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:             
                    nn = NeuralNetwork(2,3)
                    baloon.setNeuralNetwork(nn);
                    print(baloon.neuralNetwork.feedforward(np.array([[0],[0]])));
                    nnVisualizer = NeuralNetVisualizer(baloon.neuralNetwork)
                    baloon.position = Vector2D(100,100)
                    baloon.velocity = Vector2D(0,0)
                if event.key == pygame.K_ESCAPE:
                     running = False
                if event.key == pygame.K_d:
                     baloon.applyForce(Vector2D(5,0))
                if event.key == pygame.K_a:
                     baloon.applyForce(Vector2D(-5,0))
                if event.key == pygame.K_w:
                     baloon.applyForce(Vector2D(0,-5))
                if event.key == pygame.K_s:
                     baloon.applyForce(Vector2D(0,5))

    # Clear the main screen with a white color
    clearScreens()
    
    baloonLogic(baloon)

    baloon.update()
    baloon.draw()

    # Draw the neural network
    nnVisualizer.updateAndDraw(neuralNetworkScreen.surface)

    # playgroundScreen texts
    playgroundScreen.textRenderer.addText('playgroundScreen',(10,10));
    playgroundScreen.textRenderer.render()

    infoScreen.textRenderer.addText('__X: {:.2f}'.format(baloon.position.x),(10,10))
    infoScreen.textRenderer.addText('__Y: {:.2f}'.format(baloon.position.y),(200,10))

    infoScreen.textRenderer.addText('_dX: {:.2f}'.format(baloon.velocity.x),(10,30))
    infoScreen.textRenderer.addText('_dY: {:.2f}'.format(baloon.velocity.y),(200,30))

    infoScreen.textRenderer.addText('ddX: {:.2f}'.format(baloon.acceleration.x),(10,50))
    infoScreen.textRenderer.addText('ddY: {:.2f}'.format(baloon.acceleration.y),(200,50))
    infoScreen.textRenderer.render()

    # Blit (draw) mini-screens on the main screen
    screen.blit(playgroundScreen.surface, (0, 0))
    screen.blit(infoScreen.surface, (WIDTH//2, 0))
    screen.blit(neuralNetworkScreen.surface, (WIDTH//2, HEIGHT//2))

    pygame.display.flip()
    clock.tick(60) 

pygame.quit()
