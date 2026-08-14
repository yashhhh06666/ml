import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
# 1. training data
# Hours studied
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
# Test scores
y = np.array([2, 4, 6, 8, 10])

# 2. Create a linear regression model
model = LinearRegression()
#3. Train the model
model.fit(X, y)

hours = float(input("Enter the number of hours studied: "))
# 4. Make a prediction
predicted_marks = model.predict([[hours]])

print("predicted marks :" + str(round(predicted_marks[0], 2)))

#6 Display model info.
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

#7. Calculate R-squared value
score = model.score(X, y)
print("R-squared value:", round(score, 2))

# 8 Plot the data and regression line
plt.scatter(X, y, color='blue', label='Data points')
plt.plot(X, model.predict(X), color='red', label='Regression line')
plt.xlabel('Hours Studied')
plt.ylabel('Test Scores')
plt.title('Linear Regression: Hours Studied vs Test Scores')
plt.legend()
plt.show()