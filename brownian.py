import numpy as np 
import matplotlib.pyplot as plt 
import pandas as pd 
from pandas import DataFrame, Series

import pims 
import trackpy as tp 

@pims.pipeline
def gray(image):
    return image[:, :, 1]

# frames = pims.open('../uke2/TIFF_browntest_2022-08-30-140914-0001.tif')
frames = pims.open('../uke2/no_contrast.tif')

# f = tp.locate(frames[0], 9, invert = True)
# tp.annotate(f, frames[0])

# fig, ax = plt.subplots()
# ax.hist(f['mass'], bins=20)

# Optionally, label the axes.
# ax.set(xlabel='mass', ylabel='count')
# plt.show()


f = tp.quiet(tp.batch(frames[:3], 9, minmass = 200, threshold  = 5))#100 might have also worked 
print(f)

# tp.annotate(f, frames)

# fig, ax = plt.subplots()
# ax.hist(f['mass'], bins=20)
# ax.set(xlabel='mass', ylabel='count')
# plt.show()

# a = tp.subpx_bias(f)
# plt.show()



