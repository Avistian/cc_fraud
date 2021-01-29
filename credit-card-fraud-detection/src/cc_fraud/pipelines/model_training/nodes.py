import logging
from typing import Dict, List

import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import r2_score

def train_model(X_train: pd.DataFrame) -> DecisionTreeClassifier:
    """Train the linear regression model.

        Args:
            X_train: Training data of independent features.
            y_train: Training data for price.

        Returns:
            Trained model.

    """
    y_train = X_train["is_fraud"]
    X_train.drop(columns=["is_fraud"], axis=1, inplace=True)
    classifier = DecisionTreeClassifier()
    classifier.fit(X_train, y_train)
    return classifier

def evaluate_model(classifier: DecisionTreeClassifier, X_test: pd.DataFrame):
    """Calculate the coefficient of determination and log the result.

        Args:
            regressor: Trained model.
            X_test: Testing data of independent features.
            y_test: Testing data for price.

    """
    y_test = X_test["is_fraud"]
    X_test.drop(columns=["is_fraud"], axis=1, inplace=True)
    y_pred = classifier.predict(X_test)
    score = r2_score(y_test, y_pred)
    logger = logging.getLogger(__name__)
    logger.info("Model has a coefficient R^2 of %.3f.", score)