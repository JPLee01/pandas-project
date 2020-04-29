#John Paul Lee
#Analysis of Iris Data Set

#Import Pandas for Data Management 
import pandas as pd

#Import Numpty for Analysis of the data 
import numpy as np

#Import Sys to allow the "Print Results" to be written to a Txt File
import sys

#Create a Txt File called Analysis and excute the Write Function (Allows the "Print Results" to be written onto the Analysis Txt File)
sys.stdout = open("Analysis.txt", "w")
print ("The following is the results of the analysis of the Iris Data Set")
print() #Print a blank line for cleaner output on the text file 

#Import the data
f = pd.read_csv("IrisData.csv")

#Create a DataFrame from the Csv file to allow for easier analysis
df = pd.DataFrame(f)

#General Overview of the Data Section
#List of the Species in the Data Set (Removing unique Species)
Specieslist = df["species"].unique()
print ("The species present in this Data Set are:")
for i in Specieslist:
    print('>', i)
print() #Print a blank line for cleaner output on the text file 

#Amount of samples of each Species in the Data Set
print("Amount of samples of each Species:")
print(df['species'].value_counts(), '\n')

#Using the pandas.DataFrame.head Command to Print the First 10 Rows of Data
print("Sample of the First 10 Rows of Data:")
print(df.head(10), "\n")

#Using the pandas.DataFrame.tail Command to Print the Last 10 Rows of Data
print("Sample of the Last 10 Rows of Data:")
print(df.tail(10), "\n")

#Using the pandas.DataFrame.sample Command to Print a random sample of 10 Rows of Data
print("Random Sample of 10 Rows of Data:")
print(df.sample(10), "\n")

#Using the pandas Slice Command to Print the Middle 10 Rows of Data (70-80)
print("Sample of Rows 70-80 of Data:")
print(df[70:80], "\n")

#Using the pandas.describe Command to provide a Summary Statistics for all the Species (Rounded to 3 Decimal Places)
#Rounded to 3 Decimal Places using the Round command
print("Summary Statistics of all the Species (Rounded to 3 decimal places):")
print(round(df.describe(),3),'\n') 

#Using the pandas.describe Command to provide a Summary Statistics of each type of Species (Rounded to 3 Decimal Places)

#Create 3 DataFrame for each Species
setosa = f[f['species']=="setosa"]
versicolor = f[f['species']=="versicolor"]
virginica = f[f['species']=="virginica"]

print("Summary Statistics for Setosa (Rounded to 3 decimal places):")
#Rounded to 3 Decimal Places using the Round command
print(round(setosa.describe(),3),'\n')

print("Summary Statistics for Versicolor (Rounded to 3 decimal places):")
#Rounded to 3 Decimal Places using the Round command
print(round(versicolor.describe(),3),'\n')

print("Summary Statistics for Virginica (Rounded to 3 decimal places):")
#Rounded to 3 Decimal Places using the Round command
print(round(virginica.describe(),3),'\n')

#Close and Save the Analyisis Text File
sys.stdout.close()
