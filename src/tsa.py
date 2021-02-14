# import the libraries
import re # regular expressions
import nltk # text manuplations
import warnings
import string
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

#optional pandas and warning settings
pd.set_option("display.max_colwidth", 200)
warnings.filterwarnings("ignore", category=DeprecationWarning)

#load and read train and test data 
train = pd.read_csv('../Data/train_data.csv')
test = pd.read_csv('../Data/test_data.csv')

# Data Inspection
print(train[train['label'] == 0].head(10))