import numpy as np
import os
import math

class readData():
    
    def __init__(self):
        pass

    # function to read data from files
    def ReadData(self,path):
        path_list = os.listdir(path)
        Dataset = []
        for filename in path_list:
            read_dictionary = np.load(path+'/'+filename,allow_pickle=True).item()
            Dataset.append(read_dictionary)
        return Dataset
        pass

    # extract dataset that can be used in training process
    def Extract(self,path):
        Dataset = self.ReadData(path)
        Dim = len(Dataset)

        Left = []
        Right = []

        for i in range(Dim):

            # extract LeftFrame data
            NFL = len(Dataset[i]['LeftFrame'])
            for j in range(NFL):
                Left.append(Dataset[i]['LeftFrame'][j])
            
            # extract RightFrame data
            NFR = len(Dataset[i]['RightFrame'])
            for j in range(NFR):
                Right.append(Dataset[i]['RightFrame'][j])

        # add two Frames together
        
        Total = Left+Right
        return Total, Left, Right
        pass
