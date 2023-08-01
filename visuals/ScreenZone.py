import pygame

class Text:
    def __init__(self,text,position):
        self.position = position;
        self.string = text

class TextRenderer():
    def __init__(self, screen,fontSize):
        self.screen = screen
        self.texts = []
        self.positions = []
        self.font = pygame.font.Font(None, fontSize)

    def addText(self, string, position):
        self.texts.append(Text(self.font.render(string, True, (255, 255, 255)), position));

    def render(self):
        for text in self.texts:
            self.screen.blit(text.string, text.position)
        
        self.texts = []
        self.positions = []

class Screen():
    def __init__(self, dimensions):
        self.surface = pygame.Surface(dimensions)
        self.textRenderer = TextRenderer(self.surface, 30);



    # velX = font.render("VelX: {:.2f}".format(baloon.velocity.x,baloon.velocity.y), True, (255, 255, 255))  # White text
    # acceleration = font.render("AccX: {:.2f}  AccY: {:.2f}".format(baloon.acceleration.x,baloon.acceleration.y), True, (255, 255, 255))  # White text
    # targetError = font.render("errX: {:.2f}  errY: {:.2f}  total: {:.2f}".format(targetErrX,targetErrY,errSum), True, (255, 255, 255))  # White text
    
    # baloon.update()

    # neuralNetworkText = font.render("NN Visualizer", True, (255, 255, 255))  # White text

    # # Blit (draw) text surfaces on the mini-screens
    # playgroundScreen.blit(playgroundText, (10, 10))
