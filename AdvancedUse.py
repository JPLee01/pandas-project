#John Paul Lee
#Analysis of Iris Data Set

#Created to explore the potential advanced use of the Iris Data Set

#Import Pandas for Data Management 
import pandas as pd

#Import Numpty for Analysis of the data 
import numpy as np

#Import Train Test Split module from the Scikit-learn library to split the dataset
from sklearn.model_selection import train_test_split

#Import KNeighborsClassifier module from the Scikit-learn library to implement the K-Nearest Neighbor approach to Machine Learning
from sklearn.neighbors import KNeighborsClassifier

#Import the data
f = pd.read_csv("IrisData.csv")

#Create a DataFrame from the Csv file to allow for easier analysis
df = pd.DataFrame(f)

