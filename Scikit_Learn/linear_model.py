from random import randint
from sklearn.linear_model import LinearRegression

TRAIN_SET_LIMIT = 1000
TRAIN_SET_COUNT = 100

TRAIN_INPUT = []
TRAIN_OUTPUT = []

for i in range(TRAIN_SET_COUNT):
    a = randint(0, TRAIN_SET_LIMIT)
    b = randint(0, TRAIN_SET_LIMIT)
    c = randint(0, TRAIN_SET_LIMIT)

    y = (10*a) + (2*b) + (3*c)

    TRAIN_INPUT.append([a, b, c])
    TRAIN_OUTPUT.append(y)

model = LinearRegression()
model.fit(TRAIN_INPUT, TRAIN_OUTPUT)

X_TEST = [[10, 20, 30]]
prediction = model.predict(X_TEST)

print("Prediction:", prediction)
print("Coefficients:", model.coef_)