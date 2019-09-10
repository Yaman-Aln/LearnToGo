import numpy as np
import matplotlib.pyplot as plt
from LearnToGo.logistic_regression import sigmoid

def predict(w, b, X):
    '''
    Using sigmoid because in logistic regression, 0/1 is what we are seeking.
    Predict whether the label is 0 or 1 using learned logistic regression parameters (w, b)

    Arguments:
    w -- weights
    b -- bias
    X -- data of size

    Modules used:
    sigmoid

    Returns:
    Y_prediction -- a numpy array (vector) containing all predictions (0/1) for the examples in X
    '''

    m = X.shape[1]
    Y_prediction = np.zeros((1,m))
    w = w.reshape(X.shape[0], 1)

    # Compute vector "A" predicting the probabilities of a cat being present in the picture
    A = sigmoid.sigmoid(np.dot(w.T,X)+b)

    for i in range(A.shape[1]):

        # Convert probabilities A[0,i] to actual predictions p[0,i]
        if A[0,i]>=0.5:
            Y_prediction[0,i]=1
        else:
            Y_prediction[0,i]=0
        pass

    assert(Y_prediction.shape == (1, m))

    return Y_prediction