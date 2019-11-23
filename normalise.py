import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn import preprocessing
data=pd.read_csv("USvideos.csv")
def standardize(df, label):
    df = df.copy(deep=True)
    series = df.loc[:, label]
    avg = series.mean()
    stdv = series.std()
    series_standardized = (series - avg)/ stdv
    return series_standardized
data['likes']=standardize(data,'likes')
data['views']=standardize(data,'views')
data['dislikes']=standardize(data,'dislikes')
data['comment_count']=standardize(data,'comment_count')
print(data.describe())
