import json,csv
import pandas as pd
import glob


csv_files = glob.glob('*.CSV')
list = []

for f in csv_files:
    list.append(pd.read_csv(f))
df = pd.concat(list)

df.to_csv("AllMail.csv")