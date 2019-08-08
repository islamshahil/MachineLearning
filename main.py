import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np
from sklearn.linear_model import LinearRegression

df = pd.read_excel('./LandData.xlsx') #add the path of the file directory

#print(df['Year'])

m=list(df['Year'])
m=np.array(m).reshape(-1,1)
n=list(df['Price'])
n=np.array(n).reshape(-1,1)

#print(m)
#print(n)

reg = LinearRegression().fit(m, n)

a=reg.score(m, n)
#b=reg.coef_array([1., 2.])
d=reg.predict([[2033]]) #enter the year for which you want to predict

print(*d)
