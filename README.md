# Fisher\'s Iris Data Set 

* **Author:** John Paul Lee
* **Github:** JPLee01
* **Email:** G00387906@gmit.ie
* **Created:** 21-03-2020, **Last update:** 29-04-2020
------------------------------------------------------------------------------------------------
**Programming and Scripting:** Fisher’s Iris Data Set Project 2020

This repository details my research and findings to the Fisher’s Iris Data Set Project for Programming and Scripting 2020.

**Lecturer:** Dr. Ian McLoughlin

The Project instructions can be found at: https://github.com/JPLee01/pandas-project/blob/master/Project%20Instructions.pdf

**Table of Contents**
------------------------------------------------------------------------------------------------

[Fisher\'s Iris Data Set](#fishers-iris-data-set)

[1. Introduction](#1-introduction)

[2. Project Repository](#2-project-repository)

[3. Fisher\'s Iris Data Set](#3-Fishers-Iris-Data-Set)

  [3.1 Background](#3.1-Background)

[4. Problem Statement](#4-Problem-Statement)

[5. Previous Case Studies of the Data Set](#5-Previous-Case-Studies-of-the-Data-Set)

[6. Issues and Inconsistencies with Data Set](#6-Issues-and-Inconsistencies-with-Data-Set)

[7. User Guide](#7-User-Guide)

  [7.1 Downloading the Repository](#7.1-Downloading-the-Repository)

  [7.2  Running the Program](#7.2-Running-the-Program)

  [7.3  Libraries](#7.3-Libraries)

[8. Python Programs and Results Explained](#8-Python-Programs-and-Results-Explained)

  [8.1 Analysis.py Program Explained](#8.1-Analysis.py-Program-Explained)

  [8.2 Visualisation.py Program Explained](#8.2-Visualisation.py-Program-Explained)

  [8.3 Interactive.py Program Explained](#8.3-Interactive.py-Program-Explained)

  [8.4 AdvancedUse.py Program Explained](#8.4-AdvancedUse.py-Program-Explained)

[9. Summary, Conclusion and Future Possibilities for the Data Set](#9-Summary,-Conclusion-and-Future-Possibilities-for-the-Data-Set)

[10. References](#10-References)

[11. Bibliography](#11-Bibliography)

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
  Visualisations | A folder containing all of the Plots of the Visualisation.py Program
  .gitignore | A Text File explicitly explaining to Git which files or folders to ignore in the Project 
  AdvancedUse.py | Python Program created to explore the potential advanced use of the Iris Data Set
  Analysis.py | Python Programme for carrying out analysis of the Iris Data Set
  Analysis.txt | The results from the Analysis.py Program saved onto a Text File
  Interactive-Report.gif | Gif used in the Readme to highlight the Iris Data Interactive Report
  Interactive.py | Python Program for creating the Interactive Report of the Iris Data Set
  Iris Data Interactive Report.html | Interactive Report created through the Interactive.py program
  IrisData.csv |  Iris Flower Data Set
  LICENSE     |    MIT License for the project
  Project Instructions.pdf | A PDF copy of the Project Instructions
  README.md   |    This file; A Description of the Project and Instructions
  Visualisation.py | Python Programme for creating visualisations of the Iris Data Set

## 3 Fishers Iris Data Set
------------------------------------------------------------------------------------------------
### 3.1 Background
The data analysed in this project is the \"Iris Flower Data
Set\".<sup>[1](#myfootnote1)</sup> This data set was collected by R.A. Fisher and presented
as a data set in 1936 in his paper \"The Use of Multiple Measurements in
Taxonomic Problems\".<sup>[2](#myfootnote2)</sup> In this paper Fisher studied the
use of linear combinations of multiple characterising features of a
species to discriminate it from related species. Within the paper Fisher
studied the following three related species of Iris flowers:

![Iris Species](https://miro.medium.com/max/1400/0*Uw37vrrKzeEWahdB)

Fifty samples of each species were collected and analysed. (It should be
noted that the data for the Setosa and Versicolor were already
available from a previous study by Fisher's colleague Botanist Edgar
Anderson). Within each species, Fisher studied four distinct
characteristics:

1.  Sepal Length (Cm)
2.  Sepal Width (Cm)
3.  Petal Length (Cm)
4.  Petal Width (Cm)

These characteristics can be seen below:

  ![Iris Characteristics](https://miro.medium.com/max/800/1*1q79O5DCx_XNrAARXSFzpg.png)

##  4 Problem Statement
------------------------------------------------------------------------------------------------
As part of the assignment, the student was given a set of instructions which can be viewed [here](https://github.com/JPLee01/pandas-project/blob/master/Project%20Instructions.pdf). As seen, within the instructions a problem statement was printed. It stated that this project will involve an analysis of the Iris Data Set. Python code will be utilised for this analysis and the student will be required to give explanations of the python code. The problem statement also explained it was required for the project that a program(s) be created that:
* Outputs a summary of each variable to a single text file
* Saves a histogram of each variable to png files
* Outputs a scatter plot of each pair of variables

##  5 Previous Case Studies of the Data Set
------------------------------------------------------------------------------------------------
Through an online search it can be seen that a number of previous iterations of the analysis of the data have taken place. These include programs written in Python as well as other computing language. Previous iteration referenced in the study of this project were the works of Venkata Sai Reddy Avuluri<sup>[3](#myfootnote3)</sup> and Oluwasogo Oluwafemi Ogundowole<sup>[4](#myfootnote4)</sup> on Medium, who demonstrates the use of Pandas, Numpy, Matplotlib and Seaborn for management of the Iris Data Set. As well as Binu<sup>[5](#myfootnote5)</sup> on Kaggle who demonstrates in further detail the visualisations which can be created from the Iris Data Set using Seaborn and Matplotlib.

##  6 Issues and Inconsistencies with Data Set
------------------------------------------------------------------------------------------------
It should be noted, that there are three inconsistencies between the data set sourced from UCI<sup>[1](#myfootnote1)</sup> and the data set presented by Fisher.<sup>[2](#myfootnote2)</sup> These three inconsistencies are as follows:
1.  35th sample: the fourth feature is given as "0.1" where Fisher had originally given "0.2".
2.  38th sample: the second feature is given as "3.1" where Fisher had originally given "3.6".
3.  38th sample: the third feature is given as "1.5" where Fisher had originally given "1.4".

Please be advised that these three errors have not been rectified in the data set analysed.

##  7 User Guide
------------------------------------------------------------------------------------------------
This section will describe the steps required to download and run the files in the repository.

### 7.1 Downloading the Repository
The repository is stored at the following: https://github.com/JPLee01/pandas-project

To download the repository, do the following:
1.  Click on the above link to open the repository
2.  Once in the repository, click on the green “clone or download” button on the right side of the screen.
3.  Select "Download ZIP". This will open a prompt allowing you to save the file to a desired location on your computer.
4.  Navigate to where  the ZIP files are located on your computer and extract the compressed (.zip) files.

### 7.2 Running the Program
Once the repository has been downloaded, you will need to ensure that you are running it in the correct environment. It should be noted that this repository has been written using Python 3.8.2 and consequently it will require a Python version of 3.7 at a minimum to run as designed. The repository also requires a number of external Python libraries [seen below](#7.3-Libaries) to execute correctly. Once the correct version of Python has been installed complete with necessary libraries and the ZIP has been downloaded and extracted the user can run the program. The running of any of the programs from the command line can be executed as follows:
1.  Open a command prompt (cmd) or equivalent on your computer.([Cmdr](https://cmder.net) is recommended for Windows computers, Mac Computers via the terminal)
2.  Navigate to the desired location through the use of the change directory (cd) command.
3.  Run the program by typing:  
```
python <programme_name.py>
```

### 7.3 Libraries
The following Python libraries were used in the writing of the programs code and are required to successfully run the programs:
* [Numpy](https://www.numpy.org/) - Used for mathematical functions in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py), [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) and [AdvancedUse.py](https://github.com/JPLee01/pandas-project/blob/master/AdvancedUse.py) programs.
* [Pandas](https://pandas.pydata.org/) - Used for import, management, data manipulation and analysis in both the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py), [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) and [AdvancedUse.py](https://github.com/JPLee01/pandas-project/blob/master/AdvancedUse.py) programs.
* [Matplotlib.pyplot](https://matplotlib.org/tutorials/introductory/pyplot.html) - Used for the manipulation of elements and the creation of certain plots graphs, plots and charts within the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program.
* [Seaborn](https://seaborn.pydata.org/) - Used for the creation and manipulation of all plots in the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program. (Seaborn allows for the extetion of the functionality of Matplotlib).
* [Sys](https://docs.python.org/3/library/sys.html) - A module more than a library within Python used for the creation and writing of text files in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) program.
* [Pandas Profiling](https://towardsdatascience.com/exploratory-data-analysis-with-pandas-profiling-de3aae2ddff3) - A module more than a library within Python used for the creation of interactive reports through ProfileReport as seen in the [Interactive.py](https://github.com/JPLee01/pandas-project/blob/master/Interactive.py) program.
* [Scikit-Learn](https://scikit-learn.org/stable/) - A machine learning library for the Python programming language. The use of this library is explored within the [AdvancedUse.py](https://github.com/JPLee01/pandas-project/blob/master/AdvancedUse.py) program.

## 8 Python Programs and Results Explained
------------------------------------------------------------------------------------------------
This section will describe the Python programs and subsequent code which was created as well as the results these programs yielded.

It should be noted that four separate python programs have been written for this project:
1.  [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) - A program which was created to carry out the general and statistical analysis of the data set. It outputs results were produced into the [Analysis.txt](https://github.com/JPLee01/pandas-project/blob/master/Analysis.txt) file.
2.  [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) - A program which was created to produce visualisations of the data set. It outputs were stored as .png files in the [repository](https://github.com/JPLee01/pandas-project#2-project-repository) the programe is stored in.
3. [Interactive.py](https://github.com/JPLee01/pandas-project/blob/master/Interactive.py) - A program which was created to show the potential and capability of the Pandas Profiling module. The output of this program is the creation of the [Iris Data Interactive Report](https://github.com/JPLee01/pandas-project/blob/master/Iris%20Data%20Interactive%20Report.html).
4.  [AdvancedUse.py](https://github.com/JPLee01/pandas-project/blob/master/AdvancedUse.py) - A program created to investigate the potential advanced uses of the Iris Data Set, namely the K-Nearest Neighbors (KNN) algorithm. 

For clarity comments within the code have been removed from this document, but these can be viewed within the specific Python programs.

### 8.1 Analysis.py Program Explained
As seen above the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) program is primarily concerned with the general and statistical analysis of the data set.

#### Importing the Libraries
As seen above a munber of libraries are required to successfully write and run the programs code. For the Analysis.py program the following libraries were imported:
```
import pandas as pd 
import numpy as np
import sys
```

#### Importing the Data Set and Creation of a DataFrame
The data set is imported from the Csv file through the use of the pandas.read function. Once imported this data set is used in the creation of a DataFrame to allow for greater ease of analysis.

This is implemented as follows:
```
f = pd.read_csv("IrisData.csv")
df = pd.DataFrame(f)
```

It should be noted that this procedure is also repeated in the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program.

#### List of the Species in the Data Set
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
The species present in this Data Set are:
> setosa
> versicolor
> virginica
```

#### Print the Amount of Samples of each Species in the Data Set
In order to create a list displaying the amount of species present in the data set the following code is executed:
  * Note this code makes use of the Pandas.DataFrame.value_counts command and the '\n' function to produce each species on a seperate line.
```
print("Amount of samples of each Species:")
print(df['species'].value_counts(), '\n')
```
This code produces the following results:
```
Amount of samples of each Species:
virginica     50
versicolor    50
setosa        50
Name: species, dtype: int64 
```

####  Print the First 10 Rows of Data
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

#### Print the Last 10 Rows of Data
To display the last 10 rows of data from the data set the Pandas.DataFrame.tail command is used within the code:
```
print("Sample of the Last 10 Rows of Data:")
print(df.tail(10), "\n")
```
This code produces the following results:
```
Sample of the Last 10 Rows of Data:
     sepal_length  sepal_width  petal_length  petal_width    species
140           6.7          3.1           5.6          2.4  virginica
141           6.9          3.1           5.1          2.3  virginica
142           5.8          2.7           5.1          1.9  virginica
143           6.8          3.2           5.9          2.3  virginica
144           6.7          3.3           5.7          2.5  virginica
145           6.7          3.0           5.2          2.3  virginica
146           6.3          2.5           5.0          1.9  virginica
147           6.5          3.0           5.2          2.0  virginica
148           6.2          3.4           5.4          2.3  virginica
149           5.9          3.0           5.1          1.8  virginica 
```

#### Print a Random Sample of 10 Rows of Data
To display a random 10 rows of data from the data set the Pandas.DataFrame.sample command is used within the code:
```
print("Random sample of 10 Rows of Data:")
print(df.sample(10), "\n")
```
This code produces the following results:
```
Random Sample of 10 Rows of Data:
     sepal_length  sepal_width  petal_length  petal_width     species
12            4.8          3.0           1.4          0.1      setosa
84            5.4          3.0           4.5          1.5  versicolor
16            5.4          3.9           1.3          0.4      setosa
53            5.5          2.3           4.0          1.3  versicolor
17            5.1          3.5           1.4          0.3      setosa
112           6.8          3.0           5.5          2.1   virginica
124           6.7          3.3           5.7          2.1   virginica
38            4.4          3.0           1.3          0.2      setosa
81            5.5          2.4           3.7          1.0  versicolor
51            6.4          3.2           4.5          1.5  versicolor 
```
* Note the result for this code will change everytime the program is run.

#### Print the Middle 10 Rows of Data (70-80)
To display the middle 10 rows of data the Pandas.DataFrame.slice command is used within the code:
```
print("Sample of Rows 70-80 of Data:")
print(df[70:80], "\n")
```
This code produces the following results:
```
Sample of Rows 70-80 of Data:
    sepal_length  sepal_width  petal_length  petal_width     species
70           5.9          3.2           4.8          1.8  versicolor
71           6.1          2.8           4.0          1.3  versicolor
72           6.3          2.5           4.9          1.5  versicolor
73           6.1          2.8           4.7          1.2  versicolor
74           6.4          2.9           4.3          1.3  versicolor
75           6.6          3.0           4.4          1.4  versicolor
76           6.8          2.8           4.8          1.4  versicolor
77           6.7          3.0           5.0          1.7  versicolor
78           6.0          2.9           4.5          1.5  versicolor
79           5.7          2.6           3.5          1.0  versicolor  
```

#### Print Summary Statistics for all the Species (Rounded to 3 Decimal Places)
To display a summary statistics for all the species the Pandas.DataFrame.describe command is used within the code:
  * Note the Pandas.Round command is also implemented to round the results to 3 decimal places for aesthetics.<sup>[6](#myfootnote6)</sup>
```
print("Summary Statistics of all the Species (Rounded to 3 Decimal Places):")
print(round(df.describe(),3),'\n') 
```
This code produces the following results:
```
Summary Statistics of all the Species (Rounded to 3 decimal places):
       sepal_length  sepal_width  petal_length  petal_width
count       150.000      150.000       150.000      150.000
mean          5.843        3.054         3.759        1.199
std           0.828        0.434         1.764        0.763
min           4.300        2.000         1.000        0.100
25%           5.100        2.800         1.600        0.300
50%           5.800        3.000         4.350        1.300
75%           6.400        3.300         5.100        1.800
max           7.900        4.400         6.900        2.500 
```

#### Print Summary Statistics for each of the Species (Rounded to 3 Decimal Places)
In order to create a summary statistics for each of the species we first need to create DataFrames for each of the species, to do this we use the Pandas.DataFrame command to further breakdown the origional DataFrame:
```
setosa = f[f['species']=="setosa"]
versicolor = f[f['species']=="versicolor"]
virginica = f[f['species']=="virginica"]
```
We then use the Pandas.DataFrame.describe and the Pandas.Round commands as above for each species. 

To create Summary Statistics for Setosa (Rounded to 3 Decimal Places):
```
print("Summary Statistics for Setosa (Rounded to 3 Decimal Places):")
print(round(setosa.describe(),3),'\n')
```
The result of this code is as follows:
```
Summary Statistics for Setosa (Rounded to 3 decimal places):
       sepal_length  sepal_width  petal_length  petal_width
count        50.000       50.000        50.000       50.000
mean          5.006        3.418         1.464        0.244
std           0.352        0.381         0.174        0.107
min           4.300        2.300         1.000        0.100
25%           4.800        3.125         1.400        0.200
50%           5.000        3.400         1.500        0.200
75%           5.200        3.675         1.575        0.300
max           5.800        4.400         1.900        0.600  
```
To create Summary Statistics for Versicolor (Rounded to 3 Decimal Places):
```
print("Summary Statistics for Versicolor (Rounded to 3 Decimal Places):")
print(round(versicolor.describe(),3),'\n')
```
The result of this code is as follows:
```
Summary Statistics for Versicolor (Rounded to 3 decimal places):
       sepal_length  sepal_width  petal_length  petal_width
count        50.000       50.000         50.00       50.000
mean          5.936        2.770          4.26        1.326
std           0.516        0.314          0.47        0.198
min           4.900        2.000          3.00        1.000
25%           5.600        2.525          4.00        1.200
50%           5.900        2.800          4.35        1.300
75%           6.300        3.000          4.60        1.500
max           7.000        3.400          5.10        1.800 
```
To create Summary Statistics for Virginica (Rounded to 3 Decimal Places):
```
print("Summary Statistics for Virginica (Rounded to 3 Decimal Places):")
print(round(virginica.describe(),3),'\n')
```
The result of this code is as follows:
```
Summary Statistics for Virginica (Rounded to 3 decimal places):
       sepal_length  sepal_width  petal_length  petal_width
count        50.000       50.000        50.000       50.000
mean          6.588        2.974         5.552        2.026
std           0.636        0.322         0.552        0.275
min           4.900        2.200         4.500        1.400
25%           6.225        2.800         5.100        1.800
50%           6.500        3.000         5.550        2.000
75%           6.900        3.175         5.875        2.300
max           7.900        3.800         6.900        2.500 
```

#### To create a Text File and Save the Results of the Analysis.py to it
In order to create a text file and save the results to it we make use of the [Sys](https://docs.python.org/3/library/sys.html) module within Python.<sup>[7](#myfootnote7)</sup>
1.  First at the beginning of the program we import the sys module:
```
import sys
```
2.  This then allows the use of the sys.stdout and write function to create a text file called "Analysis.txt" and allows the results of the Analysis.py program to be written into the Analysis.txt. An opening sentance is inserted explaining that the following are results of the analysis of the Iris Data Set:
```
sys.stdout = open("Analysis.txt", "w")
print ("The following is the results of the analysis of the Iris Data Set")
print()
```
3.  At the end of the program the text file is saved and closed as follows:

```
sys.stdout.close()
```

### 8.2 Visualisation.py Program Explained
As seen above the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program is primarily concerned with the production of visualisations of the data set.

All plots produced by the program are saved in .png formal to the Visualisations folder. 

  * Note that any exisiting plots in the folder will be overwritten as new plots are generated through the program. 

####  Importing the Libraries
As well as the libraries imported in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) program the following extra libraries are imported to the Visualisation.py program:
```
import matplotlib.pyplot as plt
import seaborn as sns
```

####  Setting of Global Styles for Seaborn Plots
Global styles are set for all Seaborn plots in the program, this will allow for uniformity within the program:
```
sns.set(style='darkgrid')
sns.set_palette("colorblind",3)
```

####  Creation of a DataFrame
The process in Analysis.py repeated and this DataFrame is further broken down into Species Specific Data Sets easier visualisation:
```
SetosaData = df[df.species == "setosa"]
VersicolorData = df[df.species == "versicolor"]
VirginicaData = df[df.species == "virginica"]
```

####  Creation of Histograms Comparing the Frequency of Sepal Length/Width and Petal Length/Width of Each of the Species
Histograms provide a visual interpretation of numerical data and are an excellent to highlight the normal distribution, outliers, skewness etc.<sup>[8](#myfootnote8)</sup> Histograms are created to allow for the quick comparison between the frequency of Sepal Length/Width and Petal Length/Width of each of the species.

To create a histogram comparing the frequency of Sepal Length/Width and Petal Length/Width of each of the species the following code is executed:
```
bins = np.linspace(0, 5, 30)
plt.hist(SetosaData.sepal_width, bins, alpha=0.5, label="Setosa")
plt.hist(VersicolorData.sepal_width, bins, alpha=0.5, label="Versicolor")
plt.hist(VirginicaData.sepal_width, bins, alpha=0.5, label="Virginica")
plt.xlabel("Sepal Width (Cm)", fontsize=12)
plt.ylabel("Frequency of Occurrence", fontsize=12)
plt.legend(loc='upper right')
plt.title("Species Sepal Width", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Histrogram Comparing the Frequency of Sepal Width of Each of the Species.png")
plt.show()
```
  * Note the above code creates a histogram comparing the frequency of Sepal Width of each of the species. To create a histogram comparing the frequency of Sepal Length and Petal Length/Width of each of the species the following changes would have to be made to the code:
    * **Sepal Length:** Replace sepal_width with sepal_length.
    * **Petal Width:** Replace sepal_width with petal_width.
    * **Petal Length:** Replace sepal_width with petal_length.

The following plots will be produced as a result of the above code:

<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Histrogram%20Comparing%20the%20Frequency%20of%20Sepal%20Length%20of%20Each%20of%20the%20Species.png"> &nbsp;<img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Histrogram%20Comparing%20the%20Frequency%20of%20Sepal%20Width%20of%20Each%20of%20the%20Species.png">

<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Histrogram%20Comparing%20the%20Frequency%20of%20Petal%20Length%20of%20Each%20of%20the%20Species.png"> <img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Histrogram%20Comparing%20the%20Frequency%20of%20Petal%20Width%20of%20Each%20of%20the%20Species.png">

####  Observations 
As seen from the above plots there is a concentration and overlap of the species within the Sepal Length (4-8 Cm) and Sepal Width (2-4.5 Cm) histograms. However in the Petal Length and Width histograms it can be seen that there is a differentiation between the Setosa species and the Versicolor and Virginica species.The Setosa species in the Petal Length and Width are concentrated in smaller size (Cm) than the other two species. 


####  Creation of Histograms complete with Density Plot Comparing the Sepal Length/Width and Petal Length/Width of Each of the Species
Similiar to the above, the following histograms compare the Sepal Length/Width and Petal Length/Width of each of the species with the addition of a density plot overlaid. 

A density plot is a smoothed, continuous version of a histogram estimated from the data. The density plot is a variation of a histogram that uses kernel smoothing to plot values, allowing for smoother distributions by smoothing out the noise.<sup>[9](#myfootnote9)</sup> 

An advantage of density plots is that due to thier shape the peaks help display where values are concentrated. Also they are better at determining the distribution shape because they are not affected by the number of bins used (each bar used in a typical histogram).<sup>[10](#myfootnote10)</sup> 

To create a histogram complete with density plot comparing the Sepal Length/Width and Petal Length/Width of each of the species the following code is executed:
```
sns.distplot(SetosaData.sepal_width, label="Setosa")
sns.distplot(VersicolorData.sepal_width, label="Versicolor")
sns.distplot(VirginicaData.sepal_width, label="Virginica")
plt.xlabel("Sepal Width (Cm)", fontsize=12)
plt.legend(loc='best')
plt.title("Histogram with the Density Plot for Sepal Width of each of the Species", fontsize=15)
plt.tight_layout()
plt.savefig("Visualisations/Histogram with the Density Plot Comparing the Sepal Width of Each of the Species.png")
plt.show()
```
  * Note the above code creates a histogram with a density plot comparing the Sepal Width of each of the species. To create a histogram comparing the  Sepal Length and Petal Length/Width of each of the species the following changes would have to be made to the code:
    * **Sepal Length:** Replace sepal_width with sepal_length.
    * **Petal Width:** Replace sepal_width with petal_width.
    * **Petal Length:** Replace sepal_width with petal_length.

The following plots will be produced as a result of the above code:

<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Histogram%20with%20the%20Density%20Plot%20Comparing%20the%20Sepal%20Length%20of%20Each%20of%20the%20Species.png"> &nbsp;<img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Histogram%20with%20the%20Density%20Plot%20Comparing%20the%20Sepal%20Width%20of%20Each%20of%20the%20Species.png">

<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Histogram%20with%20the%20Density%20Plot%20Comparing%20the%20Petal%20Length%20of%20Each%20of%20the%20Species.png"> <img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Histogram%20with%20the%20Density%20Plot%20Comparing%20the%20Petal%20Width%20of%20Each%20of%20the%20Species.png">

####  Observations 
As seen from the above plots the additon of the density plot offers greater clarity with regards areas of concentration. While in the previous histograms, within any areas of concentration it was very difficult to make obserations because the process of stacking bars on top of another created confusion with regards to the position one bar ended and another continued. Also the stacking bars on top of another created the illusions of different colours which some individuals may take to mean additional species. The addition of the density plots however, allows for easier observations because the continuous density lines help the eye keep the distributions separate and also do not change colour where overlapping occurs.

####  Creation of Boxplots Displaying the Distribution of the Data of Each of the Species
A boxplot (also known as a Box-and-Whisker Plot) displays a summary of a set of data containing the minimum, first quartile, median, third quartile and maximum. In a box plot, we draw a box from the first quartile to the third quartile. A vertical line goes through the box at the median. The whiskers go from each quartile to the minimum or maximum. Additionally, outliers (if present) are shown by points outside the minimum and maximum lines.<sup>[11](#myfootnote11)</sup> A boxplot is created for each of the species to display the distribution of data within each of the species and highlight any areas of commonality.

To create a boxplots displaying the distribution of the data of each of the species the following code is executed:
```
sns.boxplot(data=SetosaData, orient="h")
plt.xlabel("Size (Cm)", fontsize=12)
plt.ylabel("Setosa Data", fontsize=12)
plt.title("Distribution of Setosa Data", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Boxplot Displaying the Distribution of the Setosa Data.png")
plt.show()
```
  * Note the above code creates a boxplot displaying the distribution of the Setosa data. To create a a boxplot displaying the distribution of the data of the other two species the following changes would have to be made to the code:
    * **Versicolor:** Replace SetosaData with VersicolorData
    * **Virginica:** Replace SetosaData with VirginicaData.

The following plots will be produced as a result of the above code:

<img align="left" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Boxplot%20Displaying%20the%20Distribution%20of%20the%20Setosa%20Data.png"> <img align="center" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Boxplot%20Displaying%20the%20Distribution%20of%20the%20Versicolor%20Data.png"><img align="right" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Boxplot%20Displaying%20the%20Distribution%20of%20the%20Virginica%20Data.png">

####  Observations 
It can be seen from the above plots there does seem to be an overlap across the species within the Sepal Width as all the boxes are concentrated within the 3 Cm area. Also within the Sepal Length all the species minimums and maximums occupy within the 5.5-7 Cm area, while the Setosa species Petal Length and Width results are much smaller than the other two species. This reinforces the observations made from the histogram plots. It should also be noted that within each species at least one outlier is present. 


####  Creation of a Boxplot Comparing the Sepal Length/Width and Petal Length/Width of each of the Species
These boxplots draw on the observations made in the pervious two sets of plots to give a greater understanding into the relationship between the Sepal Length/Width and Petal Length/Width of each of the species.

To create a boxplot displaying the Sepal Length/Width and Petal Length/Width of each of the species the following code is executed:
```
sns.boxplot(x="species" , y="petal_length" , data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Length (Cm)", fontsize=12)
plt.title("Compare the Distributions of Petal Length", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Boxplot comparing the Distributions of Petal Length of Each Species.png")
plt.show()
```
  * Note the above code creates a Boxplot displaying the Petal Length of each of the species. To create a boxplot displaying the Petal Width and Sepal Length/Width of each of the species the following changes would have to be made to the code:
    * **Petal Width:** Replace petal_length with petal_width.
    * **Sepal Length:** Replace petal_length with sepal_length.
    * **Sepal Width:** Replace petal_length with sepal_width.

The following plots will be produced as a result of the above code:

<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Boxplot%20comparing%20the%20Distributions%20of%20Petal%20Length%20of%20Each%20Species.png"> &nbsp;<img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Boxplot%20comparing%20the%20Distributions%20of%20Petal%20Width%20of%20Each%20Species.png">
&nbsp;
<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Boxplot%20comparing%20the%20Distributions%20of%20Sepal%20Length%20of%20Each%20Species.png"> &nbsp;<img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Boxplot%20comparing%20the%20Distributions%20of%20Sepal%20Width%20of%20Each%20Species.png">

####  Observations 
Reinforcing our obserations from the pervious plots we can see in the boxplots that there is little or no overlap between measurements for Setosa as compared to the other two species.


####  Creation of a Violin Plot Comparing the Sepal Length/Width and Petal Length/Width of each of the Species
Very similiar to the above boxplot a violin plot depicts distributions of numeric data for one or more groups using density curves.<sup>[12](#myfootnote12)</sup> Within a violin plot the white dot represents the median value the thick black bar in the center represents the interquartile range, the thin black line represents the rest of the distribution except for points that are determined to be “outliers” using a method that is a function of the interquartile range. On each side of the black line is a Kernel Density Estimation (KDE) to show the distribution shape of the data. Wider sections of the violin plot represent a higher probability that members of the population will take on the given value, the skinnier sections represent a lower probability.<sup>[13](#myfootnote13)</sup>

To create a violin plot displaying the Sepal Length/Width and Petal Length/Width of each of the species the following code is executed:
```
sns.violinplot(x="species",y="petal_length",data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Length(Cm)", fontsize=12)
plt.title("Violin Plots of Petal Length", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Violin Plot of comparing the Petal Length of each of the Species.png")
plt.show()
```
  * Note the above code creates a violin plot displaying the Petal Length of each of the species. To create a violin plot displaying the Petal Width and Sepal Length/Width of each of the species the following changes would have to be made to the code:
    * **Petal Width:** Replace petal_length with petal_width.
    * **Sepal Length:** Replace petal_length with sepal_length.
    * **Sepal Width:** Replace petal_length with sepal_width.

The following plots will be produced as a result of the above code:

<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Violin%20Plot%20of%20comparing%20the%20Petal%20Length%20of%20each%20of%20the%20Species.png"> &nbsp;<img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Violin%20Plot%20of%20comparing%20the%20Petal%20Width%20of%20each%20of%20the%20Species.png">
&nbsp;
<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Violin%20Plot%20of%20comparing%20the%20Sepal%20Length%20of%20each%20of%20the%20Species.png"> &nbsp;<img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Violin%20Plot%20of%20comparing%20the%20Sepal%20Width%20of%20each%20of%20the%20Species.png">

####  Observations 
While the violin plot may be slightly more complex concept than a box plot to understand it does offer the advantage of adding the KDE.

From the above violin plots it can be seen that the Virginica has the highest median value in Petal Length, Petal Width and Sepal Length. While the Setosa has the highest Sepal Width median value. These observations are easier to make in a violin plot thanks to the white dot. 


####  Creation of a a Scatter Plot depicting the relationship between Sepal/Petal Length and Sepal/Petal Width of each of the Species
A scatter plot uses dots to represent values for two different numeric variables. The position of each dot on the horizontal and vertical axis indicates values for an individual data point. Scatter plots are used to observe relationships between variables.<sup>[14](#myfootnote14)</sup>

If the data points show an "up-hill" pattern from left to right, then there is a positive correlation between X & Y. Conversely if the pattern is "downhill" there is a negative correlation between X & Y. If the dats is scattered then there is no relationship between the X & Y.<sup>[15](#myfootnote15)</sup>

The creation of a scatter plot depicting the relationship between Sepal/Petal Length and Sepal/Petal will indicate if a positive or negtive correlation exisits within any of the species.

To create a scatter plot depicting the relationship between Sepal/Petal Length and Sepal/Petal Width of each of the species the following code is executed:
```
sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=f)
plt.xlabel("Petal Length(Cm)", fontsize=12)
plt.ylabel("Petal Width(Cm)", fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.title("Relationship Between Petal Length and Petal Width", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Scatter Plot depicting the relationship between Petal Length and Petal Width of each of the Species.png")
plt.show()
```
  * Note the above code creates a scatter plot depicting the relationship between Petal Length and Petal Width of each of the species. To create a scatter plot depicting the relationship between Sepal Length and Sepal Width of each of the species the following changes would have to be made to the code:
    * **Sepal Length:** Replace petal_length with sepal_length.
    * **Sepal Width:** Replace petal_length with sepal_width.

The following plots will be produced as a result of the above code:

<img align="left" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Scatter%20Plot%20depicting%20the%20relationship%20between%20Petal%20Length%20and%20Petal%20Width%20of%20each%20of%20the%20Species.png"> &nbsp;<img align="righ" width="425" height="425" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Scatter%20Plot%20depicting%20the%20relationship%20between%20Sepal%20Length%20and%20Sepal%20Width%20of%20each%20of%20the%20Species.png">

####  Observations 
From the scatter plots it can be seen that a positive correlation exists for all three species for the relationship between Petal Length and Petal Width. Also it can be seen that there is a large distinction between the Setosa species the other two species (Setosa occupys the lower left quartile for Petal Length and Petal Width and upper left quartile for Sepal Length and Sepal Width). It can also be argued that while differentiation exists between Versicolor and Virgnica for the relationship between Petal Length and Petal Width (apart from a few outliers), the relationship between Sepal Length and Sepal Width it does not exist. 


####  Creation of a KDE Plot of each of the Species displayig Sepal/Petal Length Vs. Sepal/Petal Width
A KDE (Kernel Density Estimate) plot is used for visualizing the probability density of a specific variable.
The plot can either be One-Dimensional or Two-Dimensional and is mainly used in the field of non-parametric analysis.<sup>[16](#myfootnote16)</sup>

The output for this KDE plot will be a Two-Dimensional representation of the relationship of the Sepal/Petal Length Vs. Sepal/Petal Width of each of the species.

To create a KDE plot of each of the species displayig Sepal/Petal Length Vs. Sepal/Petal Width the following code is executed:
```
sns.kdeplot(data=SetosaData[["sepal_length","sepal_width"]], cmap="Purples_d", shade=True, shade_lowest=False)
plt.xlabel("Sepal Length(Cm)")
plt.ylabel("Sepal Width(Cm)")
plt.title("KDE Plot of Setosa - Sepal Length Vs. Sepal Width", fontsize=18)
plt.savefig("Visualisations/KDE Plot of Setosa - Sepal Length Vs. Sepal Width.png")
plt.show()
```
  * Note the above code creates a KDE plot depicting the relationship between Sepal Length Vs. Sepal Width of the Setosa species. To create a KDE plot depicting the relationship between Sepal Length Vs. Sepal Width of the other two species the following changes would have to be made to the code:
    * **Versicolor:** Replace SetosaData[["sepal_length","sepal_width"]] with VersicolorData[["sepal_length","sepal_width"]].
    * **Virgnica:** Replace SetosaData[["sepal_length","sepal_width"]] with VirginicaData[["sep_length","sepal_width"]].
  * While to create a KDE Plot depicting the relationship between Petal Length Vs. Petal Width of the species the following changes would have to be made to the code:
    * **Setosa:** Replace SetosaData[["sepal_length","sepal_width"]] with SetosaData[["petal_length","petal_width"]].
    * **Versicolor:** Replace SetosaData[["sepal_length","sepal_width"]] with VersicolorData[["petal_length","petal_width"]].
    * **Virgnica:** Replace SetosaData[["sepal_length","sepal_width"]] with VirginicaData[["petal_length","petal_width"]].

The following plots will be produced as a result of the above code:

<img align="left" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/KDE%20Plot%20of%20Setosa%20-%20Sepal%20Length%20Vs.%20Sepal%20Width.png"> <img align="center" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/KDE%20Plot%20of%20Versicolor%20-%20Sepal%20Length%20Vs.%20Sepal%20Width.png"><img align="right" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/KDE%20Plot%20of%20Virginica%20-%20Sepal%20Length%20Vs.%20Sepal%20Width.png">
<img align="left" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/KDE%20Plot%20of%20Setosa%20-%20Petal%20Length%20Vs.%20Petal%20Width.png"> <img align="center" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/KDE%20Plot%20of%20Versicolor%20-%20Petal%20Length%20Vs.%20Petal%20Width.png"><img align="right" width="285" height="400" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/KDE%20Plot%20of%20Virginica%20-%20Petal%20Length%20Vs.%20Petal%20Width.png">

####  Observations 
The above KDE plots highlight the observations made in the pervious plots with regards to the Sepal/Petal Length Vs. Sepal/Petal Width of each of the species but offers the visualisation through a different perspective which some users may find helpful for highlighting trends/patterns.
  * Note the KDE plot could also have been constructed to include all species in one plot but due to the large overlaps this was decided against for aesthetic purposes. 
  * Please also note when running the plots the following message is observed: "UserWarning: Passing a 2D dataset for a bivariate plot is deprecated in favor of kdeplot(x, y), and it will cause an error in future versions. Please update your code." This error can appear when dealing with Two-Dimensional representations and users should be aware of this when running the program.

####  Creation of a Pairplot of the Data Set
A pairplot is a plot in which one variable in the same data row is matched with another variables value. Pairplots show all variables paired with all the other variables and allow users to see both distribution of single variables and relationships between two variables.<sup>[17](#myfootnote17)</sup> By creating a multigraph representations of the data it is easy for the user to identify the differing relationships between the variables.

To create a Pairplot of the Data Set the following code is executed:
```
g = sns.pairplot(data=f,hue="species")
g = g.map_upper(sns.scatterplot)
g = g.map_diag(plt.hist, histtype="step", linewidth=3)
g = g.map_lower(sns.kdeplot)
g = g.add_legend()
plt.tight_layout(rect=[0, 0, 0.90, 0.95])
plt.suptitle("Pair Plot for Dataset", fontsize = 20)
plt.savefig("Visualisations/Pairplot of the Data Set.png")
plt.show()
```
  * Note the above code creates a pairplot with scatterplots as the upper plots, stepped histrograms as the diagional plots and KDE plots as the lower plots. With a pairplot there is a lot of flexability with regards to the type of plots which can be used.

The following plots will be produced as a result of the above code:
<img align="center" width="950" height="950" img src="https://github.com/JPLee01/pandas-project/blob/master/Visualisations/Pairplot%20of%20the%20Data%20Set.png">

####  Observations
Within the pairplot seen above it can be stated the Setosa can be clearly distinguished from the other two species in each subplot. Within the Petal Length and Width this is particularly apparent. 

As seen with a pairplot the creation of a multigraph resperesntation of the data offers the user an overview of the data set. This it could be argued, would aid the user in identifying relationships within the data set. Pairplots are also seen as a useful tool within bivariate analysis. A pairplot can identify the bivariate relation between each variable and can be used in the construction of hypotheses of associations between variables.<sup>[18](#myfootnote18)</sup>


### 8.3 Interactive.py Program Explained
As seen above the [Interactive.py](https://github.com/JPLee01/pandas-project/blob/master/Interactive.py) program is primarily concerned with highlighting the potential and capability of the Pandas Profiling module.

Upon investigation into potential advanced uses of the Iris Data Set an article by Peter Nistrup<sup>[19](#myfootnote19)</sup> was discovered which spoke about the potential of the Pandas Profiling module. Upon further investigation a GitHub repository by sbrugman<sup>[20](#myfootnote20)</sup> was discovered which explained the Pandas Profiling module in great detail. These two references have been heavily used in the creation of the [Interactive.py](https://github.com/JPLee01/pandas-project/blob/master/Interactive.py) program.

The report produced by the program are saved in .html format within the repository. 

  * Note that the exisiting report in the repository will be overwritten as a new report generated through the program. 

#### Importing the Libraries
As well as the [Pandas](https://pandas.pydata.org/) library imported in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) and [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) programs the following extra library is imported to the Interactive.py program:
```
from pandas_profiling import ProfileReport
```

####  Creation of a DataFrame
The process in [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) is repeated for this program.

####  Creation of the Interactive Report
In order to create and save the interactive report the following code is executed:
```
profile = ProfileReport(df, title="Iris Data Interactive Report", html={'style':{'full_width':True}})
df.profile_report()
profile.to_file(output_file="Iris Data Interactive Report.html")
```
  * Note the above code requires the installation of the Pandas Profiling module by the user. If this is not present the program will not run and the report will not be generated. It is advised that if the the Pandas Profiling module is not installed, the detail instructions on sbrugman GitHub repository is followed<sup>[20](#myfootnote20)</sup>.

As a result of running the program the following interactive report is created:

<img align="center" width="550" height="550" img src="https://github.com/JPLee01/pandas-project/blob/master/Interactive-Report.gif">

The above example is a 30 second Gif highlighting the process of executing the Interactive.py program from the command line and interacting with the interactive report. As seen from the Gif the interactive report .

The process of uploading of a Gif to the Readme file can be seen in an article by Kelli Blaock.<sup>[21](#myfootnote21)</sup>

The [Iris Data Interactive Report](https://github.com/JPLee01/pandas-project/blob/master/Iris%20Data%20Interactive%20Report.html) is available online within the repository however due to it's size it can not be viewed through the GitHub website. It is recommended that should the report wished to be viewed the steps in [7.2  Running the Program](#7.2-Running-the-Program) are followed. 


### 8.4 AdvancedUse.py Program Explained
As seen above the [AdvancedUse.py](https://github.com/JPLee01/pandas-project/blob/master/AdvancedUse.py) program is concerned with the potential advanced use of the Iris Data Set. 

Machine learning is one area which has seen an explosion in recent years thanks to advances in technology. Machine learning is defined as an application of artificial intelligence (AI) that provides systems the ability to automatically learn and improve from experience without being explicitly programmed. Machine learning focuses on the development of computer programs that can access data and use it learn for themselves.<sup>[22](#myfootnote22)</sup> As seen in the article by Dan Shewan<sup>[23](#myfootnote23)</sup> a number of the top companies are beginning to employ machine learning into their operations. Within machine learning, the primary aim is to allow the computers learn automatically without human intervention or assistance and adjust actions accordingly. An example of the types of uses of machine learning can be seen below:

<img align="center" width="500" height="500" img src="https://www.houseofbots.com/images/news/3736/cover.png">

Within the Iris Data Set there is the potential to explore the possibilities machine learning can offer. This can be seen in the articles by Felipe Trindade<sup>[24](#myfootnote24)</sup> and Muller and Guido<sup>[25](#myfootnote25)</sup> which were used as inspirations for this program. 

####  Importing the Libraries
As well as the [Pandas](https://pandas.pydata.org/) and [Numpy](https://www.numpy.org/) libraries imported in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) and [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) programs the following extra libraries is imported to the AdvancedUse.py program:
```
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
```
####  Creation of a DataFrame
The process in [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) is repeated for this program.

####  Implementation of Machine Learning - K-Nearest Neighbors (KNN)
This program will look at the machine learning algorithm of K-Nearest Neighbors (KNN). KNN is a supervised machine learning algorithm that can be used to solve both classification and regression problems. It is a non-parametric method, where an unknown sample is classified according to a class belonging to the majority of its neighbors, i.e. if K (Number selected for nearest neighbors) = 1, then the case is simply assigned to the class of its nearest neighbor.<sup>[26](#myfootnote26)</sup> Around since the 1970's KNN can be used for both classification and regression predictive problems.<sup>[27](#myfootnote27)</sup> A visual representation of KNN can be viewed below:

<img align="center" width="500" height="500" img src="https://machinelearningknowledge.ai/wp-content/uploads/2018/08/KNN-Classification.gif">

As seen in the above Gif, the value designated to K has a profound effect on the result on the unknown sample classification. This can be seen in further detail below in which displays different outcomes as a result of different values for K:

<img width="600" height="600" img src="https://miro.medium.com/max/1400/0*6IVs874DUMvJh-f0.png">

Dhilip Subramanian in his article<sup>[28](#myfootnote28)</sup> highlights the importance for selecting the right value for K within a model. Choosing too small of a value: "can be noisy and will have a higher influence on the result", while a higher values will: "mean lower variance but increased bias" and also is "computationally expensive." The ideal figure he suggest when choosing the value of K is: "K = sqrt(N) where N stands for the number of samples in your training dataset". While also ensuring: "he value of K odd in order to avoid confusion between two classes of data."

As we have 150 samples of data (N), K is the sqrt(150), which is 12.24744874. However, as this is an even figure will we round up to 13 to ensure an odd figure. To initiate this the following code is entered:
```
knn = KNeighborsClassifier(n_neighbors=13)
```

####  Creation of the K-Nearest Neighbors Algorithm
Once the value for K has been identified the next step is to slice the DataFrame and to split the data columns (Sepal Length, Sepal Width, Petal Length, Petal Width) from the species column. The data columns once split is designated x, while the species column is designated y. This is achieved through the following code:
```
x = df.iloc[:, :-1].values
y = df.iloc[:, 4].values 
```

Once this is completed the DataFrame is divided into two subsets as training and test set. The trainng subset is used to train the model and the trained model is tested on the test subset. This is called cross validation. This is undertaken in order to check how accurately the classifying model is at predicting<sup>[29](#myfootnote29)</sup>. For simpliciity we will use the same 75/25 split as Felipe Trindade<sup>[24](#myfootnote24)</sup> did in his example. However it should be noted that various different splits may be used. To achieve this split the following code is entered:
```
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)
```
  * Please note the above training/test split splits arrays or matrices into random train and test subsets. If you don't specify a Random State number, then everytime the program is executed a new random value is generated and the train and test datasets would have different values each time. Due to the fact that the program will be run a number of times (by student and examiner) a Random State number is inserted this will ensure that the no matter how many times the program is executed the result would be the same .i.e, same values in train and test datasets. It also appears from research that the specific number entered for the random state is not of vital importance, more that a number is entered<sup>[30](#myfootnote30)</sup>.

Next the knn.fit function takes as arguments the array x_train (containing the training data) and the array y_train (containing the corresponding training labels).This way, the model is built on the training set<sup>[31](#myfootnote31)</sup>. This is achieved through the following code:
```
knn.fit(x_train, y_train)
```
Now predictions can be made using the model on any new data for which we might not know the correct labels.
To initiate new data the user will be asked to input a value for the Sepal Length, Sepal Width, Petal Length and Petal Width. A letter will then be designated for each input. This is achieved through the following code:
```
a = float(input("Please enter a Sepal Length(Cm): "))
b = float(input("Please enter a Sepal Width(Cm): "))
c = float(input("Please enter a Petal Length(Cm): "))
d = float(input("Please enter a Sepal Width(Cm): "))
```

Once all the relevant dimensions have been entered the are grouped together and designated "x_new", as can be seen by the following code:
```
x_new = np.array([[a, b, c, d]])
```

After this a prediction is made on the test set using predict() function based on the users inputs. The result of this prediction is then displayed to the user stating: 'Based on your input the predicted species is: ______'. This is achieved through the following code: as can be seen by the following code:
```
prediction = (knn.predict(x_new))
print("Based on your input the predicted species is:", prediction)
```

In order to offer reassurances to the user about the accuracy of the model the knn.score fuction is used to calculate the mean accuracy of the predicted result (Rounded to 3 decimal places). This result is then displayed to the user stating: 'The mean accuracy of this result is: ______'. This is achieved through the following code: 
```
Accuracy = round(knn.score(x_test, y_test),3)
print("The mean accuracy of this result is:", Accuracy)
```

####  Working Example
To demonstrate the model in action the following is an example of the results generated from the following measurments entered by the user: Sepal Length 5.8 cm, Sepal Width 2.7 cm, Petal Length 1.3 cm and Sepal Width 3.1 cm.
```
Please enter a Sepal Length(Cm): 5.8
Please enter a Sepal Width(Cm): 2.7
Please enter a Petal Length(Cm): 1.3
Please enter a Sepal Width(Cm): 3.1
Based on your input the predicted species is: ['setosa']
The mean accuracy of this result is: 0.974
```

As seen the model predicts based on the dimensions entered that the species would be Setosa and this would be accurate to 0.974 or 97.4%. 

Analysis of the scatter plots produced earlier can also be used to reinforced any predicions made by the model.

##  9 Summary, Conclusion and Future Possibilities for the Data Set
------------------------------------------------------------------------------------------------
####  Summary
Within the project, chapter 1 offered an introduction while chapter 2 outlined the files present within the projects repository. Chapter 3 investigated Fishers Iris Data Set, gave a background and described the four variable measurements of each data entry. Chapter 4 outlined the problem statement of the assignmnent, while chapter 5 dicussed previous case studies of the data set. Chapter 6 highlighted issues and inconsistencies with data set. Chpater 7 offered a user guide to downloading the repository, running the program and a description of the libraries used. Chapter 8 describeed the Python programs within the project and explained the results generated. Chapter 9 closed the project by offering a summary, conclusion and discussed future possibilities for the data set.

In summary it can be seen from this project that the Iris Data Set offers numberous opportunities to explore and visually represent the data. This is due to its one hundred and fifty data inputs spread over four variable measurements (Petal Length, Petal Width, Sepal length and Sepal Width) and broken into three species (Setosa, Versicolor and Virginica). 

The statistical summaries of the data set developed in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) program and outputted to the [Analysis.txt](https://github.com/JPLee01/pandas-project/blob/master/Analysis.txt) file offers the user numerical information about the data set. This information including; sample of the first 10 rows of data, sample of the last 10 rows of data and summary statistics of all the species etc. allows the user to seen a snapshot of the data and how it is structured.

The visualisations of the data set produced in the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program offers the user the ability to observe the data and discover noticable patterns or trends. The visualisations also offer the user the ability to search the data for frequency distributions, while also developing hypothesis with regards to species parameters.

The [Iris Data Interactive Report](https://github.com/JPLee01/pandas-project/blob/master/Iris%20Data%20Interactive%20Report.html) produced from the [Interactive.py](https://github.com/JPLee01/pandas-project/blob/master/Interactive.py) program highlights to the user the potential capabilities of the Pandas Profiling module. This offers the user the experience of gererating and interacting with a Pandas Profiling report, something which the author was not aware of prior to this project. 

The investigation of the K-Nearest Neighbors (KNN) algorithm in the [AdvancedUse.py](https://github.com/JPLee01/pandas-project/blob/master/AdvancedUse.py) program highlights to the user the possibility of implementing machine learning on the data set and the opportunities it can create. 

####  Conclusion
In conclusion within this project the author attempted to analyse the Iris Data Set using Python and a number of libraries for data analysis. As the author had no computing or data analysis experience prior to the commencement of the course, extensive research was undertaken. This resulted in the author gaining an experience, understanding and overall insight into data analysis. The author now feels a level of confidence with regards to data analysis which was not present before undertaking the project. In essence, the entire experience associated with the project can be summarised by the following Carly Fiorina quote *“The goal is to turn data into information, and information into insight”*<sup>[32](#myfootnote32)</sup>.

####  Future Possibilities for the Data Set
Due to time constraints, three areas the author was investigating were not implemented into the project. These included:
  1.  **The ability the export plots to a PDF file** - Similarly to the [Analysis.txt](https://github.com/JPLee01/pandas-project/blob/master/Analysis.txt) file created from the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) program the author attempted to create a PDF file in which the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) programs outputs would have produced to. This the author felt would have enhanced the project as it could offer the user the opportunity to create a download a file which contained all the plots. Unfortunately the author was not able to achieve this. The ability the export plots to a PDF file was discussed in a Data to Fish article which the author had used in the investigation<sup>[33](#myfootnote33)</sup>.
  2.  **Implementation of the Cufflinks library into the Project** - The ability to implement the cufflinks library the author felt would have greatly improved the project, particially data available through the plots. Despite repeated attempts the author was not able to successfully implement the library. The ability to implement the Cufflinks library was originally discovered by the author through a Peter Nistrup article<sup>[34](#myfootnote34)</sup>, and was further investigated through the official Cufflinks webpage<sup>[35](#myfootnote35)</sup>.
  3.  **Implementation of the Dash Platform into the Project** - Within the same Peter Nistrup article<sup>[34](#myfootnote34)</sup> the Dash Platform and its capabilities was also discovered. Similarly to implementing the Cufflinks library the author feels the implemetation of the Dash platform would have greatly enhanced the data analysis capability of the project. While the official Dash webpage<sup>[36](#myfootnote36)</sup> offers a guide regards implementation and use, the author felt this was perhaps beyond thier current technical capability, and would require further research to implement.

The author feels these three areas would have enhanced the project greatly should they have been implemented. If more time had been available it was the authors intention to implement all three areas fully into the project. 


##  10 References
------------------------------------------------------------------------------------------------

<a name="myfootnote1">1</a>: UCI Machine Learning Repository - Iris Data Set, <http://archive.ics.uci.edu/ml/datasets/Iris>

<a name="myfootnote2">2</a>: The Use of Multiple Measurements in Taxonomic Problems, <http://www.comp.tmu.ac.jp/morbier/R/Fisher-1936-Ann._Eugen.pdf>

<a name="myfootnote3">3</a>: Venkata Sai Reddy Avuluri - Exploratory Data Analysis of IRIS Data Set Using Python, <https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d>

<a name="myfootnote4">4</a>: Oluwasogo Oluwafemi Ogundowole - Basic Analysis of the Iris Data set Using Python, <https://medium.com/codebagng/basic-analysis-of-the-iris-data-set-using-python-2995618a6342>

<a name="myfootnote5">5</a>: Binu - Seaborn Matplotlib plot to visualize Iris data, <https://www.kaggle.com/biphili/seaborn-matplotlib-plot-to-visualize-iris-data>

<a name="myfootnote6">6</a>: Pandas Round Command, <https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.round.html>

<a name="myfootnote7">7</a>: How to redirect the print to a .txt file using the [Sys](https://docs.python.org/3/library/sys.html) module within Python, <https://stackoverflow.com/questions/7152762/how-to-redirect-print-output-to-a-file-using-python>

<a name="myfootnote8">8</a>: Histogram, <https://corporatefinanceinstitute.com/resources/excel/study/histogram/>

<a name="myfootnote9">9</a>: Will Koehrsen - Histograms and Density Plots in Python, <https://towardsdatascience.com/histograms-and-density-plots-in-python-f6bda88f5ac0>

<a name="myfootnote10">10</a>: The Data Visualisation Catalogue - Density Plot, <https://datavizcatalogue.com/methods/density_plot.html>

<a name="myfootnote11">11</a>: Boxplot, <https://www.tutorialspoint.com/matplotlib/matplotlib_box_plot.htm>

<a name="myfootnote12">12</a>:  Mike Yi - What is a Violin Plot?, <https://chartio.com/learn/charts/violin-plot-complete-guide/>

<a name="myfootnote13">13</a>: Joel Carron - Violin Plots 101: Visualizing Distribution and Probability Density, <https://mode.com/blog/violin-plot-examples>

<a name="myfootnote14">14</a>: Mike Yi - What is a Scatter Plot?, <https://chartio.com/learn/charts/what-is-a-scatter-plot/>

<a name="myfootnote15">15</a>: ASQ - What is a Scatter Diagram?, <https://asq.org/quality-resources/scatter-diagram>

<a name="myfootnote16">16</a>: Geeks for Geeks - KDE Plot Visualization with Pandas and Seaborn, <https://www.geeksforgeeks.org/kde-plot-visualization-with-pandas-and-seaborn/>

<a name="myfootnote17">17</a>: Will Koehrsen - Visualizing Data with Pairs Plots in Python, <https://towardsdatascience.com/visualizing-data-with-pair-plots-in-python-f228cf529166>

<a name="myfootnote18">18</a>: Alessandro Bertani et al. - How to describe Bivariate Data, <https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5864614/#__sec3title>

<a name="myfootnote19">19</a>: Peter Nistrup - Exploring your data with just 1 line of Python, <https://towardsdatascience.com/exploring-your-data-with-just-1-line-of-python-4b35ce21a82d>

<a name="myfootnote20">20</a>: sbrugman - GitHub Repository, <https://github.com/pandas-profiling/pandas-profiling>

<a name="myfootnote21">21</a>: Kelli Blaock - Demo your App in your GitHub README with an Animated GIF, <https://dev.to/kelli/demo-your-app-in-your-github-readme-with-an-animated-gif-2o3c>

<a name="myfootnote22">22</a>: Expert System - What is Machine Learning? A definition, <https://expertsystem.com/machine-learning-definition>

<a name="myfootnote23">23</a>: Dan Shewan - 10 Companies Using Machine Learning in Cool Ways, <https://www.wordstream.com/blog/ws/2017/07/28/machine-learning-applications>

<a name="myfootnote24">24</a>: Felipe Trindade - Start to learn Machine Learning with the Iris Flower Classification Challenge, <https://medium.com/gft-engineering/start-to-learn-machine-learning-with-the-iris-flower-classification-challenge-4859a920e5e3>

<a name="myfootnote25">25</a>: Muller and Guido - Introduction - Iris Dataset, <https://rpubs.com/nandong/imlp-ch1-iris>

<a name="myfootnote26">26</a>: Science Direct - K Nearest Neighbor Definition, <https://www.sciencedirect.com/topics/immunology-and-microbiology/k-nearest-neighbor>

<a name="myfootnote27">27</a>: Tavish Srivastva - Introduction to k-Nearest Neighbors, <https://www.analyticsvidhya.com/blog/2018/03/introduction-k-neighbours-algorithm-clustering/>

<a name="myfootnote28">28</a>: Dhilip Subramanian - A Simple Introduction to K-Nearest Neighbors Algorithm, <https://towardsdatascience.com/a-simple-introduction-to-k-nearest-neighbors-algorithm-b3519ed98e>

<a name="myfootnote29">29</a>: Kraj Education - Implementataion of Naive Bayes in python(using Sklearn), <https://kraj3.com.np/blog/2019/07/implementataion-of-naive-bayes-in-pythonusing-scikit-learn/>

<a name="myfootnote30">30</a>: Stack Overflow - Random state (Pseudo-random number) in Scikit learn, <https://stackoverflow.com/questions/28064634/random-state-pseudo-random-number-in-scikit-learn>

<a name="myfootnote31">31</a>: Avinash Navlani - KNN Classification using Scikit-learn, <https://www.datacamp.com/community/tutorials/k-nearest-neighbor-classification-scikit-learn>

<a name="myfootnote32">32</a>: Carly Fiorina - Quotes, <https://quotefancy.com/quote/1187260/Carly-Fiorina-The-goal-is-to-turn-data-into-information-and-information-into-insight>

<a name="myfootnote33">33</a>: Data to Fish - How to Export Matplotlib Charts to a PDF, <https://datatofish.com/export-matplotlib-pdf/>

<a name="myfootnote34">34</a>: Peter Nistrup - 7 things to quickly improve your Data Analysis in Python, <https://towardsdatascience.com/7-things-to-quickly-improve-your-data-analysis-in-python-3d434243da7>

<a name="myfootnote35">35</a>: Cufflinks Library, <https://plotly.com/python/cufflinks/>

<a name="myfootnote36">36</a>: Dash Platform, <https://plotly.com/dash/>


##  11 Bibliography
------------------------------------------------------------------------------------------------

Within the course of this project the following sources were also used for research purposes:

* CMD Line Tips - How to Make Boxplots in Python with Pandas and Seaborn?, <https://cmdlinetips.com/2018/03/how-to-make-boxplots-in-python-with-pandas-and-seaborn/>

* Code Cademy - Where do images get saved in Matplotlib when using savefig?, <https://discuss.codecademy.com/t/where-do-images-get-saved-in-matplotlib-when-using-savefig/353086>

* Corey Schafer - Matplotlib Tutorial (Part 2): Bar Charts and Analyzing Data from CSVs, <https://www.youtube.com/watch?v=nKxLfUrkLE8>

* CS Dojo - Intro to Data Analysis / Visualization with Python, Matplotlib and Pandas. Matplotlib Tutorial, <https://www.youtube.com/watch?v=a9UrKTVEeZA&t=747s>

* Dataquest - Pandas Cheat Sheet, Python for Data Science, <https://www.dataquest.io/blog/pandas-cheat-sheet/>

* Data Camp - Seabon Cheat Sheet, <https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf>

* Geeks for Geeks - Print lists in Python (4 Different Ways), <https://www.geeksforgeeks.org/print-lists-in-python-4-different-ways/>

* Geeks for Geeks - Python Pandas DataFrame, <https://www.geeksforgeeks.org/python-pandas-dataframe/>

* Github - Creating and highlighting Code Blocks, <https://help.github.com/en/github/writing-on-github/creating-and-highlighting-code-blocks>

* Github David Wells - Aligning images, <https://gist.github.com/DavidWells/7d2e0e1bc78f4ac59a123ddf8b74932d>

* Karlijn Willems - Pandas Tutorial: DataFrames in Python, <https://www.datacamp.com/community/tutorials/pandas-tutorial-dataframe-python>

* Keith Galli - Complete Python Pandas Data Science Tutorial! (Reading CSV/Excel files, Sorting, Filtering, Groupby), <https://www.youtube.com/watch?v=vmEHCJofslg&feature=youtu.be>

* Kite - How to import Stdout, <https://kite.com/python/docs/sys.stdout/>

* Kite - How to redirect print output to a text file in Python <https://kite.com/python/answers/how-to-redirect-print-output-to-a-text-file-in-python>

* Markdown Guide - Markdown Syntax, <https://www.markdownguide.org/basic-syntax/#overview>

* Mathplotlib - Tight Layout guide, <https://matplotlib.org/3.2.1/tutorials/intermediate/tight_layout_guide.html>

* note.nkmk.me - Pandas Head, Tail, Slice, <https://note.nkmk.me/en/python-pandas-head-tail/>

* Python Basics - Seaborn Distplot, <https://pythonbasics.org/seaborn-distplot/>

* Seaborn.boxplot, <https://seaborn.pydata.org/generated/seaborn.boxplot.html>

* Seaborn.kdeplot, <https://seaborn.pydata.org/generated/seaborn.kdeplot.html#seaborn-kdeplot>

* Seaborn.pairgrid, <https://seaborn.pydata.org/generated/seaborn.PairGrid.html>

* Seaborn.pairplot, <https://seaborn.pydata.org/generated/seaborn.pairplot.html>

* Seaborn.scatterplot, <https://seaborn.pydata.org/generated/seaborn.scatterplot.html>

* Seaborn - Visualizing the distribution of a Dataset, <https://seaborn.pydata.org/tutorial/distributions.html>

* Stack Overflow - Plot two histograms on single chart with Matplotlib, <https://stackoverflow.com/questions/6871201/plot-two-histograms-on-single-chart-with-matplotlib>

* Stack Overflow - Round each number in a Python Pandas data frame by 2 decimals, <https://stackoverflow.com/questions/25272024/round-each-number-in-a-python-pandas-data-frame-by-2-decimals>

* The Python Graph Gallery - Histogram with several variables, <https://python-graph-gallery.com/25-histogram-with-several-variables-seaborn/>

* Towards Data Science - Pandas DataFrame: Playing with CSV files, <https://towardsdatascience.com/pandas-dataframe-playing-with-csv-files-944225d19ff>