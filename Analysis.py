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
print ("The Species present in this dataset are:")
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
print("Random sample of 10 Rows of Data:")
print(df.sample(10), "\n")

#Using the pandas Slice Command to Print the Middle 10 Rows of Data (70-80)
print("Sample of Rows 70-80 of Data:")
print(df[70:80], "\n")

#Using the pandas.describe Command to provide a Summary Statistics for all the Species (Rounded to 3 Decimal Places)
#Rounded to 3 Decimal Places using the Round command
print("Summary Statistics of all the Species (Rounded to 3 Decimal Places):")
print(round(df.describe(),3),'\n') 

#Using the pandas.describe Command to provide a Summary Statistics of each type of Species (Rounded to 3 Decimal Places)

#Create 3 DataFrame for each Species
setosa = f[f['species']=="setosa"]
versicolor = f[f['species']=="versicolor"]
virginica = f[f['species']=="virginica"]

print("Summary Statistics for Setosa (Rounded to 3 Decimal Places):")
#Rounded to 3 Decimal Places using the Round command
print(round(setosa.describe(),3),'\n')

print("Summary Statistics for Versicolor (Rounded to 3 Decimal Places):")
#Rounded to 3 Decimal Places using the Round command
print(round(versicolor.describe(),3),'\n')

print("Summary Statistics for Virginica (Rounded to 3 Decimal Places):")
#Rounded to 3 Decimal Places using the Round command
print(round(virginica.describe(),3),'\n')

#Close and Save the Analyisi Text File
sys.stdout.close()









#References:
#DataFrame: https://www.geeksforgeeks.org/python-pandas-dataframe/
#DataFrame: https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python
#Lists: https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/
#Pandas Head, Tail, Slice: https://note.nkmk.me/en/python-pandas-head-tail/
#Pandas Cheat Sheet: https://www.dataquest.io/blog/pandas-cheat-sheet/
#Pandas Rounding of Describe Result: https://stackoverflow.com/questions/25272024/round-each-number-in-a-python-pandas-data-frame-by-2-decimals
#How to Save the  "Print Results" to a text file: https://kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python
#How to import Stdout: https://kite.com/python/docs/sys.stdout/
#General Refernce: https://www.youtube.com/watch?v=vmEHCJofslg&feature=youtu.be
#How to use CSV files: https://towardsdatascience.com/pandas-dataframe-playing-with-csv-files-944225d19ff