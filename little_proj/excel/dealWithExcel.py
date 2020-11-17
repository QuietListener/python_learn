import pandas as pd
df = pd.read_excel("./excel.xls")
for i in df.index.values:
    row_data = df.loc[i]
    row_size = len(row_data)
    for j in range(0,row_size):
        print(str(row_data[j]))
