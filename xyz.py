import pandas as pd

df=  pd.read_csv("/home/raushan/bakchodi/data.csv")
x= df.to_numpy()
data=[]

# print(x)
for i in range(len(x)):
    p=[]
    for j in range(len(x[i])):
        p.append(x[i][j])
    data.append(p)
# print(*data, end="\n")
for i in data:
    print(i,end=',')
    print()