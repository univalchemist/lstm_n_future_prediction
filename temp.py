import pandas as pd

df = pd.DataFrame({"Col1": [10, 20, 15, 30, 45, 33, 45, 43, 23],
                   "Col2": [13, 23, 18, 33, 48, 78, 65, 45, 34],
                   "Col3": [17, 27, 22, 37, 52, 34, 23, 12, 56]},
                  index=pd.date_range("2020-01-01", "2020-01-9"))

print("----------------df--------------------")
print(df)
df['future'] = df['Col3'].shift(-2)
print("----------------df shift--------------------")
print(df)