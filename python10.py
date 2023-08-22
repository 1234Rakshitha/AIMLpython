import pandas as pd
import numpy as np 

data=pd.DataFrame([[10,11,12,13],[10,11,12,13]],columns=["maths","seicence","kannada","english"])
print(data)

print("\nsum of subjects\n",data.sum())
print(data['maths'].sum())
print(data['seicence'].min())
print(data['kannada'].max())
print(data['english'].max())
print(data.value_counts())
print(data['kannada'].value_counts())
print(data.agg(['sum','max']))

