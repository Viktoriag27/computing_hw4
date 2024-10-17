
##train_model: Function to train the model
from sklearn.linear_model import LogisticRegression

def train_model(X_train, y_train):
    model = LogisticRegression()
    model.fit(X_train, y_train)
    return model

##evaluate_model: Function to make predictions and compute ROC AUC score.
from sklearn.metrics import roc_auc_score

def evaluate_model(model, X_train, X_test, y_train, y_test):
    y_train_pred = model.predict_proba(X_train)[:, 1]
    y_test_pred = model.predict_proba(X_test)[:, 1]
    train_roc_auc = roc_auc_score(y_train, y_train_pred)
    test_roc_auc = roc_auc_score(y_test, y_test_pred)
    return train_roc_auc, test_roc_auc
