import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1 Create a sample dataset
data = {
    'Area': [1500, 1600, 1700, 1800, 1900],
    'Bedrooms': [3, 3, 4, 4, 5],
    'Age': [10,8,9,4,6,5],
    'Price': [300000, 320000, 340000, 360000, 380000]
}

# convert data into dataframe

df = pd.DataFrame(data)

#independent var.
X = df[['Area', 'Bedrooms', 'Age']]

# Dependent Var.
Y = df['Price']

# Split DAta into traning and testing data 
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)   

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, Y_train)
y_pred = model.predict(X_test)
print("Predicted Price:",list(y_pred))

# Cal. Model Performance 
mse = mean_squared_error(Y_test, y_pred)
r2 = r2_score(Y_test, y_pred)

print("\nMean Squared Error:", mse)
print("R-squared Score:", r2)

# predict price for a new house 
new_house = [[2500, 4, 2]]
pred_price = model.predict(new_house)

print("\nPredicted price for new house", pred_price[0])