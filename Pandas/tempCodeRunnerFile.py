import pandas as pd

dict = {                       
    "name":['anshu','shubh'],  
    "marks":[99,93],         # dict is a dictionary
    "city":['Kolkata','mumbai']
}
df = pd.DataFrame(dict)
df.to_csv("friends.csv")
print(df)


# Passing list in dataframe

arr = [1,2,34,5,8,44]

arr2 = ["A", "B", "C", "D", "E","F"]

df = pd.DataFrame(
    {
        "column" : arr,
        "column2" : arr2,
        
    }, index=["I", "II", "III","IV","V","VI"]
)

print(df)

# Calculating the mean of the column2 using class method of pandas

mean=df["column2"].mean()

print(mean)