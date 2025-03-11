from sklearn.svm import SVR
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.preprocessing import StandardScaler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv(r"D:\Bioinformatics project\dataset\nanobodies_rigid.csv")

#Independent variable
X = df[['bsa', 'desolv', 'elec', 'vdw', 'Molecule name', 'caprieval_rank']]
#Dependent variable
y = df['dockq']



param_grid = {
    'C': [0.1, 1, 10],
    'epsilon': [0.01, 0.1, 1],
    'gamma': ['scale', 'auto']
}
# Hyperparameter tuning
svr = SVR(kernel='rbf')


# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, stratify=df['Molecule name'], random_state=42)

X_train = X_train.drop(['Molecule name', 'caprieval_rank'], axis=1)
X_test = X_test.drop(['Molecule name', 'caprieval_rank'], axis=1)

#Scaling 
X_scaler = StandardScaler()
y_scaler = StandardScaler()
# Fit the scaler on the training and test data
X_train_scaled = X_scaler.fit_transform(X_train)
X_test_scaled = X_scaler.transform(X_test)
y_train_scaled = y_scaler.fit_transform(y_train.values.reshape(-1, 1)).ravel()
#y_test_scaled = y_scaler.transform(y_test.values.reshape(-1, 1)).ravel()
#Grid search with 5-fold Cross Validation
grid_search = GridSearchCV(estimator=svr, param_grid=param_grid, cv=5, scoring='neg_mean_squared_error')
grid_search.fit(X_train_scaled, y_train_scaled)

    # Evaluate the best model on the test set
best_model = grid_search.best_estimator_
    # Make predictions on the test set
y_pred_scaled = best_model.predict(X_test_scaled)
y_pred = y_scaler.inverse_transform(y_pred_scaled.reshape(-1, 1))

#Ensuring y_test is reshaped
y_test = y_test.values.reshape(-1, 1)

#plot results
plt.scatter(y_test, y_pred)
plt.xlabel("Actual dockq")
plt.ylabel("Predicted dockq")
plt.title("Actual vs. Predicted dockq")
plt.savefig(r"D:\Bioinformatics project\Final python\Graphs\poly_Nanobodies_rigid.png")
plt.show()

test_mse = mean_squared_error(y_test, y_pred)
test_mae = mean_absolute_error(y_test, y_pred)
test_r2 = r2_score(y_test, y_pred)

# Print the results
print('best_params', grid_search.best_params_)
print('test_mse', test_mse)
print('test_mae', test_mae)
print('test_r2', test_r2)




