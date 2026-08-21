import numpy as np 
import matplotlib.pyplot as plt
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier, plot_tree

#  1. Create data

X = np.array([[2, 60],
              [3, 65],
              [4, 70],
              [5, 75],
              [6, 80], 
              [7, 85],
              [8, 90]
             ])

Y = np.array([0, 0, 0, 1, 1, 1, 1]) # 0 = Fail, 1 = Pass

model = DecisionTreeClassifier(
    criterion = 'gini',
    max_depth = 3,
    random_state=42

)

# Train the model   
model.fit(X, Y)

#  Predication 

new_student = np.array([[5, 75]])
prediction = model.predict(new_student)

if prediction[0] == 1:
    print("\n Predicted Result : Pass")
else:
    print("\n Predicted Result : Fail")

plt.figure(figsize=(12, 7))

plot_tree(model, feature_names=['Study Hours', 'Attendance (%)'], class_names=['Fail', 'Pass'], filled=True ,round=tree)

plt.title('Decision Tree Classifier')
plt.xlabel('Study Hours')
plt.ylabel('Attendance (%)')
plt.show

