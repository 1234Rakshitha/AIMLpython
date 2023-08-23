import pandas as pd
import numpy as np
dict={ 'first score':[np.nan,30,np.nan,60],
       'second score':[np.nan,40,50,30],
       'third score':[np.nan,30,np.nan,50]}
data=pd.DataFrame(dict)
print(data)

print(data.isnull())
print(data.notnull())
print(data.fillna(0))
print(data.fillna(method="pad"))
print(data.fillna(method="bfill"))
print(data.replace(to_replace=np.nan,value=-99))
print(data.dropna())
print(data.dropna(how="all"))
