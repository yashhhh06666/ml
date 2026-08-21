from sklearn.neighbors import KNeighborsClassifier
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
    "Pass",
    "Pass"
]

#  Create KNN Model 
model = KNeighborsClassifier(n_neighbors=3)

# Train the model
model.fit(X, Y)

# new student data 
new_student = [[5.5, 78]]

# prediction
prediction = model.predict(new_student)
print("\n Predicted Result :", prediction[0])

#  Graph 
for i in range(len(X)):
    if Y[i] == "Pass":
        plt.scatter(X[i][0], X[i][1], marker='o', label='Pass' if i == 3 else "")
    else:
        plt.scatter(X[i][0], X[i][1], marker='o', label='Fail' if i == 0 else "")

plt.scatter(
    new_student[0][0],
    new_student[0][1],
    marker='*',
    s=200,
    label = "New Student"
)

plt.title('KNClassifier')
plt.xlabel(' Study Hours')
plt.ylabel('Attandance (%)') 
plt.legend()
plt.show()