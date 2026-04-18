import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Task3/data.csv")

print(df.info())
print(df.describe())

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors='coerce')

df = df.dropna()

df["AvgMonthlySpend"] = df["TotalCharges"] / df["tenure"]

def tenure_group(x):
    if x <= 12:
        return "0-12"
    elif x <= 24:
        return "13-24"
    else:
        return "24+"

df["TenureGroup"] = df["tenure"].apply(tenure_group)

df["Churn"] = df["Churn"].map({"Yes": 1, "No": 0})

df = pd.get_dummies(df, columns=["Contract"], drop_first=True)

df.to_csv("Task3/cleaned_data.csv", index=False)

plt.figure()
sns.countplot(x="Churn", data=df)
plt.savefig("Task3/plots/churn_count.png")

plt.figure()
sns.boxplot(x="Churn", y="MonthlyCharges", data=df)
plt.savefig("Task3/plots/boxplot.png")

plt.figure()
sns.heatmap(df.corr(), annot=True)
plt.savefig("Task3/plots/heatmap.png")

print("Task 3 Completed")