import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

data = pd.read_csv('student_data.csv')

#  display the data 

print ("Dataset:")
print (data)

# Input VAr.
X = data[['hours']]

# Target Var.
Y = data['Result']

# Split DAta into traning and testing data 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Creat a Logistic reg.
model = LogisticRegression()

# Train the model
model.fit(X_train, Y_train)

# Predicit  test data 
y_pred = model.predict(X_test)

# Cal. acc.
accuracy = accuracy_score(Y_test, y_pred)

print ("\n Actual Values:")
print (Y_test.values)
print ("\n Predicted Values:")
print (y_pred)

print ("\n Accuracy:", accuracy)

#  Confusion Matrix
cm = confusion_matrix(Y_test, y_pred)
print ("\n Confusion Matrix:")
print (cm)

#  Predict for a new student result
new_student = [[5]]
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

print("\n Predicted Result for new student:")
if prediction[0] == 1:
    print("Pass")
else:
    print("Fail")   

print("\n Probability of Passing:", round(probability[0][1] * 100, 2), "%")

#  Graph

X_range = np.linspace(data['Hours'].min(), data['Hours'].max(), 100).reshape(-1, 1)

#  Cal. Probabilitie

probabilities = model.predict_proba(X_range)[:, 1]

#  Plot Actual Data
plt.scatter(data['Hours'], data['Result'], color='blue', label='Actual Data')

#  Plot Logistic Regression Curve
plt.plot(X_range, probabilities, color='red', label='Logistic Regression Curve')

#  Add label title 
plt.title('Logistic Regression Student pass/fail')
plt.xlabel('Hours Studied')
plt.ylabel('Probability of Passing')    

# add grid and legend 
plt.grid(True)
plt.legend()

#  Display Graph 
plt.show()

