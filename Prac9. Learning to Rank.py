#Implement a learning to rank algorithm (e.g., RankSVM or RankBoost).
#Train the ranking model using labelled data and evaluate its effectiveness.

import numpy as np
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import ndcg_score

# Example dataset
X = np.array([[3, 2, 1], [2, 1, 0], [0, 1, 2], [1, 2, 0], [2, 1, 3], [1, 0, 2]])
y = np.array([1, 0, 0, 1, 0, 1])

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train RankSVM model
model = SVC(kernel='linear', C=1.0)
model.fit(X_train, y_train)

# Evaluate model
ndcg = ndcg_score([y_test], [model.predict(X_test)])
print(f"NDCG Score: {ndcg:.4f}")
