import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data=pd.read_csv("USvideos.csv")
#data.boxplot(column='dislikes',by='category_id')
#data.boxplot(column='likes',by='category_id')
#data.boxplot(column='views',by='category_id')
#data.boxplot(column='comment_count',by='category_id')
#data.hist(column='likes',bins=50, figsize=(20,15))
#data.hist(column='dislikes',bins=50, figsize=(20,15))
#data.hist(column='views',bins=50, figsize=(20,15))
#data.hist(column='comment_count',bins=50, figsize=(20,15))
plt.show()
