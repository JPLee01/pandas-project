#John Paul Lee
#Analysis of Iris Data Set
#Visualisation of the Data Section
#Creation of Histograms and Scatter Plots

#Import Pandas for Data Management 
import pandas as pd

#Import Numpty for Analysis of the data 
import numpy as np

#Import matplotlib.pyplot and seaborn for Visualisation of the data 
import matplotlib.pyplot as plt
import seaborn as sns



#Set a global style for all the Seaborn Plots in the program
sns.set(style='darkgrid')
sns.set_palette("colorblind",3)

#Import the data
f = pd.read_csv("IrisData.csv")

#Create a DataFrame from the Csv file to allow for easier analysis
df = pd.DataFrame(f)

#Create Species Specific Data Sets to allow for easier visualisation
SetosaData = df[df.species == "setosa"]
VersicolorData = df[df.species == "versicolor"]
VirginicaData = df[df.species == "virginica"]


#Create a Histogram Comparing the Frequency of Sepal Width of Each of the Species
#Use Numpy Linspace command to set the start and end point as well as the specify the number of intervals (30 chosen to allow for 10 for each specie)
bins = np.linspace(0, 5, 30)
#Set the parameters for the Setosa Histogram
#Data is Sepal Width within the Setosa Data Set, above bins are imposed, alpha (transparency) is set and a label is added
plt.hist(SetosaData.sepal_width, bins, alpha=0.5, label="Setosa")
#Set the parameters for the Versicolor Histogram
plt.hist(VersicolorData.sepal_width, bins, alpha=0.5, label="Versicolor")
#Set the parameters for the Virginica Histogram
plt.hist(VirginicaData.sepal_width, bins, alpha=0.5, label="Virginica")
#Set the name and size of the X Label
plt.xlabel("Sepal Width (Cm)", fontsize=12)
#Set the name and size of the Y Label
plt.ylabel("Frequency of Occurrence", fontsize=12)
#Add a legend and locate it in the top right
plt.legend(loc='upper right')
#Set the name and size of the Title
plt.title("Species Sepal Width", fontsize=18)
#The tight_layout command is used to fit the Plot within the Figure
plt.tight_layout()
#The Figure is Saved as a .png file in the Visualisations folder and a name is given to it
plt.savefig("Visualisations/Histrogram Comparing the Frequency of Sepal Width of Each of the Species.png")
#The Figure is displayed
plt.show()


#Create a Histogram Comparing the Frequency of Sepal Length of Each of the Species
bins = np.linspace(0, 10, 30)
plt.hist(SetosaData.sepal_length, bins, alpha=0.5, label="Setosa")
plt.hist(VersicolorData.sepal_length, bins, alpha=0.5, label="Versicolor")
plt.hist(VirginicaData.sepal_length, bins, alpha=0.5, label="Virginica")
plt.xlabel("Sepal Length (Cm)", fontsize=12)
plt.ylabel("Frequency of Occurrence", fontsize=12)
plt.legend(loc='best')
plt.title("Species Sepal Length", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Histrogram Comparing the Frequency of Sepal Length of Each of the Species.png")
plt.show()

#Create a Histogram Comparing the Frequency of Petal Width of Each of the Species
bins = np.linspace(0, 3, 30)
plt.hist(SetosaData.petal_width, bins, alpha=0.5, label="Setosa")
plt.hist(VersicolorData.petal_width, bins, alpha=0.5, label="Versicolor")
plt.hist(VirginicaData.petal_width, bins, alpha=0.5, label="Virginica")
plt.xlabel("Petal Width (Cm)", fontsize=12)
plt.ylabel("Frequency of Occurrence", fontsize=12)
plt.legend(loc='upper right')
plt.title("Species Petal Width", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Histrogram Comparing the Frequency of Petal Width of Each of the Species.png")
plt.show()


#Create a Histogram Comparing the Frequency of Petal Length of Each of the Species
bins = np.linspace(0, 8, 30)
plt.hist(SetosaData.petal_length, bins, alpha=0.5, label="Setosa")
plt.hist(VersicolorData.petal_length, bins, alpha=0.5, label="Versicolor")
plt.hist(VirginicaData.petal_length, bins, alpha=0.5, label="Virginica")
plt.xlabel("Petal Length (Cm)", fontsize=12)
plt.ylabel("Frequency of Occurrence", fontsize=12)
plt.legend(loc='upper right')
plt.title("Species Petal Length", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Histrogram Comparing the Frequency of Petal Length of Each of the Species.png")
plt.show()

#Create a Histogram with the Density Plot Comparing the Sepal Width of Each of the Species
#Set the parameters for the Sepal Width Histogram with Density Plot
#Data selected is Sepal Width within the each of the Species Set and a label is added
sns.distplot(SetosaData.sepal_width, label="Setosa")
sns.distplot(VersicolorData.sepal_width, label="Versicolor")
sns.distplot(VirginicaData.sepal_width, label="Virginica")
#Set the name and size of the X Label
plt.xlabel("Sepal Width (Cm)", fontsize=12)
#Add a legend and locate it in the best location
plt.legend(loc='best')
#Set the name and size of the Title
plt.title("Histogram with the Density Plot for Sepal Width of each of the Species", fontsize=14)
#The tight_layout command is used to fit the Plot within the Figure
plt.tight_layout()
#The Figure is Saved as a .png file in the Visualisations folder and a name is given to it
plt.savefig("Visualisations/Histogram with the Density Plot Comparing the Sepal Width of Each of the Species.png")
#The Figure is displayed
plt.show()

#Create a Histogram with the KDE Comparing the Sepal Length of Each of the Species
sns.distplot(SetosaData.sepal_length, label="Setosa")
sns.distplot(VersicolorData.sepal_length, label="Versicolor")
sns.distplot(VirginicaData.sepal_length, label="Virginica")
plt.xlabel("Sepal Length (Cm)", fontsize=12)
plt.legend(loc='best')
plt.title("Histogram with the Density Plot for Sepal Length of each of the Species", fontsize=14)
plt.tight_layout()
plt.savefig("Visualisations/Histogram with the Density Plot Comparing the Sepal Length of Each of the Species.png")
plt.show()

#Create a Histogram with the Density Plot Comparing the Petal Width of Each of the Species
sns.distplot(SetosaData.petal_width, label="Setosa")
sns.distplot(VersicolorData.petal_width, label="Versicolor")
sns.distplot(VirginicaData.petal_width, label="Virginica")
plt.xlabel("Petal Width (Cm)", fontsize=12)
plt.legend(loc='best')
plt.title("Histogram with the Density Plot for Petal Width of each of the Species", fontsize=14)
plt.tight_layout()
plt.savefig("Visualisations/Histogram with the Density Plot Comparing the Petal Width of Each of the Species.png")
plt.show()

#Create a Histogram with the Density Plot Comparing the Petal Length of Each of the Species
sns.distplot(SetosaData.petal_length, label="Setosa")
sns.distplot(VersicolorData.petal_length, label="Versicolor")
sns.distplot(VirginicaData.petal_length, label="Virginica")
plt.xlabel("Petal Length (Cm)", fontsize=12)
plt.legend(loc='best')
plt.title("Histogram with the Density Plot for Petal Length of each of the Species", fontsize=14)
plt.tight_layout()
plt.savefig("Visualisations/Histogram with the Density Plot Comparing the Petal Length of Each of the Species.png")
plt.show()


#Create a Boxplot Displaying the Distribution of the Setosa Data
#Set the parameters for the Boxplot
#Set the data to be displayed in the Boxplot and it's orientation
sns.boxplot(data=SetosaData, orient="h")
#Set the name and size of the X Label
plt.xlabel("Size (Cm)", fontsize=12)
#Set the name and size of the Y Label
plt.ylabel("Setosa Data", fontsize=12)
#Set the name and size of the Title
plt.title("Distribution of Setosa Data", fontsize=18)
#The tight_layout command is used to fit the Plot within the Figure
plt.tight_layout()
#The Figure is Saved as a .png file in the Visualisations folder and a name is given to it
plt.savefig("Visualisations/Boxplot Displaying the Distribution of the Setosa Data.png")
#The Figure is displayed
plt.show()

#Create a Boxplot Displaying the Distribution of the Versicolor Data
sns.boxplot(data=VersicolorData, orient="h")
plt.xlabel("Size (Cm)", fontsize=12)
plt.ylabel("Versicolor Data", fontsize=12)
plt.title("Distribution of Versicolor Data", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Boxplot Displaying the Distribution of the Versicolor Data.png")
plt.show()

#Create a Boxplot Displaying the Distribution of the Virginica Data
sns.boxplot(data=VirginicaData, orient="h")
plt.xlabel("Size (Cm)", fontsize=12)
plt.ylabel("Virginica Data", fontsize=12)
plt.title("Distribution of Virginica Data", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Boxplot Displaying the Distribution of the Virginica Data.png")
plt.show()


#Create a Boxplot comparing the Distributions of Petal Length of Each Species
#Set the parameters for the Boxplot
#Set the X and Y Axes and the data to be used in the Boxplot
sns.boxplot(x="species" , y="petal_length" , data=f)
#Set the name and size of the X Label
plt.xlabel("Species", fontsize=12)
#Set the name and size of the Y Label
plt.ylabel("Petal Length (Cm)", fontsize=12)
#Set the name and size of the Title
plt.title("Compare the Distributions of Petal Length", fontsize=18)
#The tight_layout command is used to fit the Plot within the Figure
plt.tight_layout()
#The Figure is Saved as a .png file in the Visualisations folder and a name is given to it
plt.savefig("Visualisations/Boxplot comparing the Distributions of Petal Length of Each Species.png")
#The Figure is displayed
plt.show()

#Create a Boxplot comparing the Distributions of Petal Width of Each Species
sns.boxplot(x="species" , y="petal_width" , data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Width (Cm)", fontsize=12)
plt.title("Compare the Distributions of Petal Width", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Boxplot comparing the Distributions of Petal Width of Each Species.png")
plt.show()

#Create a Boxplot comparing the Distributions of Sepal Length of Each Species
sns.boxplot(x="species" , y="sepal_length" , data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepal Length (Cm)", fontsize=12)
plt.title("Compare the Distributions of Sepal Length", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Boxplot comparing the Distributions of Sepal Length of Each Species.png")
plt.show()

#Create a Boxplot comparing the Distributions of Sepal Width of Each Species
sns.boxplot(x="species" , y="sepal_width" , data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepal Width (Cm)", fontsize=12)
plt.title("Compare the Distributions of Sepal Width", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Boxplot comparing the Distributions of Sepal Width of Each Species.png")
plt.show()


#Create a Violin Plot of comparing the Petal Length of each of the Species
#Set the parameters for the Violin Plot
#Set the X and Y Axes and the data to be used in the Violin Plot 
sns.violinplot(x="species",y="petal_length",data=f)
#Set the name and size of the X Label
plt.xlabel("Species", fontsize=12)
#Set the name and size of the Y Label
plt.ylabel("Petal Length(Cm)", fontsize=12)
#Set the name and size of the Title
plt.title("Violin Plots of Petal Length", fontsize=18)
#The tight_layout command is used to fit the Plot within the Figure
plt.tight_layout()
#The Figure is Saved as a .png file in the Visualisations folder and a name is given to it
plt.savefig("Visualisations/Violin Plot of comparing the Petal Length of each of the Species.png")
#The Figure is displayed
plt.show()

#Create a Violin Plot of Petal Width of each of the Species
sns.violinplot(x="species",y="petal_width",data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Petal Width(Cm)", fontsize=12)
plt.title("Violin Plots of Petal Width", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Violin Plot of comparing the Petal Width of each of the Species.png")
plt.show()


#Create a Violin Plot of Sepalal Length of each of the Species
sns.violinplot(x="species",y="sepal_length",data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepal Length(Cm)", fontsize=12)
plt.title("Violin Plots of Sepal Length", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Violin Plot of comparing the Sepal Length of each of the Species.png")
plt.show()


#Create a Violin Plot of Sepalal Width of each of the Species
sns.violinplot(x="species",y="sepal_width",data=f)
plt.xlabel("Species", fontsize=12)
plt.ylabel("Sepal Width(Cm)", fontsize=12)
plt.title("Violin Plots of Sepal Width", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Violin Plot of comparing the Sepal Width of each of the Species.png")
plt.show()

#Create a Scatter Plot depicting the relationship between Petal Length and Petal Width of each of the Species
#Set the parameters for the Scatter Plot
#Set the X and Y Axes, the colmun of data to be used in the Scatter Plot 
sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=f)
#Set the name and size of the X Label
plt.xlabel("Petal Length(Cm)", fontsize=12)
#Set the name and size of the Y Label
plt.ylabel("Petal Width(Cm)", fontsize=12)
#Set the location and size of the Legend
plt.legend(loc='best', fontsize=10)
#Set the name and size of the Title
plt.title("Relationship Between Petal Length and Petal Width", fontsize=18)
#The tight_layout command is used to fit the Plot within the Figure
plt.tight_layout()
#The Figure is Saved as a .png file in the Visualisations folder and a name is given to it
plt.savefig("Visualisations/Scatter Plot depicting the relationship between Petal Length and Petal Width of each of the Species.png")
#The Figure is displayed
plt.show()


#Create a Scatter Plot depicting the relationship between Sepal Length and Sepal Width of each of the Species
sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=f)
plt.xlabel("Sepal Length(Cm)", fontsize=12)
plt.ylabel("Sepal Width(Cm)", fontsize=12)
plt.legend(loc='best', fontsize=10)
plt.title("Relationship Between Sepal Length and Sepal Width", fontsize=18)
plt.tight_layout()
plt.savefig("Visualisations/Scatter Plot depicting the relationship between Sepal Length and Sepal Width of each of the Species.png")
plt.show()

#Create a KDE Plot of Setosa - Sepal Length Vs. Sepal Width
#Set the parameters for the KDE Plot of Setosa - Sepal Length Vs. Sepal Width
#Data is Sepal Length and Sepal Width within the Setosa Data Set, colour and shading is set 
sns.kdeplot(data=SetosaData[["sepal_length","sepal_width"]], cmap="Purples_d", shade=True, shade_lowest=False)
#Set the name and size of the X Label
plt.xlabel("Sepal Length(Cm)")
#Set the name and size of the Y Label
plt.ylabel("Sepal Width(Cm)")
#Set the name and size of the Title
plt.title("KDE Plot of Setosa - Sepal Length Vs. Sepal Width", fontsize=18)
#The Figure is Saved as a .png file in the Visualisations folder and a name is given to it
plt.savefig("Visualisations/KDE Plot of Setosa - Sepal Length Vs. Sepal Width.png")
#The Figure is displayed
plt.show()

#Create a KDE Plot of Versicolor - Sepal Length Vs. Sepal Width
sns.kdeplot(data=VersicolorData[["sepal_length","sepal_width"]], cmap="plasma", shade=True, shade_lowest=False)
plt.xlabel("Sepal Length(Cm)")
plt.ylabel("Sepal Width(Cm)")
plt.title("KDE Plot of Versicolor - Sepal Length Vs. Sepal Width", fontsize=18)
plt.savefig("Visualisations/KDE Plot of Versicolor - Sepal Length Vs. Sepal Width.png")
plt.show()


#Create a KDE Plot of Virginica - Sepal Length Vs. Sepal Width
sns.kdeplot(data=VirginicaData[["sepal_length","sepal_width"]], cmap="Greens", shade=True, shade_lowest=False)
plt.xlabel("Sepal Length(Cm)")
plt.ylabel("Sepal Width(Cm)")
plt.title("KDE Plot of Virginica - Sepal Length Vs. Sepal Width", fontsize=18)
plt.savefig("Visualisations/KDE Plot of Virginica - Sepal Length Vs. Sepal Width.png")
plt.show()

#Create a KDE Plot of Setosa - Petal Length Vs. Petal Width
sns.kdeplot(data=SetosaData[["petal_length","petal_width"]], cmap="Purples_d", shade=True, shade_lowest=False)
plt.xlabel("Petal Length(Cm)")
plt.ylabel("Petal Width(Cm)")
plt.title("KDE Plot of Setosa - Petal Length Vs. Petal Width", fontsize=18)
plt.savefig("Visualisations/KDE Plot of Setosa - Petal Length Vs. Petal Width.png")
plt.show()

#Create a KDE Plot of Versicolor - Petal Length Vs. Petal Width
sns.kdeplot(data=VersicolorData[["petal_length","petal_width"]], cmap="plasma", shade=True, shade_lowest=False)
plt.xlabel("Petal Length(Cm)")
plt.ylabel("Petal Width(Cm)")
plt.title("KDE Plot of Versicolor - Petal Length Vs. Petal Width", fontsize=18)
plt.savefig("Visualisations/KDE Plot of Versicolor - Petal Length Vs. Petal Width.png")
plt.show()


#Create a KDE Plot of Virginica - Petal Length Vs. Petal Width
sns.kdeplot(data=VirginicaData[["petal_length","petal_width"]], cmap="Greens", shade=True, shade_lowest=False)
plt.xlabel("Petal Length(Cm)")
plt.ylabel("Petal Width(Cm)")
plt.title("KDE Plot of Virginica - Petal Length Vs. Petal Width", fontsize=18)
plt.savefig("Visualisations/KDE Plot of Virginica - Petal Length Vs. Petal Width.png")
plt.show()

#Create a Pairplot of the Data Set
#Set the parameters for the Pairplot
g = sns.pairplot(data=f,hue="species")
#Changing of the Upper Plots to Scatterplots
g = g.map_upper(sns.scatterplot)
#Changing of the Diagional Plots to a Stepped Histrogram
g = g.map_diag(plt.hist, histtype="step", linewidth=3)
#Changing of the Lower Plots to KDE Plots
g = g.map_lower(sns.kdeplot)
#Addition of a legend
g = g.add_legend()
#Tight layout to adjust space between elements, limit hight to 95% to allow room for the Title and 90% width to allow room for the Legend
plt.tight_layout(rect=[0, 0, 0.90, 0.95])
#Addition of a title at the top of the Plot
plt.suptitle("Pair Plot for Dataset", fontsize = 20)
#The Figure is Saved as a .png file in the Visualisations folder and a name is given to it
plt.savefig("Visualisations/Pairplot of the Data Set.png")
#The Figure is displayed
plt.show()
