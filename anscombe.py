# graphical analysis of data. The dataset is named after Francis Anscombe, who created
# it in 1973. Anscombe designed this dataset to illustrate how summary statistics
# (mean, variance, correlation, etc.) can be misleading if not accompanied by visual
# representations such as scatter plots.
# The Anscombe's Quartet consists of four datasets that have nearly identical simple descriptive
# statistics, but when graphed, they reveal very different distributions and relationships between
# variables.
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset("anscombe")
sns.set(style="ticks")
g = sns.FacetGrid(df, col="dataset", col_wrap=2)
g.map(sns.scatterplot, "x", "y")
plt.show()