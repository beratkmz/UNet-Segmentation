import os
from PIL import Image
from torch.utils.data.dataset import Dataset
from torchvision import transforms

class Dataset(Dataset):
    def __init__(self, root_path, test=False):
        self.root_path = root_path
        if test:
            self.images = sorted([root_path+"/manual_test/"+i for i in os.listdir(root_path+"/manual_test/")])
            self.masks = sorted([root_path+"/manual_test_mask/"+i for i in os.listdir(root_path+"/manual_test_mask/")])
        else:
            self.images = sorted([root_path+"/train/"+i for i in os.listdir(root_path+"/train/")])
            self.masks = sorted([root_path+"/train_mask/"+i for i in os.listdir(root_path+"/train_mask/")])
        self.transform = transforms.Compose([
            transforms.Resize((512,512)),
            transforms.ToTensor()])
    def __getitem__(self, index):
        img = Image.open(self.images[index]).convert("RGB")   
        mask = Image.open(self.masks[index]).convert("L")

        return self.transform(img), self.transform(mask)
    
    def __len__(self):
        return len(self.images)