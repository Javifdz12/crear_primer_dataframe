import pandas as pd
dict1={"tierra":9.8,"marte":3.7,"jupiter":24.8,"saturno":9,"urano":8.7,"neptuno":11}
dataframe1=pd.DataFrame(dict1.values(),dict1.keys()).transpose()
t1=0.46
l1=1
g1=(2*l1)/t1*t1
t2=0.66
l2=2
g2=(2*l2)/t2*t2
print(dataframe1)
print(g1,g2)