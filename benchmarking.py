from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from pmlb import fetch_data, classification_dataset_names

np.random.seed(31415)
logit_test_scores = []
gnb_test_scores = []

classification_dataset = "molecular_biology_promoters"
#classification_dataset = "postoperative_patient_data"
#classification_dataset = "biomed"

# Split the data into training, testing, and validation
X, y = fetch_data(classification_dataset, return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25)

# Create data structures
models = dict()
scores = []
model_names = []

# Add new models here!
models["LogisticRegression1"] = LogisticRegression(penalty='l2', tol=1e-3, C=0.1)

# Train models and evaluate on validation data
for model_name in models:
    model = models[model_name]
    model_names.append(model_name)
    model.fit(X_train, y_train)
    scores.append(model.score(X_val, y_val))

# Create a dataframe
df = {"Accuracy": scores, "Model": model_names}

# Plot our current models
print(scores)
sns.barplot(data=df, x="Model", y="Accuracy")
plt.ylabel('Test Accuracy')
plt.show()