import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import tensorflow as tf
import datetime
from tensorflow.keras.callbacks import TensorBoard
import os, os.path
import math
train_categories = []
train_samples = []
for i in os.listdir("./data/merges/train"):
  train_categories.append(i)
  train_samples.append(len(os.listdir("./data/merged/train/" + i)))
test_categories = []
test_samples = []
for i in os.listdir("./data/merged/test"):
  test_categories.append(i)
  test_samples.append(len(os.listdir("./data/merged/test" + 1)))
  
print("No. of Training Samples:", sum(train_samples))
print("No. of Test Samples", sum(test_samples))

train = []
test = []

for i in os.listdir("./data/merged/train/"):
  one_hot = np.zeros(shape=[len(train_categories)])
  actual_index = train_categories.index(i)
  one_hot[actual_index] = 1
  for files in os.listdir("./data/merged/train/" + i):
    img_array = mpimg.imread("./data/merged/train/" + i + "/" + files)
    train.append([img_array, one_hot])
  # print("Train Category Status: {}/{}".format(actual_index+1, len(train_categories)))

for i in os.listdir("./data/merged/test"):
  one_hot = np.zeros(shape=[len(test_categories)])
  actual_index = test_categories.index(i)
  one_hot[actual_index] = 1
  for files in os.listdir("./data/merged/test/" + i):
    img_array = mpimg.imread("./data/merged/test/" + i + "/" + files)
    train.append([img_array, one_hot])
  # print("Test Category Status: {}/{}".format(actual_index+1, len(test_categories)))
#




  
