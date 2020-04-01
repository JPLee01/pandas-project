#John Paul Lee
#Analysis of Iris Data Set

#Import Pandas for Data Management 
import pandas as pd

#Import Numpty and Scipy.stats for analysis
import numpy as np
from scipy import stats

#Import the data
f = pd.read_csv("IrisData.csv")

#Create a DataFrame from the Csv file to allow for easier analysis
df = pd.DataFrame(f)

#General Overview of the Data
#List of the Species in the data
Specieslist = df["species"].unique()
print ("The Species present in this dataset are:")
for i in Specieslist:
    print('>', i)


#References:
#DataFrame: https://www.geeksforgeeks.org/python-pandas-dataframe/
#DataFrame: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
#Lists: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
