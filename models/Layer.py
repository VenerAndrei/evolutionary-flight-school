import numpy as np;

class Layer:

    def __init__(self, input:int , output:int):
        self.weights  = np.random.rand(output,input)
        self.bias = np.random.rand(output,1)

    def compute(self, input):
        return np.matmul(input,self.weights)
