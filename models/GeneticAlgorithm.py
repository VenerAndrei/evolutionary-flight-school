from typing import List, Dict

import numpy
from models.Baloon import Body
from models.NeuralNetwork import NeuralNetwork
from physics.Vector2D import Vector2D
WIDTH, HEIGHT = 1600, 900

def getNewBebeEliteBrains(population:List[Body]):
    eliteTop5 = population[:20]
    newBrains:List[NeuralNetwork] = []
    for parent1Idx,parent1 in enumerate(eliteTop5):
        for parent2Idx,parent2 in enumerate(eliteTop5):
            if parent1Idx != parent2Idx:
                brain = createChildrenBrain(parent1,parent2)
                newBrains.append(brain);
    return newBrains;

def createChildrenBrain(parent1: Body, parent2: Body):
    bebeBrain = crossover(parent1,parent2)
    bebeBrain = mutate(bebeBrain,0.1)
    return bebeBrain;

def crossover(parent1: Body, parent2: Body):
    childBrain = NeuralNetwork(4,4);
    for layerIndex,layer in enumerate(parent1.neuralNetwork.layers):
        for rowIdx in range(len(layer.weights)):
            for colIdx in range(len(layer.weights[0])):
                if numpy.random.rand() < 0.5:
                    childBrain.layers[layerIndex].weights[rowIdx][colIdx] = parent1.neuralNetwork.layers[layerIndex].weights[rowIdx][colIdx]
                else:
                    childBrain.layers[layerIndex].weights[rowIdx][colIdx] = parent2.neuralNetwork.layers[layerIndex].weights[rowIdx][colIdx]
       
        for biasIdx in range(len(layer.bias)):
            if numpy.random.rand() < 0.5:
                childBrain.layers[layerIndex].bias[biasIdx] = parent1.neuralNetwork.layers[layerIndex].bias[biasIdx] 
            else:
                childBrain.layers[layerIndex].bias[biasIdx] = parent2.neuralNetwork.layers[layerIndex].bias[biasIdx] 
    return childBrain
             
def mutate(brain:NeuralNetwork, mutationRate:float):
    for layerIndex,layer in enumerate(brain.layers):
        for rowIdx in range(len(layer.weights)):
            for colIdx in range(len(layer.weights[0])):
                if numpy.random.rand() < mutationRate:
                    brain.layers[layerIndex].weights[rowIdx][colIdx] = (numpy.random.rand() - 0.5) * 2

        for biasIdx in range(len(layer.bias)):
           if numpy.random.rand() < mutationRate:
                    brain.layers[layerIndex].bias[biasIdx] += (numpy.random.rand() - 0.5) * 2
    return brain

def nextGeneration(population:List[Body],surface):
    population.sort(key=lambda b: b.score)
    newBrains = getNewBebeEliteBrains(population)

    for brain in newBrains:
        population.pop()
        population.append(Body(surface, brain, Vector2D(WIDTH//4,HEIGHT-20)))

    for agent in population:
        agent.position.x = WIDTH//4 - 50;
        agent.position.y = HEIGHT-50;
        agent.velocity.x = 0;
        agent.velocity.y = 0;
        agent.neuralNetwork.feedforward([[0],[0],[0],[0]]);
        agent.score = 0;
    return population
    
