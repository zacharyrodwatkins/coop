#Import fits parser load data
import time
import sys
sys.path.append('/home/watkinsz/Desktop/For_Zack/ML/fitsParser')
sys.path.append('/home/watkinsz/Desktop/For_Zack/ML/abs_mag')

#import ML stuff
from function import get_EBV, save_data
from fitsParser import fitsParser
from sklearn.model_selection import train_test_split
import numpy as np
from keras.models import Sequential
from keras import Model
from keras.layers import Dense, Activation
from keras import optimizers
#for the classifier
from dwarfClassifier import *

#plotting stuff
import matplotlib.pyplot as plt
from astropy.modeling import models, fitting


#saving stuff
import pandas as pd
pd.options.mode.chained_assignment = None #disables some warning
import joblib as jb