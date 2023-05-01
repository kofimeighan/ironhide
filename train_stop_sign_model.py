import logging
import argparse
import torch
from torch.utils.data import Dataset, DataLoader
import os
import tensorflow as tf
import cv2
import time
#import tesnsorflow_datasets as tfds

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

def parse_tfr_element(element):
  data = {
    'height': tf.io.FixedLenFeature([], tf.int64),
    'width': tf.io.FixedLenFeature([], tf.int64),
    'label': tf.io.FixedLenFeature([], tf.int64),
    'raw_image': tf.io.FixedLenFeature([], tf.string),
    'depth': tf.io.FixedLenFeature([], tf.int64),
  }

  content = tf.io.parse_single_example(element, data)

  height = content['height']
  width = content['width']
  depth = content['depth']
  label = content['label']
  raw_image = content['raw_image']

  #get our 'feature'-- our image -- and reshape it appropriately
  feature = tf.io.parse_tensor(raw_image, out_type=tf.uint8)
  feature = tf.reshape(feature, shape=[height, width, depth])
  return (feature, label)



def get_dataset(tfr_dir = "/content/", example_type = "train/"):
  #files = glob.glob(os.path.join(tfr_dir, pattern), recursive=False)
  #print(files)

  #create the dataset
  dir = None
  if example_type == "train/":
    dir = os.path.join(tfr_dir, example_type)
  elif example_type == "valid/":
    dir = os.path.join(tfr_dir, example_type)


  dataset = tf.data.TFRecordDataset(dir)
  print(type(dataset))

  #pass every single feature through our mapping function
  dataset = dataset.map(
    parse_tfr_element
  )

  dataset = dataset.batch(32) #batch
  dataset = dataset.map(lambda x, y:(tf.cast(x, tf.float32)/255.0, y)) #normalize
  dataset = dataset.apply(tf.data.experimental.assert_cardinality(32))
  #dataset = dataset.with_format("torch")
  #print(type(tfds.as_numpy(dataset)))
  return dataset#tfds.as_numpy(dataset)

def main():
  net = StopSignModel()
  print(summary(net, (1, 256, 256)))
  training_dataset = get_dataset()
  valid_dataset = get_dataset(example_type = "valid/")

  training_loader = DataLoader(training_dataset, batch_size = 32, shuffle = True, num_workers = 2)
  valid_loader = DataLoader(valid_dataset, batch_size = 32, shuffle = True, num_workers = 2)
  print(type(training_loader))
  optimizer = torch.optim.Adam(net.parameters(), lr = 0.0002, betas = (0.5, 0.999))

  loss = nn.BCELoss()

  num_epochs = 12
  loss_sum = 0

  with open(os.path.join("epoch_loss", "epoch_loss.csv"), "w+" , buffering = 1) as epoch_loss_file:
    epoch_loss_file.write("/content/epoch, training_loss, validation_loss\n")
    for epoch in range(1, num_epochs):
      logging.info(" ********** Epoch {} **********".format(epoch))
      #print(training_loader.item())
      iterator = iter(training_loader)
      for feature, label in enumerate(training_loader):
        #feature, label = data
        feature, label = feature.to(device), label.to(device)
        optimizer.zero_grad()
        output = net(input)
        loss = loss(output, label)
        loss.backward()
        optimizer.step()
        loss_sum += loss.item()

