import pandas as pd

s = pd.Series([10,20,30,40])

print(s)

data = {
    "Name" :["Ken","Jon","Audy"],
    "Age" : [29, 28, 29],
    "Marks" : [86, 87, 85]
}

df = pd.DataFrame(data)
print(df)
print(df.head()) #Top five rows
print(df.tail()) #Bottom five rows

print(df.info())

high_marks = df[df["Marks"] > 85]
print(high_marks)

df["Passed"] = df["Marks"] >= 50
print(df)