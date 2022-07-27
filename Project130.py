import pandas

df = pandas.read_csv("Project130.csv")

df = df.drop_duplicates()

del df["right_ascension"]
del df["apparent_magnitude"]
del df["declination"]
del df["Unnamed: 0"]
del df["distance"]
del df["mass"]
del df["radius"]


df.to_csv("Project130_cleaned.csv")