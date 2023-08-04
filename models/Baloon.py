from numpy import sqrt
import numpy
from pygame import Rect
import pygame
from models.NeuralNetwork import NeuralNetwork

from physics.Object import Object
from physics.Vector2D import Vector2D
WIDTH, HEIGHT = 1600, 900

class Body(Object):
    def __init__(self, screen, neuralNetwork:NeuralNetwork, position: Vector2D = Vector2D(0,0), mass = 1):
        super().__init__(position, mass)
        self.screen = screen
        self.neuralNetwork = neuralNetwork;
        self.score = 0;
        self.color = 'blue'
    def update(self):
        self.updatePhysics()

    def draw(self):
        pygame.draw.rect(self.screen, self.color, Rect(self.position.x,self.position.y, 20,20));

    def setNeuralNetwork(self, neuralNetwork: NeuralNetwork):
        self.neuralNetwork = neuralNetwork;

    def think(self, target):
        
        # input = [
        #          [(target.x - self.position.x)/(WIDTH/2)],
        #          [(target.y - self.position.y)/HEIGHT],
        #          [target.x/(WIDTH/2)],
        #          [target.y/HEIGHT],
        #          [self.position.x/(WIDTH/2)],
        #          [self.position.y/HEIGHT],
        #          [self.velocity.x/3],
        #          [self.velocity.y/3]
        #          ]
        input = [
                 [(target.x - self.position.x)/(WIDTH/2)],
                 [(target.y - self.position.y)/HEIGHT],
                 [self.velocity.x/3],
                 [self.velocity.y/3]
                 ]
        out = self.neuralNetwork.feedforward(input);
        max = numpy.argmax(out);

        if max == 0:
            self.applyForce(Vector2D(0,-1));
        if max == 1:
            self.applyForce(Vector2D(0,1));
        if max == 2:
            self.applyForce(Vector2D(1,0));
        if max == 3:
            self.applyForce(Vector2D(-1,0));
        
        # self.applyForce(Vector2D(0,-out[0][0]));
        # self.applyForce(Vector2D(0,out[1][0]));
        # self.applyForce(Vector2D(out[2][0],0));
        # self.applyForce(Vector2D(-out[3][0],0));
        # print(out)
        self.score += ((target.x - self.position.x)**2 + (target.y - self.position.y)**2)/HEIGHT;
