# Fisher\'s Iris Data Set 

* Author: John Paul Lee
* Github: JPLee01
* Email: G00387906@gmit.ie
* Created: 21-03-2020, Last update:
------------------------------------------------------------------------------------------------
Programming and Scripting: Fisher’s Iris Data Set Project 2020

This repository details my research and findings to the Fisher’s Iris Data Set Project for Programming and Scripting 2020.

Lecturer: Dr. Ian McLoughlin

The Project instructions can be found at: https://github.com/JPLee01/pandas-project/blob/master/Project%20Instructions.pdf

Table of Contents
------------------------------------------------------------------------------------------------

[Fisher\'s Iris Data Set](#fishers-iris-data-set)

[1. Introduction](#1-introduction)

[2. Project Repository](#2-project-repository)

[3. Fisher\'s Iris Data Set](#3-Fishers-Iris-Data-Set)

  [3.1 Background](#3.1-Background)

[4. Problem Statement](#4-Problem-Statement)

[5. Issues and Inconsistencies with Data Set](#5-Issues-and-Inconsistencies-with-Data-Set)

[6. User Guide](#6-User-Guide)

  [6.1 Downloading the Repository](#6.1-Downloading-the-Repository)

  [6.2  Running the Program](#6.2-Running-the-Program)

  [6.3  Libaries](#6.3-Libaries)

[7. Python Programs and Results Explained](#7-Python-Programs-and-Results-Explained)

  [7.1 Analysis.py Program Explained](#7.1-Analysis.py-Program-Explained)

## 1 Introduction
------------------------------------------------------------------------------------------------

This analysis of Fisher\'s Iris Flower Data Set has been carried out as
an assignment of the Programming & Scripting Module. The aim of this
assignment is to help the student gain a practical experience in data
handling within Python, including data types and structures handling,
data splicing, plots generation and interpretation.

## 2 Project Repository
------------------------------------------------------------------------------------------------

The Project Repository is the source where all the work associated with
the project will be stored. It contains the following files and can be
located [here](https://github.com/JPLee01/pandas-project):

  **File**    |     **Description**
  ---------   |   --------------------------------------------------------
  LICENSE     |    MIT License for the project
  README.md   |    This file; A Description of the Project and Instructions
  IrisData.csv |  Iris Flower Data Set
  Analysis.py | Python Programme for carrying out analysis of the Iris Data set
  Visualisation.py | Python Programme for creating visualisations of the Iris Data set

## 3 Fishers Iris Data Set
------------------------------------------------------------------------------------------------
### 3.1 Background

The data analysed in this project is the \"Iris Flower Data
Set\"[1](#references) This data set was collected by R.A. Fisher and presented
as a data set in 1936 in his paper \"The Use of Multiple Measurements in
Taxonomic Problems.\"[2](#references) In this paper Fisher studied the
use of linear combinations of multiple characterising features of a
species to discriminate it from related species. Within the paper Fisher
studied the following three related species of Iris flowers:

![Iris Species](https://miro.medium.com/max/1400/0*Uw37vrrKzeEWahdB)

Fifty samples of each species were collected and analysed. (It should be
noted that the data for the Setosa and Iris Versicolor were already
available from a previous study by Fishers colleague Botanist Edgar
Anderson). Within each species Fisher studied four distinct
characteristics:

1.  Sepal Length (Cm)
2.  Sepal Width (Cm)
3.  Petal Length (Cm)
4.  Petal Width (Cm)

These characteristics can be seen below:

  ![Iris Characteristics](https://miro.medium.com/max/800/1*1q79O5DCx_XNrAARXSFzpg.png)

## 4  Problem Statement
------------------------------------------------------------------------------------------------
As part of the assignmnent the student was given a set of instruction which can be viewed [here](https://github.com/JPLee01/pandas-project/blob/master/Project%20Instructions.pdf). As seen, within the instrctions a problem statement was printed. It stated that this project will invovle an analysis of the Iris data set. Python code will be utilised for this analysis and the student will be required to give explanations of the python code. The problem statement also explained it was required for the project that a program(s) be created that:
* outputs a summary of each variable to a single text file,
* saves a histogram of each variable to png files, and
* outputs a scatter plot of each pair of variables.

## 5 Issues and Inconsistencies with Data Set
------------------------------------------------------------------------------------------------
It should be noted that there are three inconsistencies between the data set sourced from UCI[1](#references) and the data set presented by Fisher[2](#references). These three inconsistencies are as follows:
1.  35th sample: the fourth feature is given as "0.1" where Fisher had originally given "0.2".
2.  38th sample: the second feature is given as "3.1" where Fisher had originally given "3.6".
3.  38th sample: the third feature is given as "1.5" where Fisher had originally given "1.4".

Please be advised that these three errors have not been rectified in the data set analysed.

##  6 User Guide
------------------------------------------------------------------------------------------------
This section will describe the steps required to download and run the files in the repository.

### 6.1 Downloading the Repository

The repository is stored at the following: https://github.com/JPLee01/pandas-project

To download the repository, do the following:
1.  CLick on the adove link to open the repository
2.  Once in the repository, click on the green “clone or download” button on the right side of the screen.
3.  Select "Download ZIP". This will open a prompt allowing you to save the file to a desired location on your computer.
4.  Navigate to where  the ZIP files are located on your computer and extract the compressed (.zip) files.

### 6.2 Running the Program
Once the repository has been downloaded, you will need to ensure that you are running it in the correct environment. It should be noted that this repository has been written using Python 3.8.2, and consequently it will require a Python version of 3.7 at a minimum to run as designed. The repository also requires a number of external Python libraries [seen below](#6.3-Libaries) to execute correctly. Once the correct version of Python has been installed complete with necessary libaries, and the ZIP has been downloaded and extracted the user can run the program. The running of any of the programs from the command line can be executed as follows:
1.  Open a command prompt (cmd) or equivalent on your computer.([Cmdr](https://cmder.net) is recommended for Windows computers, Mac Computers via the terminal)
2.  Navigate to the desired location through the use of the change directory (cd) command.
3.  Run the program by typing:  
```
python <programme_name.py>
```

### 6.3 Libaries
The following Python libraries were used in the writing of the programs code and are required to successfully run the programs:
* [Numpy](https://www.numpy.org/) - Used for mathematical functions in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) and [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) programs.
* [Pandas](https://pandas.pydata.org/) - Used for import, management, data manipulation and analysis in both the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) and [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) programs.
* [Matplotlib.pyplot](https://matplotlib.org/tutorials/introductory/pyplot.html) - Used for the manipulation of elements and the creation of certain plots graphs, plots and charts within the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program.
* [Seaborn](https://seaborn.pydata.org/) - Used for the creation and manipulation of all plots in the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program. (Seaborn allows for the extetion of the functionality of Matplotlib).
* [Sys](https://docs.python.org/3/library/sys.html) - Used for the creation and writing of text files in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) program.

## 7 Python Programs and Results Explained
------------------------------------------------------------------------------------------------
This section will describe the Pyton programs and subsequent code which was created as well as the results these progmans yeilded.

It should be noted that two separate python programmes have been written for this project:
1.  [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) - A program which was created to carry out the general and statistical analysis of the data set. It outputs results were produced into the [Analysis.txt](https://github.com/JPLee01/pandas-project/blob/master/Analysis.txt) file.
2.  [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) - A program which was created to produce visualisations of the data set. It outputs were stored as .png files in the [repository](https://github.com/JPLee01/pandas-project#2-project-repository) the programe is stored in.

For clarity comments within the code have been removed from this document, but these can be viewed within the specific Python programmes.

### 7.1 Analysis.py Program Explained
As seen above the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) program is primiarly concerned with the general and statistical analysis of the data set.

### Importing the Libaries
As seen above a munber of libaries are requred to successfully write and run the programs code. For the Analysis.py program the following libaries were imported:
```
import pandas as pd 
import numpy as np
import sys
```

### Importing the Data Set and Creation of a DataFrame
The data set is imported from the Csv file through the use of the pandas.read fuction, Once imported this data set is used in the creation of a DataFrame to allow for greater ease of analysis.

This is implemented as follows:
```
f = pd.read_csv("IrisData.csv")
df = pd.DataFrame(f)
```

It should be noted that this procedure is also repreted in the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program.

### List of the Species in the Data Set
To create a list of the species present in the data set the following code is executed:
  * Note the .unique() command is added to remove any unique (error) species in the data set and print() command is added to allow a gap between results within the [Analysis.txt](https://github.com/JPLee01/pandas-project/blob/master/Analysis.txt) file.
```
Specieslist = df["species"].unique()
print ("The Species present in this dataset are:")
for i in Specieslist:
    print('>', i)
print()
```

The result of this code is as follows:
```
The Species present in this dataset are:
> setosa
> versicolor
> virginica
```

### Amount of Samples of each Species in the Data Set
In order to create a list showing the amount of species present in the data set the following code is executed:
  * Note this code makes use of the Pandas.DataFrame.value_counts command and the '\n' function to produce each species on a seperate line.
```
print("Amount of samples of each Species:")
print(df['species'].value_counts(), '\n')
```
This code produces the following results:
```
Amount of samples of each Species:
setosa        50
versicolor    50
virginica     50
Name: species, dtype: int64 
```

### Print the First 10 Rows of Data
To display the first 10 rows of data from the data set the Pandas.DataFrame.head command is used within the code:
```
print("Sample of the First 10 Rows of Data:")
print(df.head(10), "\n")
```
The result of this code is as follows:
```
Sample of the First 10 Rows of Data:
   sepal_length  sepal_width  petal_length  petal_width species
0           5.1          3.5           1.4          0.2  setosa
1           4.9          3.0           1.4          0.2  setosa
2           4.7          3.2           1.3          0.2  setosa
3           4.6          3.1           1.5          0.2  setosa
4           5.0          3.6           1.4          0.2  setosa
5           5.4          3.9           1.7          0.4  setosa
6           4.6          3.4           1.4          0.3  setosa
7           5.0          3.4           1.5          0.2  setosa
8           4.4          2.9           1.4          0.2  setosa
9           4.9          3.1           1.5          0.1  setosa 
```




References
------------------------------------------------------------------------------------------------

1.  UCI Machine Learning Repository -- Iris Data Set, [[http://archive.ics.uci.edu/ml/datasets/Iris]{.underline}](http://archive.ics.uci.edu/ml/datasets/Iris)

2.  The Use of Multiple Measurements in Taxonomic Problems, <http://www.comp.tmu.ac.jp/morbier/R/Fisher-1936-Ann._Eugen.pdf>

3.  
