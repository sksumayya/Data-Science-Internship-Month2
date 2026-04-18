import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("netflix_data.csv")
df["date_added"] = pd.to_datetime(df["date_added"], errors='coerce')

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")

df["release_decade"] = (df["release_year"] // 10) * 10

df["is_movie"] = df["type"].apply(lambda x: 1 if x == "Movie" else 0)

print(df.head())

plt.figure()
df["type"].value_counts().plot.pie(autopct='%1.1f%%')
plt.title("Movies vs TV Shows")
plt.savefig("plots/pie_chart.png")

plt.figure()
df["release_year"].value_counts().sort_index().plot()
plt.title("Content Released Per Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("plots/line_plot.png")

plt.figure()
df["listed_in"].value_counts().head(10).plot(kind='bar')
plt.title("Top Genres")
plt.savefig("plots/bar_plot.png")

plt.figure()
pivot = pd.crosstab(df["country"], df["type"])
sns.heatmap(pivot, annot=True)
plt.title("Country vs Content")
plt.savefig("plots/heatmap.png")

print("Task 4 Completed")