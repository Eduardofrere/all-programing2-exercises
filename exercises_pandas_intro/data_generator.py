import pandas as pd 
import numpy as np

data= {"europa": ["portugal","espanha","franca"], "africa": ["marrocos", "mocambique","rwanda"], "asia": ["india","nepal","japan"]}

df= pd.DataFrame(data, index= [1,2,3])
df.to_csv("data.csv")
