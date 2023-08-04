import numpy as np;

class Layer:

    def __init__(self, input:int , output:int):
        self.weights  = (np.random.rand(output,input)-0.5)*2;
        self.bias = (np.random.rand(output,1)-0.5)*2

    def compute(self, input):
        return np.matmul(input,self.weights)
