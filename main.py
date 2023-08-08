import pygame
from typing import List, Dict
from rich import print as rprint
import numpy as np
from models.Baloon import Body
from models.GeneticAlgorithm import getNewBebeEliteBrains, nextGeneration
from models.NeuralNetwork import NeuralNetwork
from physics.Vector2D import Vector2D
from visuals.NeuralNetworkVisualizer import NeuralNetVisualizer
from visuals.ScreenZone import Screen

# Screen dimensions
WIDTH, HEIGHT = 1600, 900
     
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
oldElitePopulaiton:List[Body] = []
elitePopulation:List[Body] = []
population:List[Body] = []


lastTime = 0
nowTime = 0
difTime = 0
generationNumber = 0
tournamentNumber = 0
maxTournaments = 5;

population = []

for _ in range(50):
    nn = NeuralNetwork(2,4);
    b = Body(playgroundScreen.surface, nn, Vector2D(WIDTH//4 - 50,HEIGHT-20));
    b.neuralNetwork.feedforward(np.array([[0],[0]]));
    population.append(b);

def areAlive(baloons):
    for b in baloons:
        if(b.alive):
            return True
    return False

while running:

    nowTime = pygame.time.get_ticks()
    difTime = nowTime - lastTime

    if difTime >= 7000 or not areAlive(population):
        
        top = []
        for b in population:
            if(b.alive):
                top.append(b);
            if(len(top) == 6): break

        brains = getNewBebeEliteBrains(top);
        
        population = []
        for b in brains:
            b.feedforward((np.array([[0],[0]])));
            population.append(Body(playgroundScreen.surface, b, Vector2D(WIDTH//4 - 50,HEIGHT-20)))

        for _ in range(20):
            nn = NeuralNetwork(2,4);
            b = Body(playgroundScreen.surface, nn, Vector2D(WIDTH//4 - 50,HEIGHT-20));
            b.neuralNetwork.feedforward(np.array([[0],[0]]));
            population.append(b);
            
        lastTime = nowTime;
        nnVisualizer = NeuralNetVisualizer(population[0].neuralNetwork)
        generationNumber += 1;

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
    population.sort(key=lambda x: x.score,reverse=True);
    for baloon in population:
        baloon.color = 'blue'
    population[0].color = 'black'
    nnVisualizer = NeuralNetVisualizer(population[0].neuralNetwork)

    for baloon in population:
        baloon.updateScore(target,difTime);
        baloon.think(target)
        baloon.update()
        baloon.draw()
    population[0].draw()
    pygame.draw.rect(playgroundScreen.surface,'red',pygame.rect.Rect(target.x,target.y,20,20));
    # Draw the neural network
    nnVisualizer.updateAndDraw(neuralNetworkScreen.surface)

    # playgroundScreen texts
    playgroundScreen.textRenderer.addText('playgroundScreen',(10,10));
    playgroundScreen.textRenderer.render()

    infoScreen.textRenderer.addText('__X: {:.2f}'.format(population[0].position.x),(10,10))
    infoScreen.textRenderer.addText('__Y: {:.2f}'.format(population[0].position.y),(200,10))

    infoScreen.textRenderer.addText('_dX: {:.2f}'.format(population[0].velocity.x),(10,30))
    infoScreen.textRenderer.addText('_dY: {:.2f}'.format(population[0].velocity.y),(200,30))

    infoScreen.textRenderer.addText('ddX: {:.2f}'.format(population[0].acceleration.x),(10,50))
    infoScreen.textRenderer.addText('ddY: {:.2f}'.format(population[0].acceleration.y),(200,50))

    infoScreen.textRenderer.addText('Best score: {:.2f}'.format(population[0].score),(10,100))
    infoScreen.textRenderer.addText('in[0][0]: {:.2f}'.format((target.x - population[0].position.x)/(WIDTH/2)),(10,130))
    infoScreen.textRenderer.addText('in[1][0] {:.2f}'.format((target.y - population[0].position.y)/HEIGHT),(10,160))
    infoScreen.textRenderer.addText('elapsed time: {:.2f} mins'.format(nowTime/60000),(10,190))
    infoScreen.textRenderer.addText('GENERATION: {}'.format(generationNumber),(10,250))
    infoScreen.textRenderer.addText('TOURNAMENT: {}'.format(tournamentNumber),(10,280))
    infoScreen.textRenderer.addText('BalPop: {}'.format(len(population)),(10,310))
    infoScreen.textRenderer.addText('ElitePop: {}'.format(len(elitePopulation)),(10,340))
    rprint(population[0].neuralNetwork.outputValues)


    infoScreen.textRenderer.render()

    # print(population[0].neuralNetwork.outputValues)
    # Blit (draw) mini-screens on the main screen
    #rprint(population[0].neuralNetwork.lastInput)
    screen.blit(playgroundScreen.surface, (0, 0))
    screen.blit(infoScreen.surface, (WIDTH//2, 0))
    screen.blit(neuralNetworkScreen.surface, (WIDTH//2, HEIGHT//2))

    #rprint(population[0].neuralNetwork.outputValues)

    pygame.display.flip()
    clock.tick(120) 

pygame.quit()
