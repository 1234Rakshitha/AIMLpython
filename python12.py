import pandas as pd
import numpy as np 

data=pd.read_csv("C:/Users/SPTINT-14/Desktop/csv/taitanic.csv",index_col=('sibsp'))
print(data)
print(data.info())
print(data.shape)

print(data.loc[data['Age']>50])

print(data.iloc[5:10,2:4])
