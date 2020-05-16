# Survival Analysis for Deep Learning

This is a [tutorial on survival analysis](https://k-d-w.org/blog/2019/07/survival-analysis-for-deep-learning/), also referred to as time-to-event analysis or reliability analysis. You will learn how to train a convolutional neural network to predict time to a (generated) event from MNIST images, using a loss function specific to survival analysis.

There are two versions of the tutorial:

1. Using tf.Estimator and TensorFlow 1.X: [tutorial\_tf1.ipynb](https://nbviewer.jupyter.org/github/sebp/survival-cnn-estimator/blob/master/tutorial_tf1.ipynb)
2. Using Keras and TensorFlow 2.X: [tutorial\_tf2.ipynb](https://nbviewer.jupyter.org/github/sebp/survival-cnn-estimator/blob/master/tutorial_tf2.ipynb)


## Getting started

The easiest way to run this notebook is [Google Colaboratory](https://colab.research.google.com/github/sebp/survival-cnn-estimator/blob/master/tutorial_tf2.ipynb). If you want to run this notebook locally, you have to make sure the following dependencies are installed:

- [numpy](https://www.numpy.org/)
- [matplotlib](https://matplotlib.org/)
- [pandas](https://pandas.pydata.org/)
- [scikit-survival](https://github.com/sebp/scikit-survival/)
- [tensorflow](https://www.tensorflow.org/)
