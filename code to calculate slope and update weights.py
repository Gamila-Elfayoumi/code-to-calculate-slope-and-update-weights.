# Import the NumPy library
import numpy as np

# Define the variables
# weights: a NumPy array of the weights of the linear regression model
weights = np.array([1, 2])
# input_data: a NumPy array of the input data
input_data = np.array([3,4])
# traget: the target value
traget = 6
# learning_rate: the learning rate of the gradient descent algorithm
learning_rate = 0.01

# Calculate the predictions of the model
# This is the equation for a linear regression model:
# y = wx + b
preds = (weights * input_data).sum()

# Calculate the error of the model
# This is the difference between the predictions and the target value
error = preds - traget

# Calculate the gradient of the error with respect to the weights
# This is the equation for the gradient of the error function for a linear regression model
gradient = 2 * input_data * error
print ("The slope is the array",gradient)

# Update the weights of the model using the gradient descent algorithm
# This is the update rule for the gradient descent algorithm
weights_update = weights - learning_rate * gradient

# Calculate the new predictions of the model
preds_update = (weights_update * input_data).sum()

# Calculate the new error of the model
error_update = preds_update - traget

# Print the error of the model before and after updating the weights
print('Error before updating the weights:', error)
print('Error after updating the weights:', error_update)