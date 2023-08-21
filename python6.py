import pandas as pd
import numpy as np 

s1=pd.Series([1,4,5,4,6,7])
s2=pd.Series([4,6,7,8,10])
u=pd.Series(np.union1d(s1,s2))
print("\n.........union........ \n",u)
i=pd.Series(np.intersect1d(s1,s2))
print("\n.......intersect.......\n",i)
print()
nc=u[~u.isin (i)]
print("\ndelete comman numbers\n",nc)

