import pandas as pd

df = pd.read_csv("Album Streams.csv")

#print(df['Artist'].value_counts())

#chisel_data = df[df['Artist'] == 'Cold Chisel']
#print(chisel_data)


sorted_by_age = df.sort_values(by='Total Streams', ascending=False)
print(sorted_by_age[['Album', 'Artist', 'Total Streams']].head())