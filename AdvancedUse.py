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

#Instantiate learning model (k = 1)
#knn = KNeighborsClassifier(n_neighbors=1)

#Import the data
f = pd.read_csv("IrisData.csv")

#Create a DataFrame from the Csv file to allow for easier analysis
df = pd.DataFrame(f)


#Slice the DataFrame up to but not inlcuding the last column (i.e. Sepal_length, Sepal_Width, Petal_Length and Petal_Width)
x = df.iloc[:, :-1].values
#Slice the DataFrame to inlcude the last column only (i.e. Species)
y = df.iloc[:, 4].values 

#Divide the DataFrame into two subset as training and test set (80% training, 20% test), set the Random State at 1
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.20, random_state=1)


#print("X Train Info:{}".format(x_train.shape))
#print("Y Train Info:{}".format(y_train.shape))


#print("X Test Info:{}".format(x_test.shape))
#print("Y Test Info:{}".format(y_test.shape))


#Use a K-Nearest Neighbors Classifier to make a prediction for a new data entry.
#One neighbor is chosen for this.
#knn = KNeighborsClassifier(n_neighbors=1)

knn.fit(x_train, y_train)

a = float(input("Please enter a Sepal Length: "))
b = float(input("Please enter a Sepal Width: "))
c = float(input("Please enter a Petal Length: "))
d = float(input("Please enter a Sepal Width: "))

x_new = np.array([[a, b, c, d]])

prediction = (knn.predict(x_new))

print("Based on your input the predicted Species is:", prediction)

Accuracy = knn.score(x_test, y_test)

print("The mean accuracy of this result is:", Accuracy)

