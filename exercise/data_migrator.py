import pandas as pd
import argparse


df = pd.read_csv("data.csv")

parser = argparse.ArgumentParser()
parser.add_argument("--format")
args = parser.parse_args()

if args.format == "xlsx":
    df.to_excel("data.xlsx", index=False)
    print("Saved as data.xlsx")
elif args.format == "json":
    df.to_json("data.json", orient="records", indent=2)
    print("Saved as data.json")
elif args.format == "csv":
    df.to_csv("data_copy.csv", index=False)
    print("Saved as data_copy.csv")
else:
    print("Unknown format. Please use --format csv, xlsx, or json.")

print("\n📄 Data preview:")
print(df)
