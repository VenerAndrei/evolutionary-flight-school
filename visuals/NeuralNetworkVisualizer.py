import random
from models.Layer import Layer
from models.NeuralNetwork import NeuralNetwork
import pygame;
circleDiameter = 25;
OFFSET_X = 100;
OFFSET_Y = 100;
class NeuronVisualizer:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value
        self.color = 'white';

    def draw(self, surface):
        pygame.draw.circle(surface,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),(self.x,self.y),circleDiameter/2);
    
    def updateValue(self, value):
        self.value = value


class LayerVisualizer:
    def __init__(self, layer: Layer):
        self.layer = layer
        self.neurons = []
        self.lines = []
    
class NeuralNetVisualizer:
    def __init__(self,neuralNet: NeuralNetwork):
        self.nn = neuralNet;
        self.network = []
    
    def update(self,surface):

        for inputNeuronIndex in range(self.nn.NoOfinput):
            self.network.append([]);
            self.network[0].append(NeuronVisualizer(OFFSET_X,OFFSET_Y + inputNeuronIndex*50,10));
            self.network[0][inputNeuronIndex].draw(surface);
        
        for layerIndex in range(len(self.nn.layers)):
            self.network.append([]);
            print('Layer Index: ' + str(layerIndex));
            for neuronIndex in range(self.nn.layers[layerIndex].weights.shape[0]):
                neuronPosX = OFFSET_X + (layerIndex + 1) * 100;
                neuronPosY = OFFSET_Y + neuronIndex * 50;
                self.network[layerIndex + 1].append(NeuronVisualizer(neuronPosX,neuronPosY,10));
                self.network[layerIndex + 1][neuronIndex].draw(surface);
                
                weightsOfNeuron = self.nn.layers[layerIndex].weights[neuronIndex];
                print(weightsOfNeuron)

                for lineIndex in range(len(weightsOfNeuron)):
                    start_pos = (neuronPosX,neuronPosY);
                    end_pos = (OFFSET_X + (layerIndex) * 100,OFFSET_Y + lineIndex * 50);
                    pygame.draw.line(surface, 'black', start_pos, end_pos, int(weightsOfNeuron[lineIndex]*10))
                # for lineIndex in range(self.nn.layers[layerIndex].weights[neuronIndex]):


    # def draw(self, surface):
    #     for layerIndex in range(len(self.network)):
    #         for neuronIndex in range (len(self.network[layerIndex])):
    #             self.network[layerIndex][neuronIndex].draw(surface);