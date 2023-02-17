import pandas as pd

dict = {                       
    "name":['anshu','shubh'],  
    "marks":[99,93],         # dict is a dictionary
    "city":['Kolkata','mumbai']
}
df = pd.DataFrame(dict)
df.to_csv("friends.csv")
print(df)
