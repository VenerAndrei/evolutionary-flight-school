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
        self.outputValues = []

    def feedforward(self, input):
        output = input;
        self.outputValues = [];
        self.outputValues.append(output);
        for layer in self.layers:

            print('W:')
            print(layer.weights)

            print('I:')
            print(output)

            output = np.matmul(layer.weights,output);
            print('Out:')
            print(output)
            print('-----')
            # vecReLU = np.vectorize(ReLU)
            # output = vecReLU(output)
            vecSigmoid = np.vectorize(sigmoid)
            output = vecSigmoid(output)
            self.outputValues.append(output);

            #print(output)
        return output;
            
    

    