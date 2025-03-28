import pandas as pd
data={ 'Cylinders' : [4,1,2,6],
    'hp': [200,10,100,500]}

df=pd.DataFrame(data)
print(df)
mean_c= df['Cylinders'].mean()
print(f"Mean : {mean_c}")

median_hp = df['hp'].median()
print(f"Median : {median_hp}")

std_C = df['Cylinders'].std()
print(f"Std : {std_C}")