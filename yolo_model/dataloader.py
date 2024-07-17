import torch
from torch.utils.data import Dataset, DataLoader
from datasets import load_dataset


class DetectionDataset(Dataset):
    def __init__(self, images):
        super().__init__()
