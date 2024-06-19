# Question 4:
import torch
import torch.nn as nn
import math


class SoftMaxStable(nn.Module):
    def __init__(self):
        super().__init__()

    def forward(self, x):

        # Get max of tensor
        x_max = torch.max(x, dim=0, keepdims=True)
        x_exp = torch.exp(x - x_max.values)
        partition = x_exp.sum(0, keepdims=True)

        return x_exp / partition
    
if __name__=='__main__':
    data = torch.Tensor([1, 2, 3])
    softmax_stable = SoftMaxStable()
    output = softmax_stable(data)

    assert math.isclose(output[-1].item(), 0.6652409434318542) == True
    print(output)



# Q4: B