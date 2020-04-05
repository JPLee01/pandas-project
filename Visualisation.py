#John Paul Lee
#Analysis of Iris Data Set

#Visualisation of the Data Section
#Creation of Histograms and Scatter Plots

#Import Pandas for Data Management 
import pandas as pd

#Import Numpty for Analysis of the data 
import numpy as np

#Import Sys to allow the "Print Results" to be written to a Txt File
import sys

#Import matplotlib.pyplot, seaborn and polly.express for Visualisation of the data 
import matplotlib.pyplot as plt
import seaborn as sns

#Create a Txt File called Visualisation and excute the Write Function (Allows the "Print Results" to be written onto the Visualisation Txt File)
#sys.stdout = open("Visualisation.txt", "w")


#Import the data
f = pd.read_csv("IrisData.csv")

#Create a DataFrame from the Csv file to allow for easier analysis
df = pd.DataFrame(f)

#Create Species Specific Datasets to allow for easier visualisation
SetosaData = df[df.species == "setosa"]
VersicolorData = df[df.species == "versicolor"]
VirginicaData = df[df.species == "virginica"]

#Create a Histrogram Comparing the Frequency of Sepal Width of Each of the Species
bins = np.linspace(0, 5, 30)
plt.hist(SetosaData.sepal_width, bins, alpha=0.5, label="Setosa")
plt.hist(VersicolorData.sepal_width, bins, alpha=0.5, label="Versicolor")
plt.hist(VirginicaData.sepal_width, bins, alpha=0.5, label="Virginica")
plt.xlabel("Sepal Width (Cm)", fontsize=12)
plt.ylabel("Frequency of Occurrence", fontsize=12)
plt.legend(loc='upper right')
title="Species Sepal Width"
plt.title(title, fontsize=18)
plt.show()
######plt.savefig("Frequency of Sepal Width of Each of the Species.png", dpi=72,)#########


#Create a Histrogram Comparing the Frequency of Sepal Length of Each of the Species
bins = np.linspace(0, 10, 30)
plt.hist(SetosaData.sepal_length, bins, alpha=0.5, label="Setosa")
plt.hist(VersicolorData.sepal_length, bins, alpha=0.5, label="Versicolor")
plt.hist(VirginicaData.sepal_length, bins, alpha=0.5, label="Virginica")
plt.xlabel("Sepal Length (Cm)", fontsize=12)
plt.ylabel("Frequency of Occurrence", fontsize=12)
plt.legend(loc='best')
title="Species Sepal Length"
plt.title(title, fontsize=18)
plt.show()
######plt.savefig("Frequency of Sepal Length of Each of the Species.png", dpi=72,)#########

#Create a Histrogram Comparing the Frequency of Petal Width of Each of the Species
bins = np.linspace(0, 3, 30)
plt.hist(SetosaData.petal_width, bins, alpha=0.5, label="Setosa")
plt.hist(VersicolorData.petal_width, bins, alpha=0.5, label="Versicolor")
plt.hist(VirginicaData.petal_width, bins, alpha=0.5, label="Virginica")
plt.xlabel("Petal Width (Cm)", fontsize=12)
plt.ylabel("Frequency of Occurrence", fontsize=12)
plt.legend(loc='upper right')
title="Species Petal Width"
plt.title(title, fontsize=18)
plt.show()
######plt.savefig("Frequency of Petal Width of Each of the Species.png", dpi=72,)#########


#Create a Histrogram Comparing the Frequency of Petal Length of Each of the Species
bins = np.linspace(0, 8, 30)
plt.hist(SetosaData.petal_length, bins, alpha=0.5, label="Setosa")
plt.hist(VersicolorData.petal_length, bins, alpha=0.5, label="Versicolor")
plt.hist(VirginicaData.petal_length, bins, alpha=0.5, label="Virginica")
plt.xlabel("Petal Length (Cm)", fontsize=12)
plt.ylabel("Frequency of Occurrence", fontsize=12)
plt.legend(loc='upper right')
title="Species Petal Length"
plt.title(title, fontsize=18)
plt.show()
######plt.savefig("Frequency of Petal Lengthof Each of the Species.png", dpi=72,)#########


#Create a Boxplot Displaying the Distribution of the Setosa Data
sns.boxplot(data=SetosaData, orient="h", palette="Set1")
plt.xlabel("Size (Cm)", fontsize=12)
plt.ylabel("Setosa Data", fontsize=12)
title="Distribution of Setosa Data"
plt.title(title, fontsize=18)
plt.show()

#Create a Boxplot Displaying the Distribution of the Versicolor Data
sns.boxplot(data=VersicolorData, orient="h", palette="Set2")
plt.xlabel("Size (Cm)", fontsize=12)
plt.ylabel("Versicolor Data", fontsize=12)
title="Distribution of Versicolor Data"
plt.title(title, fontsize=18)
plt.show()

#Create a Boxplot Displaying the Distribution of the Virginica Data
sns.boxplot(data=VirginicaData, orient="h", palette="Set3")
plt.xlabel("Size (Cm)", fontsize=12)
plt.ylabel("Virginica Data", fontsize=12)
title="Distribution of Virginica Data"
plt.title(title, fontsize=18)
plt.show()


#Create a Boxplot comparing the Distributions of Petal Length of Each Species
sns.boxplot(x="species" , y="petal_length" , data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Length (Cm)", fontsize=12)
title="Compare the Distributions of Petal Length"
plt.title(title, fontsize=18)
plt.show()

#Create a Boxplot comparing the Distributions of Petal Width of Each Species
sns.boxplot(x="species" , y="petal_width" , data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Width (Cm)", fontsize=12)
title="Compare the Distributions of Petal Width"
plt.title(title, fontsize=18)
plt.show()

#Create a Boxplot comparing the Distributions of Sepal Length of Each Species
sns.boxplot(x="species" , y="sepal_length" , data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepal Length (Cm)", fontsize=12)
title="Compare the Distributions of Sepal Length"
plt.title(title, fontsize=18)
plt.show()

#Create a Boxplot comparing the Distributions of Sepal Width of Each Species
sns.boxplot(x="species" , y="sepal_width" , data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepal Width (Cm)", fontsize=12)
title="Compare the Distributions of Sepal Width"
plt.title(title, fontsize=18)
plt.show()


#Create a Violin Plot of comparing the Petal Length of each of the Species
sns.violinplot(x="species",y="petal_length",data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Length(Cm)", fontsize=12)
title="Violin Plots of Petal Length"
plt.title(title, fontsize=18)
plt.show()

#Create a Violin Plot of Petal Width of each of the Species
sns.violinplot(x="species",y="petal_width",data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Width(Cm)", fontsize=12)
title="Violin Plots of Petal Width"
plt.title(title, fontsize=18)
plt.show()


#Create a Violin Plot of Sepalal Length of each of the Species
sns.violinplot(x="species",y="sepal_length",data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepalal Length(Cm)", fontsize=12)
title="Violin Plots of Sepalal Length"
plt.title(title, fontsize=18)
plt.show()


#Create a Violin Plot of Sepalal Width of each of the Species
sns.violinplot(x="species",y="sepal_width",data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepalal Width(Cm)", fontsize=12)
title="Violin Plots of Sepalal Width"
plt.title(title, fontsize=18)
plt.show()


#Create a Scatter plot depicting the relationship between Sepal Length and Sepal Width of the Species
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=f)
plt.xlabel("Sepal Length(Cm)", fontsize=12)
plt.ylabel("Sepal Width(Cm)", fontsize=12)
plt.legend(loc='best', fontsize=10)
title="Relationship Between Sepal Length and Sepal Width"
plt.title(title, fontsize=18)
plt.show()


#Create a Scatter plot depicting the relationship between Petal Length and Petal Width of the Species
sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=f)
plt.xlabel("Petal Length(Cm)", fontsize=12)
plt.ylabel("Petal Width(Cm)", fontsize=12)
plt.legend(loc='best', fontsize=10)
title="Relationship Between Petal Length and Petal Width"
plt.title(title, fontsize=18)
plt.show()




#References:
#General Reference: https://www.youtube.com/watch?v=nKxLfUrkLE8
#General Reference: https://www.youtube.com/watch?v=a9UrKTVEeZA&t=747s
#Violin Plot: https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d
#Plotting of two Histrograms on a Single Chart: https://stackoverflow.com/questions/6871201/plot-two-histograms-on-single-chart-with-matplotlib
#Seabon Cheat Sheet: https://s3.amazonaws.com/assets.datacamp.com/blog_assets/Python_Seaborn_Cheat_Sheet.pdf
#Use of plotly.express for Scatter Plots: https://coderzcolumn.com/tutorials/data-science/build-dashboard-using-python-dash-plotly-and-deploy-online-pythonanywhere
#Use of plotly.express  advanced/interactive Plots: https://plotly.com/python/plotly-express/
#Box Plots: https://cmdlinetips.com/2018/03/how-to-make-boxplots-in-python-with-pandas-and-seaborn/
#Box Plots: https://seaborn.pydata.org/generated/seaborn.boxplot.html
#Scatterplots: https://seaborn.pydata.org/generated/seaborn.scatterplot.html