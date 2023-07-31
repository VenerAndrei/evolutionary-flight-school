import pygame
import numpy as np
from models.Baloon import Body
from models.NeuralNetwork import NeuralNetwork
from physics.Vector2D import Vector2D
from visuals.NeuralNetworkVisualizer import NeuralNetVisualizer

clock = pygame.time.Clock()
running = True

nn = NeuralNetwork(2,3);
nnVisualizer = NeuralNetVisualizer(nn)
for l in range(len(nn.layers)):
    print(nn.layers[l].weights.shape)
    
nn.feedforward(np.array([[0],[0]]));
print(nn.outputValues);

import pygame
import sys

# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
running = True

# Screen dimensions
WIDTH, HEIGHT = 1600, 900

# Mini-screen dimensions

# Create the main screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neural Network using Genetic Algorithms for optimization")

# Create mini-screens (Surfaces)
playgroundScreen = pygame.Surface((WIDTH//2, HEIGHT))
infoScreen = pygame.Surface((WIDTH//2, HEIGHT//2))
neuralNetworkScreen = pygame.Surface((WIDTH//2, HEIGHT//2))

# Create font object
font = pygame.font.Font(None, 36)  # None specifies the default font, 36 is the font size

#Baloon Object
baloon = Body(playgroundScreen,Vector2D(100,100));

v1 = Vector2D(2,2);
v2 = v1.getCopy()
v2 = v2 * -1;
print(v1 - v2)

# Main game loop
while running:
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:             
                    nn = NeuralNetwork(2,3)
                    print(nn.feedforward(np.array([[0],[0]])));
                    nnVisualizer = NeuralNetVisualizer(nn)
                if event.key == pygame.K_ESCAPE:
                     running = False
                if event.key == pygame.K_d:
                     baloon.applyForce(Vector2D(1,0))
                if event.key == pygame.K_a:
                     baloon.applyForce(Vector2D(-1,0))
                if event.key == pygame.K_w:
                     baloon.applyForce(Vector2D(0,-1))
                if event.key == pygame.K_s:
                     baloon.applyForce(Vector2D(0,1))
    # Clear the main screen with a white color
    screen.fill((255, 255, 255))

    # Clear mini-screens with different colors
    playgroundScreen.fill((255, 0, 0))  # Red
    infoScreen.fill((0, 0, 0))  # Green
    neuralNetworkScreen.fill((0, 0, 255))  # Blue
    
    # Air friction Direct proportional with speed
    baloon.applyForce(baloon.velocity*-0.01)

    # Gravity
    baloon.applyForce(Vector2D(0,1))
    if(baloon.position.y > HEIGHT - 20):
         baloon.velocity.y = -baloon.velocity.y
         
    # Render text on each mini-screen
    playgroundText = font.render("Playground", True, (255, 255, 255))  # White text

    velocity = font.render("VelX: {:.2f}  VelY: {:.2f}".format(baloon.velocity.x,baloon.velocity.y), True, (255, 255, 255))  # White text
    acceleration = font.render("AccX: {:.2f}  AccY: {:.2f}".format(baloon.acceleration.x,baloon.acceleration.y), True, (255, 255, 255))  # White text
    
    baloon.update()

    neuralNetworkText = font.render("NN Visualizer", True, (255, 255, 255))  # White text

    # Blit (draw) text surfaces on the mini-screens
    playgroundScreen.blit(playgroundText, (10, 10))
    infoScreen.blit(velocity, (10, 10))
    infoScreen.blit(acceleration, (10, 30))

    neuralNetworkScreen.blit(neuralNetworkText, (10, 10))
    # Draw the neural network
    nnVisualizer.update(neuralNetworkScreen)

    # Blit (draw) mini-screens on the main scree
    screen.blit(playgroundScreen, (0, 0))
    screen.blit(infoScreen, (WIDTH//2, 0))
    screen.blit(neuralNetworkScreen, (WIDTH//2, HEIGHT//2))

    # Update the display
    pygame.display.flip()
    clock.tick(60)  # limits FPS to 60

pygame.quit()
