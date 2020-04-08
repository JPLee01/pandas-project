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

As part of the assignmnent the student was given a set of instruction which can be viewed [here](https://github.com/JPLee01/pandas-project/blob/master/Project%20Instructions.pdf). As seen, within the instrctions a problem statement was printed. It stated that this project will invovle an analysis of the Iris data set. Python code will be utilised for this analysis and the student will be required to give explanations of the python code. The problem statement also explained it was required for the project that a program(s) be created that:
* outputs a summary of each variable to a single text file,
* saves a histogram of each variable to png files, and
* outputs a scatter plot of each pair of variables.

## 5 Issues and Inconsistencies with Data Set

It should be noted that there are three inconsistencies between the data set sourced from UCI[1](#references) and the data set presented by Fisher[2](#references). These three inconsistencies are as follows:
1.  35th sample: the fourth feature is given as "0.1" where Fisher had originally given "0.2".
2.  38th sample: the second feature is given as "3.1" where Fisher had originally given "3.6".
3.  38th sample: the third feature is given as "1.5" where Fisher had originally given "1.4".

Please be advised that these three errors have not been rectified in the data set analysed.

##  6 User Guide

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
3.  Run the program by typing:  **python  *programs_name*.py**

### 6.3 Libaries
The following Python libraries were used in the writing of the programs code and are required to successfully run the programs:
* [Numpy](https://www.numpy.org/) - Used for mathematical functions in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) and [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) programs.
* [Pandas](https://pandas.pydata.org/) - Used for import, management, data manipulation and analysis in both the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) and [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) programs.
* [Matplotlib.pyplot](https://matplotlib.org/tutorials/introductory/pyplot.html) - Used for the manipulation of elements and the creation of certain plots graphs, plots and charts within the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program.
* [Seaborn](https://seaborn.pydata.org/) - Used for the creation and manipulation of all plots in the [Visualisation.py](https://github.com/JPLee01/pandas-project/blob/master/Visualisation.py) program. (Seaborn allows for the extetion of the functionality of Matplotlib).
* [Sys](https://docs.python.org/3/library/sys.html) - Used for the creation and writing of text files in the [Analysis.py](https://github.com/JPLee01/pandas-project/blob/master/Analysis.py) program.



References
------------------------------------------------------------------------------------------------

1.  UCI Machine Learning Repository -- Iris Data Set, [[http://archive.ics.uci.edu/ml/datasets/Iris]{.underline}](http://archive.ics.uci.edu/ml/datasets/Iris)

2.  The Use of Multiple Measurements in Taxonomic Problems, <http://www.comp.tmu.ac.jp/morbier/R/Fisher-1936-Ann._Eugen.pdf>

3.  
