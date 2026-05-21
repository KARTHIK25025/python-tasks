import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load the Dataset
# Ensure the CSV file is in the same directory as this script
file_name = 'creditcard.csv'
print(f"Loading dataset: {file_name}...\n")
df = pd.read_csv(file_name)

# 2. Preprocess the Data
# 'Time' and 'Amount' need to be scaled so they don't overpower the V1-V28 features
print("Scaling Time and Amount features...")
scaler = StandardScaler()
df['scaled_amount'] = scaler.fit_transform(df['Amount'].values.reshape(-1, 1))
df['scaled_time'] = scaler.fit_transform(df['Time'].values.reshape(-1, 1))

# Drop the original unscaled columns
df.drop(['Time', 'Amount'], axis=1, inplace=True)

# 3. Split the Data (Features vs Target)
X = df.drop('Class', axis=1)
y = df['Class']

# Split into 80% training and 20% testing
# stratify=y ensures the 1.5% fraud rate is maintained in both train and test sets
print("Splitting data into training and testing sets...\n")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# ---------------------------------------------------------
# Algorithm 1: Logistic Regression (The Baseline)
# ---------------------------------------------------------
print("--- Training Algorithm 1: Logistic Regression ---")
log_reg = LogisticRegression(max_iter=1000)
log_reg.fit(X_train, y_train)

# Predict and Evaluate
y_pred_log = log_reg.predict(X_test)
print("\nConfusion Matrix (Logistic Regression):")
print(confusion_matrix(y_test, y_pred_log))
print("\nClassification Report (Logistic Regression):")
print(classification_report(y_test, y_pred_log))


# ---------------------------------------------------------
# Algorithm 2: Random Forest (The Ensemble Model)
# ---------------------------------------------------------
print("\n--- Training Algorithm 2: Random Forest ---")
# n_estimators=100 means it builds 100 decision trees
rf_clf = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
rf_clf.fit(X_train, y_train)

# Predict and Evaluate
y_pred_rf = rf_clf.predict(X_test)
print("\nConfusion Matrix (Random Forest):")
print(confusion_matrix(y_test, y_pred_rf))
print("\nClassification Report (Random Forest):")
print(classification_report(y_test, y_pred_rf))

print("\nProcess Complete! Look at the 'Recall' for Class 1 to see how many frauds were caught.")