#Reading the dataset
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

data1=pd.read_csv("iris.csv")

#Converting categorical to numerical so we can use knn
data1['variety']=data1['variety'].map({'Setosa':0,'Versicolor':1,'Virginica':2})

#Choosing the features as x and the target as y
x=data1[['sepal.length','sepal.width','petal.length','petal.width']]
y=data1['variety']
print(data1)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=30) #split our data with test size of 20% 

knn=KNeighborsClassifier(n_neighbors=20) #build our knn classifier
knn.fit(x_train,y_train) #Training KNN classifier
y_pred=knn.predict(x_test)  #Testing
print('Acuuracy=',accuracy_score(y_pred,y_test))