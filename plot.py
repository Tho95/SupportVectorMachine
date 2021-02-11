# module for plotting data

import seaborn as sns
import matplotlib.pyplot as plt

#we want to find a way to plot the categorical data

def target(X):
    '''function to plot how often the target variable is setosa versicolor or virginica'''
    sns.countplot(x='target',data= X)
    plt.title('Number of flowers in the dataset')
    plt.show()

def count(X):
    '''function to plot the count of the state of variables against the target'''
    fig, axes = plt.subplots(2, 2, figsize=(16, 8))
    fig.suptitle('flower type')
    sns.countplot(ax=axes[0, 0],x='sepal length (cm)', hue = 'target', data = X)
    sns.countplot(ax=axes[0, 1], x='sepal width (cm)', hue='target', data=X)
    sns.countplot(ax=axes[1, 1], x='petal length (cm)', hue='target', data=X)
    sns.countplot(ax=axes[1, 0], x='petal width (cm)', hue='target', data=X)
    plt.xticks(rotation=90)
    plt.show()

def scatter(X):
    fig, axes = plt.subplots(1, 2, figsize=(16, 8))
    fig.suptitle('flower type')
    #print(X['sepal length (cm)'].shape)
    #print(X['sepal width (cm)'].shape)
    sns.scatterplot(ax= axes[0], data= X,  x= 'sepal length (cm)', y= 'sepal width (cm)', hue = 'target')
    sns.scatterplot(ax=axes[1], data=X, x='petal length (cm)', y='petal width (cm)', hue='target')
    plt.show()

def swarm(X):
    fig, axes = plt.subplots(2, 2, figsize=(16, 8))
    fig.suptitle('flower type')

    sns.swarmplot(ax=axes[0, 0], x='target', y ='sepal length (cm)', data=X)
    sns.swarmplot(ax=axes[0, 1], x='target', y='sepal width (cm)', data=X)
    sns.swarmplot(ax=axes[1, 0], x='target', y='petal length (cm)', data=X)
    sns.swarmplot(ax=axes[1, 1], x='target', y='petal width (cm)', data=X)
    plt.show()


