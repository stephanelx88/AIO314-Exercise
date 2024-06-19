# Question 2:

import torch
import torch.nn as nn
import math

class MySoftMax(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdims=True)
        
        return x_exp / partition


data = torch.Tensor([5, 2, 4])
my_softmax = MySoftMax()
output = my_softmax(data)

assert math.isclose(output[-1].item(), 0.25949645042419434) == True
print(output)
# Q2: B