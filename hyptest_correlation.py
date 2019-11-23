import pandas as pd
from scipy import stats
from statsmodels.stats import weightstats as stests
import numpy as np
import random
data=pd.read_csv('USvideos.csv')
##print(data['likes'].mean())
##ztest ,pval = stests.ztest(data['likes'], x2=None, value=data['likes'][0])
##print(float(pval))
##if pval<0.05:
##    print("reject null hypothesis")
##else:
##    print("accept null hypothesis")
def Rand(start, end, num): 
    res = []
    for j in range(num): 
        res.append(random.randint(start, end))
    return res 
#print(Rand(start, end, num)) 
mean_p=data['likes'].mean()
std_p=data['likes'].std()
print(mean_p)
l=Rand(1,40000,1000)
mean_s=0
for i in l:
    mean_s+=data['likes'][i]
mean_s=mean_s/len(l)
print("sample mean : ",mean_s)
st=std_p/(np.sqrt(1000))
zstat=(mean_s-mean_p)/st
print("z score : ",zstat)
if zstat<1.96 and zstat>-1.96:
    print("Null Hypothesis is plausible")
else:
    print("Null Hypothesis should be rejected")

##correlation
data_corr=data[['views','likes','dislikes','comment_count']]
print(data_corr.corr(method="pearson",min_periods=1))
