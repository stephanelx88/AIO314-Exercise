import torch


class Softmax(torch.nn.Module):
    def __init__(self):
        super().__init__()


    def forward(self, x):
        x_exp = torch.exp(x)
        partition = x_exp.sum(0, keepdims=True)
        return x_exp / partition




if __name__ == '__main__':
    data = torch.Tensor([1, 2, 3])

    softmax_function = Softmax()
    output = softmax_function(data)
    print(output)