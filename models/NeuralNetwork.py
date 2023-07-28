from models.Layer import Layer
import numpy as np

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
        self.layers = [ Layer(NoOfinput,5), Layer(5,5), Layer(5,NoOfoutput)];

    def feedforward(self, input):
        output = input;
        for layer in self.layers:
            output = np.matmul(layer.weights,output) + layer.bias;
            # vecReLU = np.vectorize(ReLU)
            # output = vecReLU(output)
            vecSigmoid = np.vectorize(sigmoid)
            output = vecSigmoid(output)
            print(output)
        return output;
            
    

    