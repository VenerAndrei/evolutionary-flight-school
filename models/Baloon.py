from pygame import Rect
import pygame
from models.NeuralNetwork import NeuralNetwork

from physics.Object import Object
from physics.Vector2D import Vector2D

class Body(Object):
    def __init__(self, screen, neuralNetwork:NeuralNetwork, position: Vector2D = Vector2D(0,0), mass = 1):
        super().__init__(position, mass)
        self.screen = screen
        self.neuralNetwork = neuralNetwork;

    def update(self):
        self.updatePhysics()

    def draw(self):
        pygame.draw.rect(self.screen, 'blue', Rect(self.position.x,self.position.y, 20,20));

    def setNeuralNetwork(self, neuralNetwork: NeuralNetwork):
        self.neuralNetwork = neuralNetwork;
