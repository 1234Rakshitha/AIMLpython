import pandas as pd
import numpy as np 

data={'days':[1,2,3,4,5,6,7,8,9,10],'steps':[4335,9552,7332,4504,5335,7552,8332,6504,8965,7689]}
data1=pd.DataFrame(data)
print(data1)

data1['steps']=data1['steps']+1000
print("\nafter add 1000\n",data1)
a=data1[data1['steps']>7000]['days']
print("\ngretar then 7000\n",list(a))


