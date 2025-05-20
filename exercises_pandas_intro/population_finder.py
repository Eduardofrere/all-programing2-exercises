import pandas as pd
import argparse

df=pd.read_csv("worldcities.csv")


parser=argparse.ArgumentParser()
parser.add_argument("--city",required=True)
args=parser.parse_args()


df=df.set_index("city")

if args.city not in df.index:
    print("not valid city")

else:
    population= df.loc[args.city]["population"]
    print(f"the population of {args.city} is {population}")
