import pandas as pd 
from re import * 

data= pd.read_csv("cars.csv")

data["HP"]= data["Engine specs title"].str.extract(r"(\d+) HP").astype(float)
data["top speed"]=data["Top Speed"].str.extract(r"(\d+) km/h").astype(float)

new_df=data[["Title","HP","top speed","From year"]]


new_df=new_df.dropna()
new_df=new_df.drop_duplicates()


import matplotlib.pyplot as plt

plt.scatter(new_df["horsepower"], new_df["top_speed"], alpha=0.5)
plt.xlabel("Horsepower")
plt.ylabel("Top Speed (km/h)")
plt.title("Horsepower vs Top Speed")
plt.grid(True)
plt.show()

