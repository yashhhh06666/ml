
from sklearn.svm import SVC
from matplotlib import pyplot as plt

X = ([[2, 60],
    [3, 65],
    [4, 70],
    [5, 75],
    [6, 80], 
    [7, 85],
    [8, 90]
 ])

Y = [
    "fail",
    "fail",
    "fail",
    "pass",   
    "pass",
    "pass",
    "pass"
]

model = SVC(kernel="linear")

model.fit(X, Y)

new_student = ([[5.5, 75]])

prediction = model.predict(new_student)

print ("\n Predicted Result :", prediction[0])
for i in range(len(X)):
    if Y[i] == "pass":
        plt.scatter(X[i][0], X[i][1], marker='o', label='Pass' if i == 3 else "")

    else:
        plt.scatter(X[i][0], X[i][1], marker='o', label='Fail' if i == 0 else "")  

plt.scatter(
    new_student[0][0],
    new_student[0][1],
    marker ="*",
    s = 200,
    label = "new_student"  
)

plt.xlabel('Study Hours')
plt.ylabel('Attendance (%)')
plt.title('SVM Classifier')
plt.savefig('svm_classifier.png')
plt.legend()
plt.show()