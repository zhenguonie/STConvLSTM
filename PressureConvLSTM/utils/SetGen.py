import numpy as np 
import tensorflow as tf
from tensorflow import keras
from keras import layers
import math

class SetGen():
    def __init__(self):
        pass

    def Shuffle(self, data, label):
        
        randnum = np.random.randint(0,100)
        np.random.seed(randnum)
        np.random.shuffle(data)
        np.random.seed(randnum)
        np.random.shuffle(label)

        return data, label
        pass

    def GetSets(self, data, label, Ptr, Pval, gettest = False):
        trPoint = int(Ptr*len(data))
        valPoint = int(trPoint + Pval*len(data))
        Data, Label = self.Shuffle(data, label)
        Xtr, ytr = Data[:trPoint], Label[:trPoint]
        Xval, yval = Data[trPoint:valPoint], Label[trPoint:valPoint]
        if gettest:
            Xte, yte = Data[valPoint:], Label[valPoint:]
            return Xtr, ytr, Xval, yval, Xte, yte
        else:
            return Xtr, ytr, Xval, yval
        pass
    
    def DataAug(self, data, label, Pmirrow = 1, trans = 2, Ptrans = 0.2 ):
        
        fliped = np.flip(data, axis = 3)
        data = np.append(data, fliped, axis = 0)
        label = np.append(label,label, axis = 0)

        print(np.shape(data))
        return data, label                            
        pass

    def Normalization(self, data):
        [sampleNum, timeStep, H, W, C] = np.shape(data)
        Data = data
        for i in range(sampleNum):
            for j in range(timeStep):
                
                mean = np.mean(data[i][j])
                sigma = np.std(data[i][j])
                
                if mean < 0.01:
                    pass
                else:
                   Data[i][j] = (Data[i][j] - mean)/sigma
        return Data
        pass
