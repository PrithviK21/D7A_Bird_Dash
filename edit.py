# main libraries
import pandas as pd
from datetime import datetime
import seaborn as sns
import os
import numpy as np
import matplotlib.pyplot as plt
import glob

# filenames = glob.glob("finalMergedBirds/*.csv")
#
# bruh = [pd.read_csv(filename) for filename in filenames]
# toKeep = ['Scientific Name','Common Name',	'County','Locality','Latitude',
#          'Longitude','Date', 'mediaDownloadUrl']
# fml = []
# for df in bruh:
#     df = df[df['Year']>=2015]
#     fml.append(df[toKeep])
#
# for df in fml:
#     path = "semiFinalBirds/twit_ebird/bruh/"+str(df['Common Name'].iloc[0])+".csv"
#     df.to_csv(path)
#
# df = pd.concat(bruh,ignore_index=True)
# df.to_csv("finalMergedBirds/bruh.csv")

# df = pd.read_csv('finalMergedBirds/FinalMerged Bird Dataset.csv')
# x = df['Common Name']
# plt.hist(x)
# plt.show()


def newdate(x):
    date = datetime.strptime(x, '%d/%b/%Y')
    return date.strftime('%d/%m/%Y')


df = pd.read_csv("finalMergedBirds/FinalMerged Bird Dataset with slash dates.csv")
newdf = df.copy()
newdf['Date'] = newdf['Date'].apply(newdate)
newdf.to_csv("aids.csv")