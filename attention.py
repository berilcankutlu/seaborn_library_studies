# Seaborn's "attention" dataset contains data from a psychology experiment designed to study
# attention processes. This dataset can be used to understand the relationship between attention
# span and performance. The dataset includes the results of tasks performed under different conditions.

import seaborn as sns
import pandas as pd
pd.set_option("display.max_columns", None)
df = sns.load_dataset("attention")
df.head()
df.info()
df.isnull().sum()
df.drop("Unnamed: 0", axis=1).head()
df["subject"].max()
df["solutions"].unique()
df["score"].max()
df["score"].min()
df["score"].unique().sum()
aggregation_list = ["count", "mean", "median", "min", "max", "sum"]

df.groupby("attention").agg(aggregation_list)
df["score"].mean()
df.groupby("attention").agg({"score": "mean"})
