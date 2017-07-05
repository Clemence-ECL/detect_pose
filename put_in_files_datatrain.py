import os
import random

repartition = ['train']*80+['validation']*20
folder_train = 'data/train/face/'
folder_validation = 'data/validation/face/'

for element in os.listdir('face'):
  if os.path.isdir(element):
    next
  else:
    place = random.choice(repartition)
    if place == 'train':
      os.rename('face/'+element,folder_train+element)
      print('image displaced')
    else:
      os.rename('face/'+element,folder_validation+element)
      print('image displaced')
