import numpy as np
import math
from scipy.ndimage.interpolation import rotate


class DataAugement(object):
    def __init__(self, x, y):
        """
        Initialize an ImageGenerator instance.
        :param x: A Numpy array of input data. It has shape (num_of_samples, height, width, channels).
        :param y: A Numpy vector of labels. It has shape (num_of_samples, ).
        """
        self.x = x.copy()
        self.y = y.copy()
        self.N = np.size(y,axis = 0)
        self.T = np.size(x,axis = 1)
        self.C = np.size(x,axis = 4)
        self.trans_height =np.size(x,axis = 2)
        self.trans_width = np.size(x,axis = 3)
        self.is_horizontal_flip = False
        self.is_vertical_flip = False
        self.is_add_noise = False
       
        self.translated = None
        self.rotated = None
        self.flipped = None
        self.added = None
        self.x_aug = self.x.copy()
        self.y_aug = self.y.copy()
        self.N_aug = self.N

    def rotate(self, angle=0.0,rate = 1):
        """
        Rotate self.x by the angles (in degree) given.
        :param angle: Rotation angle in degrees.
        :return rotated: rotated dataset
        - https://docs.scipy.org/doc/scipy-0.16.1/reference/generated/scipy.ndimage.interpolation.rotate.html
        """
        rotated = []
        for i in range(self.N):
            flag = np.random.rand()
            if flag<= rate:
                self.dor = angle
                rotated_temp = rotate(self.x[i].copy(), angle,reshape=False,axes=(1, 2))     
                NoneZero = np.count_nonzero(self.x[i])
                NoneZeroTemp = np.count_nonzero(rotated_temp)
                self.y_aug.append(self.y[i])
                self.N_aug += 1
                rotated.append(rotated_temp)
        print('Rotated Number = ' , self.N_aug)
        return rotated

    def dataAug(self,angle = 0.0,rate = 1):
        Old = self.x.copy()
        
        rotated = self.rotate(angle,rate)
        NewData = np.append(Old,rotated,axis = 0)
        newLabel = self.y_aug.copy()
        randnum = np.random.randint(0,100)
        np.random.seed(randnum)
        np.random.shuffle(NewData)
        np.random.seed(randnum)
        np.random.shuffle(newLabel)
        return NewData, newLabel