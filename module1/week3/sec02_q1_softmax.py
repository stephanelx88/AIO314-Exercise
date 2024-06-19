# Question 1:

import torch
import torch.nn as nn
import math

data = torch.Tensor([1, 2, 3])
softmax_function = nn.Softmax(dim=0)
output = softmax_function(data)

assert math.isclose(output[0].item(), 0.09) == True
print(output)

# Q1: C