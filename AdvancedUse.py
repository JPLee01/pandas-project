#John Paul Lee
#Analysis of Iris Data Set

#Created to explore the potential advanced use of the Iris Data Set - K-Nearest Neighbor Machine learning

#Import Pandas for Data Management 
import pandas as pd

#Import Numpty for Analysis of the data 
import numpy as np

#Import Train Test Split module from the Scikit-learn library to split the dataset
from sklearn.model_selection import train_test_split

#Import KNeighborsClassifier module from the Scikit-learn library to implement the K-Nearest Neighbor approach to Machine Learning
from sklearn.neighbors import KNeighborsClassifier

#Instantiate the learning model (K = 13)
knn = KNeighborsClassifier(n_neighbors=13)

#Import the data
f = pd.read_csv("IrisData.csv")

#Create a DataFrame from the Csv file to allow for easier analysis
df = pd.DataFrame(f)

#Slice the DataFrame up to but not inlcuding the last column (i.e. Sepal_length, Sepal_Width, Petal_Length and Petal_Width)
x = df.iloc[:, :-1].values

#Slice the DataFrame to inlcude the last column only (i.e. Species)
y = df.iloc[:, 4].values 

#Divide the DataFrame into two subsets; a Training and Test set (75% training, 25% test), set the Random State at 1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=1)

#The knn.fit function is used to train the model.
knn.fit(x_train, y_train)

#The user is asked to enter a value for the Sepal Length, Sepal Width, Petal Length and Petal Width
a = float(input("Please enter a Sepal Length(Cm): "))
b = float(input("Please enter a Sepal Width(Cm): "))
c = float(input("Please enter a Petal Length(Cm): "))
d = float(input("Please enter a Sepal Width(Cm): "))

#The users inputs are grouped 
x_new = np.array([[a, b, c, d]])

#A prediction is made based on the users inputs
prediction = (knn.predict(x_new))

#The result of the prediction is displayed
print("Based on your input the predicted Species is:", prediction)

#The mean accuracy of the predicted result is calculated and rounded to 3 decimal places
Accuracy = round(knn.score(x_test, y_test),3)

#The mean accuracy of the predicted result is displayed (rounded to 3 decimal places)
print("The mean accuracy of this result is:", Accuracy)

