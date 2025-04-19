# Perceptron Implementation

This project implements a simple Perceptron model using Python, NumPy, and Matplotlib. The perceptron is trained on random data to classify points based on a linear decision boundary defined by the equation `2*x1 + x2 - 1 = 0`.

## Description

The Perceptron is a basic neural network model used for binary classification. The implementation includes the following components:
- **Data Generation**: Random data points are generated, and their labels are computed based on the equation `2*x1 + x2 - 1 = 0`.
- **Neurone Class**: This class defines the Perceptron model, including:
  - Weights initialization
  - A step function as the activation function
  - Weight and bias updates during training
- **Training**: The perceptron model is trained on the generated data by updating weights and bias iteratively.
- **Error Plotting**: The evolution of the error rate is plotted during the training process to visualize how the model learns.

## Features

- Random data generation for binary classification
- Perceptron learning algorithm with weight and bias updates
- Plot of error rate evolution during training
- Test error evaluation after training

## Requirements

- Python 3.x
- NumPy
- Matplotlib

You can install the necessary libraries using pip:

```bash
pip install numpy matplotlib
