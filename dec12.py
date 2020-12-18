import pandas as pd,numpy as np
a = pd.Series([14,5,-8,9],index=['a','b','c','d'])
#print(a)
'''print(a.values)
print(a.dtype)
print(a.index)
print(a['a'])
a['a']=45
print(a)
print(a[['a','b']])
print(a>0)
print(a[a>0])
print(a<0)
print(a[a<0])
print(a+25)
print(a*2)
print(a-5)
print(a/2)
print(np.exp(a))
print('a' in a)
print(5 in [1,2,3,4,5])
# To check whether the series filed or not
print(a.isnull())
print(pd.isnull(a))
print(a.notnull())'''

'''data = {'state':['Andhra','TG','M.rastra','Orissa','Kerala','T.nadu','MP'],
        'year':[2000,2001,2002,2003,2004,2005,2006],
        'pop':[1.5,1.8,2.1,2.7,4.5,4.8,6.4]}
f = pd.DataFrame(data)
print(f)
print(f.head())
print(f.tail())
f1 = pd.DataFrame(data,columns = ['state','year','pop','debt'],
                  index =['one','two','three','four','five','six','seven'])
print(f1)
print(f1.values)
print(f1.dtypes)
print(f1.index)
print(f1.head(2))

a = pd.Series(range(3),index=[1,2,3])
print(a)
d = a.index
print(d)
print(d[1])
d[1]=45
print(d[1])
a = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(a)
b = a.reindex(['f','b','a','e','c','d'])
print(b)

frame = pd.DataFrame(np.arange(9).reshape((-1,3)),index=['a','b','c',],
                     columns=['Ohio','Texas','California'])
print(frame)
#frame.drop(['a'],inplace=True)
#print(frame)
print(frame.drop(['Ohio','Texas'],axis=1,inplace=True))
print(frame)

data= pd.DataFrame(np.arange(16).reshape(4,4),index=['Ohio','colorado','Utah','New York'],
               columns=['one','two','three','four'])
print(data)
print(data['one'])
print(data.loc['Ohio'])
print(data.loc[['Ohio','Utah']])
print(data.loc['Ohio','one'])
print(data.iloc[0])
print(data.iloc[:2])
print(data.iloc[1:4][data>1][data<15])

df1 = pd.DataFrame(np.arange(12).reshape((3,4)),columns=list('abcd'))
df2 = pd.DataFrame(np.arange(20).reshape((4,5)),columns=list('abcde'))
print(df1)
print(df2)
print(df1+df2)
df2.loc[1,'b'] = np.nan
print(df2)
print(df1+df2)
print(df1.add(df2,fill_value=10))'''
df = pd.DataFrame(np.random.randn(5,3),index=['a','c','e','f','h'],
                  columns = ['one','two','three'])
print(df)
df1 = df.reindex(['a','b','c','d','e','f','g','h'])
print(df1)
df2 = df1.fillna(method='bfill',axis=0)
#print(df2)
df3 = df1.fillna(method='ffill',axis=0)
#print(df3)
df4 = df1.fillna(method='ffill',axis=1).fillna(5)
print(df4)




















    
