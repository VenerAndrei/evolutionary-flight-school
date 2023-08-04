import pygame
from typing import List, Dict
from rich import print as rprint
import numpy as np
from models.Baloon import Body
from models.GeneticAlgorithm import nextGeneration
from models.NeuralNetwork import NeuralNetwork
from physics.Vector2D import Vector2D
from visuals.NeuralNetworkVisualizer import NeuralNetVisualizer
from visuals.ScreenZone import Screen

# Screen dimensions
WIDTH, HEIGHT = 1600, 900
     
def baloonLogic(baloon:Body):

    # Air friction Direct proportional with speed
    baloon.applyForce(baloon.velocity*-0.01)

    # Gravity
    #baloon.applyForce(Vector2D(0,0.5))

    if(baloon.position.y > HEIGHT - 20):
        baloon.position.y = HEIGHT - 20
        baloon.velocity.y = -baloon.velocity.y
        baloon.score += 100;

    if(baloon.position.y < 0):
        baloon.position.y = 0
        baloon.velocity.y = -baloon.velocity.y
        baloon.score += 100;

    if(baloon.position.x < 0):
        baloon.position.x = 0;
        baloon.velocity.x = -baloon.velocity.x
        baloon.score += 100;

    if(baloon.position.x > WIDTH/2 - 20):
        baloon.position.x = WIDTH/2 - 20;
        baloon.velocity.x = -baloon.velocity.x
        baloon.score += 100;

def clearScreens():
    screen.fill((255, 255, 255))
    playgroundScreen.surface.fill((100, 100, 100))
    infoScreen.surface.fill((0, 0, 0))
    neuralNetworkScreen.surface.fill((0, 0, 255)) 



# Initialize Pygame
pygame.init()
clock = pygame.time.Clock()
running = True


# Create the main screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Neural Network using Genetic Algorithms for optimization")

# Create mini-screens
playgroundScreen = Screen((WIDTH//2, HEIGHT))
infoScreen = Screen((WIDTH//2, HEIGHT//2))
neuralNetworkScreen = Screen((WIDTH//2, HEIGHT//2))

#Baloon Object


target = Vector2D(WIDTH//4,HEIGHT//2);

errSum = 0
# Main game loop

baloonPopulation:List[Body] = []

for _ in range(500):

    nn = NeuralNetwork(4,4);
    b = Body(playgroundScreen.surface, nn, Vector2D(WIDTH//4,HEIGHT-20));
    b.neuralNetwork.feedforward(np.array([[0],[0],[0],[0]]));
    baloonPopulation.append(b);

lastTime = 0
nowTime = 0
difTime = 0
generationNumber = 0
while running:

    nowTime = pygame.time.get_ticks()
    difTime = nowTime - lastTime
    if(difTime >= 7000):
        lastTime = nowTime;
        nnVisualizer = NeuralNetVisualizer(baloonPopulation[0].neuralNetwork)
        rprint("------------------------")
        for idx,layer in enumerate(baloonPopulation[0].neuralNetwork.layers):
            rprint('Layer: {}'.format(idx));
            rprint(layer.weights)
            rprint('Bias')
            rprint(layer.bias)
        rprint("------------------------")

        baloonPopulation = nextGeneration(baloonPopulation, playgroundScreen.surface)
        generationNumber += 1
    

    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
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
    baloonPopulation.sort(key=lambda x: x.score);
    for baloon in baloonPopulation:
        baloon.color = 'blue'
    baloonPopulation[0].color = 'black'
    nnVisualizer = NeuralNetVisualizer(baloonPopulation[0].neuralNetwork)

    for baloon in baloonPopulation:

        baloonLogic(baloon)
        baloon.think(target)
        
        baloon.update()
        baloon.draw()
    pygame.draw.rect(playgroundScreen.surface,'red',pygame.rect.Rect(target.x,target.y,20,20));
    # Draw the neural network
    nnVisualizer.updateAndDraw(neuralNetworkScreen.surface)

    # playgroundScreen texts
    playgroundScreen.textRenderer.addText('playgroundScreen',(10,10));
    playgroundScreen.textRenderer.render()

    infoScreen.textRenderer.addText('__X: {:.2f}'.format(baloonPopulation[0].position.x),(10,10))
    infoScreen.textRenderer.addText('__Y: {:.2f}'.format(baloonPopulation[0].position.y),(200,10))

    infoScreen.textRenderer.addText('_dX: {:.2f}'.format(baloonPopulation[0].velocity.x),(10,30))
    infoScreen.textRenderer.addText('_dY: {:.2f}'.format(baloonPopulation[0].velocity.y),(200,30))

    infoScreen.textRenderer.addText('ddX: {:.2f}'.format(baloonPopulation[0].acceleration.x),(10,50))
    infoScreen.textRenderer.addText('ddY: {:.2f}'.format(baloonPopulation[0].acceleration.y),(200,50))

    infoScreen.textRenderer.addText('Best score: {:.2f}'.format(baloonPopulation[0].score),(10,100))
    infoScreen.textRenderer.addText('in[0][0]: {:.2f}'.format((target.x - baloonPopulation[0].position.x)/(WIDTH/2)),(10,130))
    infoScreen.textRenderer.addText('in[1][0] {:.2f}'.format((target.y - baloonPopulation[0].position.y)/HEIGHT),(10,160))
    infoScreen.textRenderer.addText('elapsed time: {:.2f} mins'.format(nowTime/60000),(10,190))
    infoScreen.textRenderer.addText('GENERATION: {}'.format(generationNumber),(10,250))

    infoScreen.textRenderer.render()

    # print(baloonPopulation[0].neuralNetwork.outputValues)
    # Blit (draw) mini-screens on the main screen
    #rprint(baloonPopulation[0].neuralNetwork.lastInput)
    screen.blit(playgroundScreen.surface, (0, 0))
    screen.blit(infoScreen.surface, (WIDTH//2, 0))
    screen.blit(neuralNetworkScreen.surface, (WIDTH//2, HEIGHT//2))

    #rprint(baloonPopulation[0].neuralNetwork.outputValues)

    pygame.display.flip()
    clock.tick(120) 

pygame.quit()
