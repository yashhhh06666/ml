import numpy as np
from sklearn.neighbors import KNeighboursClassifier
import matplotlib.pyplot as plt

#Traning data 
X = [
    [2,60],
    [3,65],
    [4,70],
    [5,75],
    [6,80],
    [7,85],
    [8,90]
]

# Target value 
Y = [
    "Fail",
    "Fail",
    "Fail",
    "Pass",
    "Pass",
    "Pass"
]

#  Create KNN Model 
model = KNeighboursClassifier(n_neibhours = 3)

# Train the model
model.fit(X_train, Y_train)

# new student data 
new_student = [[5.5, 78]]

# prediction
prediction = model.predict(new_student)
print("\n Predicted Result :" prediction[0])

#  Graph 
for i in range(len(X)):
    if y[i]=="Pass":
        plt.scatter(X[i][0],X[i][1]), marker='o', label='pass' if i == 3 else "")
    else:
        plt.scatter(X[i][0],X[i][1]), marker='o', label='Fail' if i == 0 else "")

plt.scatter(
    new_student[0][0],
    new_student[0][1],
    marker=''
    s=200,
    label = "New Student"
)

plt.title('KNClassifier')
plt.xlabel(' Study Hours')
plt.ylabel('Attandance (%)') 
plt.legend()
plt.show()