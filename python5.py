import pandas as pd
import numpy as np

info=np.array([1,2,3,4])
s=pd.Series(info)
print(s)

s1=pd.Series(4,index=[0,1,2,3])
print(s1)

i=pd.Index([1,2,1,3])
print(i.value_counts())



