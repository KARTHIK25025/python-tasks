# ============================================================
# IMPORTING REQUIRED LIBRARIES
# ============================================================
import numpy as np                      # For numerical operations
import pandas as pd                     # For handling datasets in table form

# ============================================================
# LOADING THE DATASET
# ============================================================
dataset = pd.read_csv("kc_house_data.csv")   # Load house price dataset
print(dataset.head())                         # Show first 5 rows to understand data

# ============================================================
# SPLITTING FEATURES (INPUT) AND TARGET (OUTPUT)
# ============================================================

# X = input features used to predict price
X = dataset[['bedrooms','bathrooms','sqft_living','sqft_lot',
             'floors','condition','grade','sqft_basement',
             'yr_built','yr_renovated']].values

# y = target variable (what we want to predict)
y = dataset['price'].values

# Check shape of data (rows, columns)
print('-'*80)
print(f'Shape of X is {X.shape}\nShape of y is {y.shape}')

# ============================================================
# SPLITTING DATA INTO TRAINING AND TESTING SETS
# ============================================================
from sklearn.model_selection import train_test_split

# 80% training data, 20% testing data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

# ============================================================
# FEATURE SCALING (IMPORTANT FOR ML MODELS)
# ============================================================

# StandardScaler makes data mean = 0 and variance = 1
# Helps models like SVR, KNN perform better
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()

# Fit only on training data (learn scaling rules)
X_train = sc.fit_transform(X_train)

# Apply same transformation to test data
X_test = sc.transform(X_test)

# ============================================================
# IMPORT EVALUATION METRIC (FOR REGRESSION)
# ============================================================

# R2 Score tells how well model explains variance
from sklearn.metrics import r2_score

# ============================================================
# FUNCTION TO EVALUATE MODELS
# ============================================================

def evaluate(name, y_test, y_pred):
    """
    Prints R2 score of each model in a clean format
    """
    print('\n'+'-'*20+f' {name} '+'-'*20)
    print("Accuracy (R2 Score):", "{:.2f}".format(r2_score(y_test, y_pred)))

# ============================================================
# 1. LINEAR REGRESSION MODEL
# ============================================================

# Simple model assumes linear relationship between features and price
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(X_train, y_train)          # Train model
y_pred = model.predict(X_test)       # Predict on test data

evaluate("Linear Regression", y_test, y_pred)

# ============================================================
# 2. SUPPORT VECTOR REGRESSION (SVR)
# ============================================================

# Works well for complex relationships using hyperplanes
from sklearn.svm import SVR

model = SVR()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("Support Vector Regression", y_test, y_pred)

# ============================================================
# 3. DECISION TREE REGRESSOR
# ============================================================

# Splits data into decision rules (like flowchart)
from sklearn.tree import DecisionTreeRegressor

model = DecisionTreeRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("Decision Tree", y_test, y_pred)

# ============================================================
# 4. RANDOM FOREST REGRESSOR
# ============================================================

# Combines many decision trees for better accuracy
from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("Random Forest", y_test, y_pred)

# ============================================================
# 5. K-NEAREST NEIGHBORS (KNN)
# ============================================================

# Predicts based on nearest similar data points
from sklearn.neighbors import KNeighborsRegressor

model = KNeighborsRegressor(n_neighbors=5)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("KNN", y_test, y_pred)

# ============================================================
# 6. GRADIENT BOOSTING REGRESSOR
# ============================================================

# Builds models sequentially to fix errors of previous models
from sklearn.ensemble import GradientBoostingRegressor

model = GradientBoostingRegressor()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("Gradient Boosting", y_test, y_pred)

# ============================================================
# 7. RIDGE REGRESSION
# ============================================================

# Linear regression with regularization (prevents overfitting)
from sklearn.linear_model import Ridge

model = Ridge()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

evaluate("Ridge Regression", y_test, y_pred)