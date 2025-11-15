# Cycling Manager ANOVA Analysis

Analyze cycling race data with two-way ANOVA to see how rider class, stage type, and their interaction affect points.

This project analyses a cycling manager game dataset using Python and a two-way ANOVA model.  
The goal is to compare rider classes across stage classes and answer three research questions:

- **RQ1:** Do rider classes differ in their average points?  
- **RQ2:** Do stage classes differ in average points?  
- **RQ3:** Does the effect of rider class on points depend on the stage class?

The project contains the analysis code.

---

## Dataset

The dataset comes from a simulated cycling tour used in a manager-style game.

Each row corresponds to **one rider in one stage** and includes:

- `all_riders`: rider name (identifier)  
- `rider_class`: rider class (All Rounder, Climber, Sprinter, Unclassed)  
- `stage`: stage identifier  
- `points`: points gained by the rider in that stage (numeric)  
- `stage_class`: stage type (`flat`, `hills`, `mount`)

There are **3,496 observations** and **5 variables**.

- **Response variable:** `points`  
- **Factors:**
  - `rider_class` (4 levels)  
  - `stage_class` (3 levels)

The distribution of `points` is skewed with many zeros and a few very large values.

---

## Methods

The analysis uses **Python** and:

- `pandas` for data handling  
- `matplotlib` and `seaborn` for visualisation  
- `statsmodels` for fitting the ANOVA model  
- `scipy` for the Shapiro–Wilk normality test  

### Workflow

1. Load `cycling.txt` into a pandas DataFrame.  
2. Convert `rider_class` and `stage_class` to categorical variables.  
3. Compute descriptive statistics:
   - Overall distribution of `points`  
   - Summary of `points` by `rider_class`  
   - Summary of `points` by `stage_class`  
   - Mean `points` by (`rider_class`, `stage_class`)  
4. Create boxplots:
   - `points` by `rider_class`  
   - `points` by `stage_class`  
5. Fit a **two-way ANOVA with interaction**:

   ```
   points ~ C(rider_class) * C(stage_class)
   ```

6. Check model assumptions:

   - Residuals vs fitted values  
   - Normal Q–Q plot  
   - Shapiro–Wilk test for normality  

A two-way ANOVA with interaction is appropriate because:

- The response variable (`points`) is numeric.  
- The predictors (`rider_class`, `stage_class`) are categorical with a small number of levels.  
- We are interested in both **main effects** (RQ1, RQ2) and the **interaction** (RQ3).

---

## Results (short summary)

### Descriptive results

**points:**

- Mean ≈ **12.39**  
- Standard deviation ≈ **36.29**  
- Median = **0**  
- Maximum = **304**

**By rider class (mean points):**

- All Rounder: **37.69**  
- Climber: **20.17**  
- Sprinter: **15.04**  
- Unclassed: **6.42**

This suggests strong differences between rider classes (RQ1).

**By stage class (mean points):**

- flat: **11.79**  
- hills: **12.52**  
- mount: **12.88**

These means are very similar and show no clear descriptive difference between stage types (RQ2).

**Mean points by (`rider_class`, `stage_class`)** show a clear interaction (RQ3):

- **All Rounder**
  - flat: **15.44**
  - hills: **35.79**
  - mount: **67.42**
- **Climber**
  - flat: **5.09**
  - hills: **21.67**
  - mount: **35.86**
- **Sprinter**
  - flat: **38.98**
  - hills: **5.20**
  - mount: **2.04**
- **Unclassed**
  - flat: **5.74**
  - hills: **9.10**
  - mount: **2.95**

Interpretation:

- Sprinters perform well on **flat** stages but poorly on **hills** and **mountain** stages.  
- Climbers and All Rounders perform better on **hilly** and **mountain** stages.  
- Unclassed riders perform poorly across all stage types.

### ANOVA results

Two-way ANOVA (type II) with:

```
points ~ C(rider_class) * C(stage_class)
```

**Key results:**

- **Main effect: rider_class (RQ1)**  
  - F ≈ **92.82**  
  - p ≈ **8.7 × 10⁻⁵⁸**  
  - → Strong evidence that rider classes differ in mean points.

- **Main effect: stage_class (RQ2)**  
  - F ≈ **0.28**  
  - p ≈ **0.75**  
  - → No evidence of a main effect of stage class on mean points.

- **Interaction: rider_class × stage_class (RQ3)**  
  - F ≈ **51.00**
  - p ≈ **2.0 × 10⁻⁶⁰**  
  - → Strong evidence that the effect of rider class depends on stage class.

So:

- **RQ1:** Yes, rider classes differ in average performance.  
- **RQ2:** No, stage classes do not differ in mean points on their own.  
- **RQ3:** Yes, there is a strong interaction between rider and stage classes.

---

## Diagnostics

**Residuals vs fitted:**

- Residuals form vertical bands (group means).  
- Spread is large with some big positive outliers.  
- No clear funnel shape, but variance is not constant.

**Normal Q–Q plot:**

- Large deviations from the reference line.  
- Many residuals near zero and a long right tail.  
- Indicates strong non-normality.

**Shapiro–Wilk test:**

- Statistic ≈ **0.56**  
- p ≈ **2.2 × 10⁻⁶⁹**  
- Rejects normality of residuals.

These diagnostics show that the ANOVA assumptions do not hold exactly.  
The sample size is large and the effects for rider class and the interaction are very strong, so the main conclusions remain stable in practice.

---

## Repository structure

Suggested layout:

```text
.
├── work.ipynb                # Python analysis script
├── cycling.txt            # dataset
├── box_rider_points.png   # boxplot: points by rider_class
├── box_stage_points.png   # boxplot: points by stage_class
├── resid_vs_fitted.png    # residuals vs fitted plot
├── qq_resid.png           # Q–Q plot of residuals
├── logo.png               # TU Dortmund logo for title page
└── README.md              # this file
```


---

## How to run the analysis

1. **Clone the repository:**

   ```bash
   git clone https://github.com/tallal02/rider-stage-performance.git
   cd REPO_NAME
   ```

2. **(Optional) Create and activate a virtual environment.**

3. **Install dependencies:**

   ```bash
   pip install pandas matplotlib seaborn statsmodels scipy
   ```

4. **Run the script:**

   ```bash
   python work.ipynb
   ```

This will:

- Load the dataset  
- Compute descriptive statistics  
- Generate and save the figures  
- Fit the ANOVA model and print the ANOVA table and diagnostics  

---


