import numpy as np
import pandas as pd
mydf=pd.DataFrame()
mydf["color"]=["red","red","yellow","green","yellow"]
myarr=np.array(mydf["color"])
unique=np.unique(myarr)
print(unique)
for x in unique:
    l=[]
    for i in mydf["color"]:
        if i==x:
            l.append(1)
        else:
            l.append(0)
    mydf[x]=l
print(mydf)

