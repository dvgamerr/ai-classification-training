from fastai.vision import *
from pathlib import Path

import warnings
import os

warnings.filterwarnings("ignore")

dir_train = './train/anime'

for t in os.listdir(dir_train):
  verify_images(dir_train/t.name, delete=True, max_size=500)