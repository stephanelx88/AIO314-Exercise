# Question 3:

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
        


data = torch.Tensor([1, 2, 300000000])
my_soft_max = MySoftMax()
output = my_soft_max(data)
assert math.isclose((output[0].item()), 0.0) == True
print(output)

# Q3: C