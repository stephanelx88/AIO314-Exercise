# Question 2:

import torch
import torch.nn as nn

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

assert round(output[-1].item(), 2) == 0.26
print(output)
# Q2: B