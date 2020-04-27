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






import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style='darkgrid')
sns.set_palette("colorblind",3)

SetosaData = df[df.species == "setosa"]
VersicolorData = df[df.species == "versicolor"]
VirginicaData = df[df.species == "virginica"]


#Create a Histogram with the KDE for Sepal Length of each of the Species
#Set the parameters for the Sepal Length Histogram
#Data selected is Sepal Width within the each of the Species Set and a label is added
sns.distplot(SetosaData.sepal_length, label="Setosa")
sns.distplot(VersicolorData.sepal_length, label="Versicolor")
sns.distplot(VirginicaData.sepal_length, label="Virginica")
#Set the name and size of the X Label
plt.xlabel("Sepal Length (Cm)", fontsize=12)
#Add a legend and locate it in the best location
plt.legend(loc='best')
#Set the name and size of the Title
plt.title("Histogram with the KDE for Sepal Length of each of the Species", fontsize=16)
#The tight_layout command is used to fit the Plot within the Figure
plt.tight_layout()
#pp.savefig()
#The Figure is displayed
plt.show()


#Create a Histogram with the KDE for Sepal Width of each of the Species
sns.distplot(SetosaData.sepal_width, label="Setosa")
sns.distplot(VersicolorData.sepal_width, label="Versicolor")
sns.distplot(VirginicaData.sepal_width, label="Virginica")
plt.xlabel("Sepal Width (Cm)", fontsize=12)
plt.legend(loc='best')
plt.title("Histogram with the KDE for Sepal Width of each of the Species", fontsize=16)
plt.tight_layout()
#pp.savefig()
plt.show()

#Create a Histogram with the KDE for Petal Length of each of the Species
sns.distplot(SetosaData.petal_length, label="Setosa")
sns.distplot(VersicolorData.petal_length, label="Versicolor")
sns.distplot(VirginicaData.petal_length, label="Virginica")
plt.xlabel("Petal Length (Cm)", fontsize=12)
plt.legend(loc='best')
plt.title("Histogram with the KDE for Petal Length of each of the Species", fontsize=16)
plt.tight_layout()
#pp.savefig()
plt.show()

#Create a Histogram with the KDE for Petal Width of each of the Species
sns.distplot(SetosaData.petal_width, label="Setosa")
sns.distplot(VersicolorData.petal_width, label="Versicolor")
sns.distplot(VirginicaData.petal_width, label="Virginica")
plt.xlabel("Petal Length (Cm)", fontsize=12)
plt.legend(loc='best')
plt.title("Histogram with the KDE for Petal Width of each of the Species", fontsize=16)
plt.tight_layout()
#pp.savefig()
plt.show()