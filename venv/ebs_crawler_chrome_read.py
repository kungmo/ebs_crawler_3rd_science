import pandas as pd

df2 = pd.read_pickle('./df2_0705.pkl')

print(df2)

df2.to_excel("df2_0705.xlsx")
print('엑셀로 저장 완료')