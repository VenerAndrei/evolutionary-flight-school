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
        self.alive = True

    def update(self):
        # Air friction Direct proportional with speed
        self.applyForce(self.velocity*-0.01)

        if(self.position.y > HEIGHT - 20):
            self.position.y = HEIGHT - 20
            self.velocity.y = -self.velocity.y
            self.alive = False

        if(self.position.y < 0):
            self.position.y = 0
            self.velocity.y = -self.velocity.y
            self.alive = False

        if(self.position.x < 0):
            self.position.x = 0;
            self.velocity.x = -self.velocity.x
            self.alive = False


        if(self.position.x > WIDTH/2 - 20):
            self.position.x = WIDTH/2 - 20;
            self.velocity.x = -self.velocity.x
            self.alive = False
        
        if(self.alive):
            self.updatePhysics()

    def draw(self):
        if(self.alive):
            pygame.draw.rect(self.screen, self.color, Rect(self.position.x,self.position.y, 20,20));

    def updateScore(self, target:Vector2D,time ):
        if(self.alive):
            self.score += 1/((((target.x - self.position.x)/(WIDTH/2))**2 + ((target.y - self.position.y)/HEIGHT)**2)) + time*1.1;

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

    