# main libraries
import pandas as pd
import os
import numpy as np
import time
import glob

filenames = glob.glob("FinalBirds/*.csv")
bruh = [pd.read_csv(filename) for filename in filenames]

def countItems():
    c = 0
    for df in bruh:
        x = df[df['Year']>=2015]
        c+=len(x.index)
    print(c)

"""df = pd.read_csv('NewBirds/White-throated Kingfisher.csv')
df2 = pd.read_csv('NewBirds/Black-backed Dwarf-Kingfisher.csv')"""

countItems()