import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def mean_squared_error(target, predicted):
    """
    Calculate Mean Squared Error for given predicted and truth values

    Parameters
    ----------
    target
        Array of ground truth values
    predicted
        Array of predicted values
    """
    return np.mean((predicted - target) ** 2)

def gredient_decent(weights, x_values, y_values, predicted, learning_rate=1e-05):
    """
    Runs Gradient decent on given data with provided weights.
    NOTE: Runs gradient decent on whole array, no batch formation is done.
    
    Parameters
    ----------
    weights
        Weights of the model, must be passed for each iteration
    x_values
        Array of feature values
    y_values
        Array of ground truth
    predicted
        Array of current prediction of model
    learning _rate
        Learning rate to be used for optimization
    """
    difference = predicted - y_values
    difference = np.multiply(difference, x_values)
    gradient = np.mean(difference, axis = 0)
    new_weights = weights - learning_rate * gradient.reshape(-1, 1)
    return new_weights