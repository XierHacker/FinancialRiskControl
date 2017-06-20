import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def loadMaterFrame():
    train_master_frame=pd.read_csv("../PPD-First-Round-Data-Update/Training Set/PPD_Training_Master_GBK_3_1_Training_Set.csv",encoding="gb18030")
    test_master_frame=pd.read_csv("../PPD-First-Round-Data-Update/Test Set/PPD_Master_GBK_2_Test_Set.csv",encoding="gb18030")
    return train_master_frame,test_master_frame

