from pygame import Rect
import pygame

from physics.Object import Object
from physics.Vector2D import Vector2D

class Body(Object):
    def __init__(self, screen, position: Vector2D = Vector2D(0,0), mass = 1):
        super().__init__(position, mass)
        self.screen = screen

    def update(self):
        self.updatePhysics()
        pygame.draw.rect(self.screen, 'blue', Rect(self.position.x,self.position.y, 20,20));
   