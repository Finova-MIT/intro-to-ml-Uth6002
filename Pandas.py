import pandas as pd
df=pd.read_csv("mtcars.csv")
print(df)

weight = df[df['wt']>5]
print(f"Cars having weight greater than 5kgs are : \n{weight}")

sorted_mpg = df.sort_values(by='mpg',ascending=False)
print(f"Cars sorted based on mpg :\n{sorted_mpg}")

df.set_index('carb',inplace=True)
print(df.loc[2])
 