import pandas as pd
import numpy as np
'''data = np.array([1,2,3,4])
f = pd.Series(data,index=[1,2,3,4])
print(f)
a = [1,2,3,4,5,6]
d1 = pd.Series(a,index=['m','u','r','a','l','i'])
print(d1)
d = {'sno':1,'name':'srinu bfs mohan','age':2}
e = pd.Series(d)
print(e)
friends = np.array(['Mohan','Srinu','Murali'])
l = pd.Series(friends)
print(l)

a = [1,2,4,5,6]
f = pd.Series(a)
print(f)
data1 = pd.DataFrame(a)
data = pd.DataFrame(a,index=[1,2,4,5,6],columns=[''])
print(data1)
print(data)

a = ('mohan','srinu','murali')
f = pd.DataFrame(a,index=[1,2,3])
print(f)

data = [['Mohan',22],['Murali',23],['Srinu',24.],['Anji',24]]
d = pd.DataFrame(data,columns=['Name','Age'],index=[1,2,3,4],dtype=float)
print(d)

data ={'Name':['satish','mohan','srinu','murali'],'Age':[24,23,23,24]}
d = pd.DataFrame(data,index=[1,2,3,4])
print(d)'''

d = {'one': pd.Series([1,2,3], index=['a','b','c']),
     'two': pd.Series([1,2,3,4], index=['a','b','c','d'])}
data = pd.DataFrame(d)
print(data)
                                      






















