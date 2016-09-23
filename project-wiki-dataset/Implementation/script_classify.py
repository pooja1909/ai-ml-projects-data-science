from __future__ import division  # floating point division
import csv
import random
import math
import numpy as np

import classalgorithms as algs
 
def splitdataset(dataset, trainsize=400, testsize=200, testfile=None):
    randindices = np.random.randint(0,dataset.shape[0],trainsize+testsize)
    numinputs = dataset.shape[1]-1
    Xtrain = dataset[randindices[0:trainsize],0:numinputs]
    ytrain = dataset[randindices[0:trainsize],numinputs]
    Xtest = dataset[randindices[trainsize:trainsize+testsize],0:numinputs]
    ytest = dataset[randindices[trainsize:trainsize+testsize],numinputs]

    if testfile is not None:
        testdataset = loadcsv(testfile)
        Xtest = dataset[:,0:numinputs]
        ytest = dataset[:,numinputs]        
        
    # Add a column of ones; done after to avoid modifying entire dataset
    Xtrain = np.hstack((Xtrain, np.ones((Xtrain.shape[0],1))))
    Xtest = np.hstack((Xtest, np.ones((Xtest.shape[0],1))))
                              
    return ((Xtrain,ytrain), (Xtest,ytest))


 
def getaccuracy(ytest, predictions):
    correct = 0
    for i in range(len(ytest)):
        if ytest[i] == predictions[i]:
            correct += 1
    return (correct/float(len(ytest))) * 100.0

def loadsusy():
    dataset = np.genfromtxt('C:\\Users\\Nandini\\Documents\\Textbooks\Project BD\\Classifiers-implemented-master\\output2.csv', delimiter=',')
    trainset, testset = splitdataset(dataset)    
    return trainset,testset

if __name__ == '__main__':
    trainset, testset = loadsusy()
    print('Running on train={0} and test={1} samples').format(trainset[0].shape[0], testset[0].shape[0])
    classalgs = {'Logistic Regression': algs.LogitReg(),
                 }
                          
    for learnername, learner in classalgs.iteritems():
        print 'Running learner = ' + learnername
        # Train model
        dividedDS={}
        dividedDS=learner.learn(trainset[0], trainset[1])
        predictions = learner.predict(testset[0])
        accuracy = getaccuracy(testset[1], predictions)
        print 'Accuracy for ' + learnername + ': ' + str(accuracy)
 
