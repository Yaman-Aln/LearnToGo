import numpy as np
import matplotlib.pyplot as plt
from LearnToGo.logistic_regression import optimize, predict

def model(X_train, Y_train, X_test, Y_test, num_iterations = 2000, learning_rate = 0.5, print_cost = False):
    """
    Builds the logistic regression model by calling the function implemented previously

    Arguments:
    X_train -- training set
    Y_train -- training labels represented by a numpy array (vector) of shape (1, m_train)
    X_test -- test set represented by a numpy array of shape (num_px * num_px * 3, m_test)
    Y_test -- test labels represented by a numpy array (vector) of shape (1, m_test)
    num_iterations -- hyperparameter representing the number of iterations to optimize the parameters
    learning_rate -- hyperparameter representing the learning rate used in the update rule of optimize()
    print_cost -- Set to true to print the cost every 100 iterations

    Modules used:
    optimize
    predict
    
    Returns:
    d -- dictionary containing information about the model.
    """

    ### START CODE HERE ###

    # initialize parameters with zeros
    w, b = np.zeros((X_train.shape[0],1)), 0

    # Gradient descent
    parameters, grads, costs = optimize.optimize(w, b, X_train, Y_train, num_iterations, learning_rate, print_cost)

    # Retrieve parameters w and b from dictionary "parameters"
    w = parameters["w"]
    b = parameters["b"]

    # Predict test/train set examples )
    Y_prediction_test = predict.predict(w, b, X_test)
    #Y_prediction_train = predict.predict(w, b, X_train)

    d = {"costs": costs,
         "Y_prediction_test": Y_prediction_test,
         #"Y_prediction_train" : Y_prediction_train,
         "w" : w,
         "b" : b,
         "learning_rate" : learning_rate,
         "num_iterations": num_iterations}
    print(d)
    return Y_prediction_test, d
