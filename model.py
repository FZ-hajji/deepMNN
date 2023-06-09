# -*- coding: utf-8 -*-

import torch

class ResnetBlock(torch.nn.Module):
    """Define a Resnet block"""
    
    def __init__(self, dim,activation_fn):
        """Initialize the Resnet block"""
        
        super(ResnetBlock, self).__init__()

        self.block = self.build_resnet_block(dim,activation_fn)
        
    def build_resnet_block(self, dim,activation_fn):
        block = [torch.nn.Linear(dim, 2*dim),
                 torch.nn.BatchNorm1d(2*dim),
                 activation_fn()]

        block += [torch.nn.Linear(2*dim, dim),
                  torch.nn.BatchNorm1d(dim),
                  activation_fn()]

        return torch.nn.Sequential(*block)
    
    def forward(self, x):
        """Forward function (with skip connections)"""
        out = x + self.block(x)  # add skip connections
        return out
        

class Net(torch.nn.Module):
    def __init__(self, 
                 input_dim,
                 activation_fn,
                 n_blocks,
                 device):
        super(Net, self).__init__()
        
        model = []
        for i in range(n_blocks):  # add resnet blocks layers
            model += [ResnetBlock(input_dim,activation_fn)]
        self.model = torch.nn.Sequential(*model)
        self.model.to(device=device)
        
    def forward(self, input):
        """Forward function"""
        out = self.model(input)
        return out