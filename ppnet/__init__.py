__version__ = "0.1.0-dev"

import torch

def load_model(path):
    model = torch.load(path)
    return model

