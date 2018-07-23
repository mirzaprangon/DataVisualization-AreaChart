import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

x1 = pd.ExcelFile("Data.xlsx")
sheets = x1.sheet_names
df = x1.parse(sheets[0])

columns = list(df)
c = columns[1:len(columns)]
x = df[columns[0]].tolist()
temp = []

for col in c:
    temp.append(np.array(df[col].tolist()))

y = [temp[0], temp[1]+temp[4], temp[1]+temp[4]+temp[3], temp[3]]
lab = ['NRX', 'TRPs Contribution', 'Estimated TRPs', 'Base']

plt.stackplot(x,y,labels=lab)
plt.legend(loc='upper left')
plt.yticks([7000, 10000, 13000, 16000, 19000])
plt.show()
