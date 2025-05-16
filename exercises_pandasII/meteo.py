import pandas as pd
import argparse

df=pd.read_csv("meteo.csv")

print("test everuythign is working") 

clean_df=pd.DataFrame()
df["fecha"]= pd.to_datetime(df["fecha"])
clean_df["fecha"]= df["fecha"]

df["tmed"]=df["tmed"].str.replace(",",".").astype(float)
clean_df["tmed"]=df["tmed"]

def plot_temperature(date: pd.Series, temperatures: pd.Series):
    assert len(date) == len(temperatures)
    assert date.dtype == np.dtype("datetime64[ns]")
    assert temperatures.dtype == np.dtype("float64")
    import matplotlib.pyplot as plt
    years = date.dt.year
    day = date.dt.dayofyear
    plt.scatter(day, temperatures, c=years, marker=".")
    plt.colorbar(label="Year")
    plt.xticks(rotation=45)
    plt.xlabel("Date")
    plt.ylabel("Temperature (Celsius)")
    plt.show()


clean_df["year"]=df["fecha"].dt.year

yearly_stats=clean_df.groupby("year").agg({
    "tmed": ["max","min"]
})


parser=argparse.ArgumentParser()
parser.add_argument("--date")
args=parser.parse_args()

goodate=pd.to_datetime(args.date)
matching_row= clean_df[clean_df["fecha"]== goodate]
print("the average temperatur for",args.date ,"is", matching_row["tmed"].values[0])

print(clean_df[clean_df["fecha"]== "2005-02-02"])


