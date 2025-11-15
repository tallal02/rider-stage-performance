import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.formula.api import ols
from scipy import stats

# Try to read the file with automatic separator detection
df = pd.read_csv("cycling.txt", sep=None, engine="python")

print(df.head())
print()
print(df.dtypes)
print()
print(df.shape)

# 1. Convert to categorical
df["rider_class"] = df["rider_class"].astype("category")
df["stage_class"] = df["stage_class"].astype("category")

# 2. Inspect unique categories
print("Rider classes:", df["rider_class"].cat.categories.tolist())
print("Stage classes:", df["stage_class"].cat.categories.tolist())
print()

# 3. Basic summary of points
print(df["points"].describe())

# 1. Summary of points by rider_class
desc_by_rider = df.groupby("rider_class")["points"].describe()
print("Summary of points by rider class:")
print(desc_by_rider)
print()

# 2. Summary of points by stage_class
desc_by_stage = df.groupby("stage_class")["points"].describe()
print("Summary of points by stage class:")
print(desc_by_stage)
print()

# 3. Mean points by rider_class and stage_class (for interaction insight)
mean_by_both = df.groupby(["rider_class", "stage_class"])["points"].mean().unstack()
print("Mean points by rider and stage class:")
print(mean_by_both)


# Boxplot: points by rider class
plt.figure()
sns.boxplot(data=df, x="rider_class", y="points")
plt.xlabel("Rider class")
plt.ylabel("Points")
plt.title("Distribution of points by rider class")
plt.tight_layout()
plt.savefig("box_rider_points.png", dpi=300)

# Boxplot: points by stage class
plt.figure()
sns.boxplot(data=df, x="stage_class", y="points")
plt.xlabel("Stage class")
plt.ylabel("Points")
plt.title("Distribution of points by stage class")
plt.tight_layout()
plt.savefig("box_stage_points.png", dpi=300)

# Two-way ANOVA: points ~ rider_class * stage_class
model = ols("points ~ C(rider_class) * C(stage_class)", data=df).fit()
anova_table = sm.stats.anova_lm(model, typ=2)

print(anova_table)

# Residuals and fitted values
resid = model.resid
fitted = model.fittedvalues

# 1. Residuals vs fitted
plt.figure()
plt.scatter(fitted, resid, alpha=0.5)
plt.axhline(0, linestyle="--")
plt.xlabel("Fitted values")
plt.ylabel("Residuals")
plt.title("Residuals vs fitted")
plt.tight_layout()
plt.savefig("resid_vs_fitted.png", dpi=300)

# 2. Q-Q plot of residuals
plt.figure()
sm.qqplot(resid, line="45")
plt.title("Normal Q-Q plot of residuals")
plt.tight_layout()
plt.savefig("qq_resid.png", dpi=300)

# 3. Optional normality test
shapiro_stat, shapiro_p = stats.shapiro(resid)
print("Shapiro-Wilk test: statistic =", shapiro_stat, ", p-value =", shapiro_p)
