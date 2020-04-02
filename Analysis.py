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
#List of the Species in the data (Removing unique Species)
Specieslist = df["species"].unique()
print ("The Species present in this dataset are:")
for i in Specieslist:
    print('>', i)

#Amount of samples of each Species in the Data
print("Amount of samples of each Species:")
print(df['species'].value_counts(), '\n')

#Using the pandas.DataFrame.head Command to Print the First 10 Rows of Data
print("Sample of the First 10 Rows of Data:")
print(df.head(10), "\n")

#Using the pandas.DataFrame.tail Command to Print the Last 10 Rows of Data
print("Sample of the Last 10 Rows of Data:")
print(df.tail(10), "\n")

#Using the pandas.DataFrame.sample Command to Print a random sample of 10 Rows of Data
print("Random sample of 10 Rows of Data:")
print(df.sample(10), "\n")

#Using the pandas Slice Command to Print the Middle 10 Rows of Data (70-80)
print("Sample of Rows 70-80 of Data:")
print(df[70:80], "\n")

#Using the pandas.describe Command to provide a Summary Statistics of the Data
print("Summary Statistics of the Data:")
print(df.describe(),'\n') 



#References:
#DataFrame: https://www.geeksforgeeks.org/python-pandas-dataframe/
#DataFrame: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
#Lists: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
#Pandas Head, Tail, Slice: https://note.nkmk.me/en/python-pandas-head-tail/
#Pandas Cheat Sheet: https://www.dataquest.io/blog/pandas-cheat-sheet/
