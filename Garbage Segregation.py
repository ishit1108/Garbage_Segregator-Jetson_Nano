import os
import torch
import torchvision
from torch.utils.data import random_split
import torchvision.models as models
import torch.nn as nn
import torch.nn.functional as F
import cv2
model = torch.jit.load('C:/Users/ishit/Desktop/model_scripted.pt')
model.eval()
def predict_external_image(image_name):
    image = Image.open(image_name)

    example_image = transformations(image)
    plt.imshow(example_image.permute(1, 2, 0))
    print("The image resembles", predict_image(example_image, loaded_model) + ".")
predict_external_image("C:/Users/ishit/Desktop/hhh.jpg")
