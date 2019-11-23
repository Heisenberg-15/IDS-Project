import pandas as pd
import numpy as np
data=pd.read_csv("USvideos_original.csv")
bool_series = pd.isnull(data['likes'])
print("Before Cleaning\n")
print(data[bool_series][0:5])
data['views'] = pd.to_numeric(data['views'], errors='coerce')
data['likes'] = pd.to_numeric(data['likes'], errors='coerce')
data['comment_count'] = pd.to_numeric(data['comment_count'], errors='coerce')
data['dislikes'] = pd.to_numeric(data['dislikes'], errors='coerce')

data['likes'] = data['likes'].fillna(data['likes'].mean())
data['comment_count'] = data['comment_count'].fillna(data['comment_count'].mean())
data['dislikes'] = data['dislikes'].fillna(data['dislikes'].mean())
data['views'] = data['views'].fillna(data['views'].mean())
bool_series = pd.isnull(data['likes'])
print("After Cleaning\n")
print(data[bool_series][0:5])
#data.to_csv("USvideos.csv")
bool_series = pd.isnull(data['comments_disabled'])
print("Before Cleaning\n")
print(data[bool_series][0:5])
data['comments_disabled']=data['comments_disabled'].fillna(method='ffill')
data['ratings_disabled']=data['ratings_disabled'].fillna(method='ffill')
data['video_error_or_removed']=data['video_error_or_removed'].fillna(method='ffill')
print("After Cleaning\n")
bool_series = pd.isnull(data['comments_disabled'])
print(data[bool_series][0:5])
##data.to_csv("USvideos.csv")
##data2=pd.read_csv("USvideos_original.csv")
##bool_series = pd.isnull(data2['views'])
##print(data2[bool_series][0:5])