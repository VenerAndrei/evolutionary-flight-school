from models.Layer import Layer
import numpy as np
from typing import List
def ReLU(input):
    if input < 0: return 0
    return input

def sigmoid(input):
    return 1/(1+np.exp(-input))

class NeuralNetwork:
    def __init__(self,NoOfinput:int ,NoOfoutput:int):
        self.NoOfinput = NoOfinput;
        self.NoOfoutput = NoOfoutput;
        self.NoOfHiddenLayers = 2;
        self.layers:List[Layer] = [ Layer(NoOfinput,6), Layer(6,NoOfoutput)];
        self.outputValues = []
        self.lastInput = 0;

    def feedforward(self, input):
        self.lastInput = input;
        output = np.array(input);
        self.outputValues = [];
        self.outputValues.append(output);
        for layer in self.layers:

            output = np.matmul(layer.weights,output);
     
            vecReLU = np.vectorize(ReLU)
            output = vecReLU(output)
            # vecSigmoid = np.vectorize(sigmoid)
            # output = vecSigmoid(output)
            self.outputValues.append(output);

        return output;
    
    def save(self,name:str):
        f = open(name,"w")
        for layer in self.layers:
            for b in layer.bias:
                f.write(str(b) + '\n');
            for row in range(len(layer.weights)):
                for col in range(len(layer.weights[0])):
                    f.write(str(layer.weights[row][col]) + '\n');
        print("Dumped the small brain");
    
    def load(self,name:str):
        f = open(name,"r")
        for layer in self.layers:
            for idxBias in range(len(layer.bias)):
                layer.bias[idxBias] = float(f.readline())
            for row in range(len(layer.weights)):
                for col in range(len(layer.weights[0])):
                    layer.weights[row][col] = float(f.readline());
        print("Loaded the small brain!");