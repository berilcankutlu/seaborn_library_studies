import seaborn as sns
# this simple dataset from a psychology experiment in which twenty subjects
# performed a memory task where they studied anagrams while their attention
# was either divided or focused
# loading dataset
df = sns.load_dataset("anagrams")
# first 10 data
df.head(10)
# summary statistics for the numerical columns
df.describe().T
# sum of the null data
df.isnull().sum()
# data types info
df.info()
# making columns' names upper
df.columns = [ col.upper() for col in df.columns]
# how many data in ATTNR
df["ATTNR"].value_counts()
# selecting object type columns
obj_cols = [col for col in df.columns if df[col].dtype=="object"]
# droping SUBIDR column
df.drop("SUBIDR", axis=1)
# selecting "NUM" columns
df.loc[: , df.columns.str.contains("NUM")]
# selecting data that bigger than 5 on NUM1 column
df[df["NUM1"] > 5].count()
# finding min, max and unique data on NUM1 column
df["NUM1"].max()
df["NUM1"].min()
df["NUM1"].unique()
# some calculations according to ATTNR
aggregation_list = ["count", "first", "last", "mean", "median", "min", "max", "sum"]
df.groupby("ATTNR").agg(aggregation_list)
