import numpy as np
import matplotlib.pyplot as plt
from LearnToGo.logistic_regression import sigmoid
def propagate(w, b, X, Y):
    """
    Implements the cost function and its gradient for the propagation

    Arguments:
    w -- weights, a numpy array of size (num_px * num_px * 3, 1)
    b -- bias, a scalar
    X -- data of size (num_px * num_px * 3, number of examples)
    Y -- true "label" vector (containing 0 if non-cat, 1 if cat) of size (1, number of examples)

    Modules used:
    sigmoid
    
    Return:
    cost -- negative log-likelihood cost for logistic regression
    dw -- gradient of the loss with respect to w, thus same shape as w
    db -- gradient of the loss with respect to b, thus same shape as b

    """

    m = X.shape[1]

    # FORWARD PROPAGATION (FROM X TO COST)
    A = sigmoid.sigmoid(np.dot(w.T,X).reshape(1,X.shape[1])+b)                # compute activation
    cost = (-1/m)*np.sum(np.multiply(Y,np.log(A))+np.multiply((1-Y),(np.log(1-A))))                                # compute cost

    # BACKWARD PROPAGATION (TO FIND GRAD)
    dw = (1/m)*np.dot(X,((A-Y).T))
    db = (1/m)*np.sum(A-Y)

    assert(dw.shape == w.shape)
    assert(db.dtype == float)
    cost = np.squeeze(cost)
    assert(cost.shape == ())

    grads = {"dw": dw,
             "db": db}

    return grads, cost
