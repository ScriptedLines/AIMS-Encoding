import pandas as pd
import numpy as np

mydf=pd.DataFrame()
mydf["Breakfast"]=["Every Day","Never","Rarely","Most Days","Never"]
arr=np.array(mydf["Breakfast"])
unique=np.unique(arr)
np.random.shuffle(unique)
ordenc=[]
for i in mydf["Breakfast"]:
    lp=np.where(unique==i)
    ordenc.append(lp[0][0])
mydf["Ordinal Encoding"]=ordenc
print(mydf)