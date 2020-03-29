import os
import numpy as np
import cv2

def resize_data(path_link):
    for label in os.listdir(path_link):
        dir = os.path.join(path_link, label)
        dir = dir + '/'
        for image in os.listdir(dir):
            img = cv2.imread(os.path.join(dir, image))
            new = cv2.resize(img, (32, 32))
            cv2.imwrite(os.path.join(dir, image), new)
            print(os.path.join(dir, image))

#Load data
train_link = 'Dataset/train/'
test_link = 'Dataset/test/'
val_link = 'Dataset/validation/'

resize_data(train_link)
resize_data(test_link)
resize_data(val_link)