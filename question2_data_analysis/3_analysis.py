"""
3_analysis.py

Question 2 – Statistical Analysis (10 marks)

Descriptive Statistics (5):
1. mean, median, mode (price)
2. std dev, range (price)
3. average price by category (top 5 categories by count)
4. rating distribution frequency

Inferential Statistics (5):
1. outlier detection (IQR method) for price
2. Pearson correlation between price and rating
3. Hypothesis test (independent t-test): Fiction vs Non-Fiction prices
   - Report t-statistic, p-value, and conclusion (alpha = 0.05)

Input:  question2_data_analysis/data/cleaned_books_data.csv
Output: printed stats + optional CSV summaries in question2_data_analysis/data/
"""

import os
import numpy as np
import pandas as pd
from scipy import stats

CLEAN_FILE = "question2_data_analysis/data/cleaned_books_data.csv"
OUT_DIR = "question2_data_analysis/data"


def load_data() -> pd.DataFrame:
    print("[INFO] Loading cleaned dataset...")
    df = pd.read_csv(CLEAN_FILE)

    # Basic validation
    required_cols = {"title", "price_gbp", "rating", "category", "availability"}
    missing = required_cols - set(df.columns)
    if missing:
        raise ValueError(f"Missing required columns in cleaned data: {missing}")

    # Ensure correct dtypes
    df["price_gbp"] = pd.to_numeric(df["price_gbp"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")

    # Drop any unexpected NaNs from analysis stage
    df = df.dropna(subset=["price_gbp", "rating", "category"])
    return df


def descriptive_stats(df: pd.DataFrame) -> None:
    print("\n================ DESCRIPTIVE STATISTICS (5 marks) ================\n")

    prices = df["price_gbp"]

    mean_price = prices.mean()
    median_price = prices.median()

    # mode can return multiple values; choose the first for reporting
    mode_series = prices.mode()
    mode_price = mode_series.iloc[0] if not mode_series.empty else np.nan

    std_price = prices.std(ddof=1)  # sample std
    price_range = prices.max() - prices.min()

    print(f"1) Central Tendency (Price GBP)")
    print(f"   - Mean   : {mean_price:.2f}")
    print(f"   - Median : {median_price:.2f}")
    print(f"   - Mode   : {mode_price:.2f}")

    print(f"\n2) Dispersion (Price GBP)")
    print(f"   - Std Dev: {std_price:.2f}")
    print(f"   - Range  : {price_range:.2f} (min={prices.min():.2f}, max={prices.max():.2f})")

    # Top 5 categories by number of books
    top5_categories = df["category"].value_counts().head(5).index.tolist()
    avg_price_by_cat = (
        df[df["category"].isin(top5_categories)]
        .groupby("category")["price_gbp"]
        .mean()
        .sort_values(ascending=False)
    )

    print("\n3) Group Statistics: Average Price by Category (Top 5 by count)")
    for cat, avgp in avg_price_by_cat.items():
        print(f"   - {cat}: {avgp:.2f}")

    rating_counts = df["rating"].value_counts().sort_index()
    print("\n4) Rating Distribution (Frequency Count)")
    for r, c in rating_counts.items():
        print(f"   - Rating {int(r)}: {c}")

    # Save summaries for report (optional but nice)
    os.makedirs(OUT_DIR, exist_ok=True)
    avg_price_by_cat.to_csv(os.path.join(OUT_DIR, "avg_price_top5_categories.csv"), header=["avg_price_gbp"])
    rating_counts.to_csv(os.path.join(OUT_DIR, "rating_distribution.csv"), header=["count"])

    print(f"\n[INFO] Saved: avg_price_top5_categories.csv, rating_distribution.csv")


def iqr_outliers(df: pd.DataFrame) -> pd.DataFrame:
    prices = df["price_gbp"]
    q1 = prices.quantile(0.25)
    q3 = prices.quantile(0.75)
    iqr = q3 - q1

    lower = q1 - 1.5 * iqr
    upper = q3 + 1.5 * iqr

    outliers = df[(df["price_gbp"] < lower) | (df["price_gbp"] > upper)].copy()
    return outliers, (q1, q3, iqr, lower, upper)


def inferential_stats(df: pd.DataFrame) -> None:
    print("\n================ INFERENTIAL STATISTICS (5 marks) ================\n")

    # 1) Outlier detection (IQR)
    outliers, (q1, q3, iqr, lower, upper) = iqr_outliers(df)
    print("1) Outlier Detection (IQR Method) - Price GBP")
    print(f"   - Q1={q1:.2f}, Q3={q3:.2f}, IQR={iqr:.2f}")
    print(f"   - Lower Bound={lower:.2f}, Upper Bound={upper:.2f}")
    print(f"   - Outliers Found: {len(outliers)}")

    # Save outliers (useful in appendix)
    os.makedirs(OUT_DIR, exist_ok=True)
    outliers_path = os.path.join(OUT_DIR, "price_outliers_iqr.csv")
    outliers.to_csv(outliers_path, index=False)
    print(f"   - Saved outliers to: {outliers_path}")

    # 2) Pearson correlation: price vs rating
    print("\n2) Correlation Analysis (Pearson) - Price vs Rating")
    r, p = stats.pearsonr(df["price_gbp"], df["rating"])
    print(f"   - Pearson r = {r:.4f}")
    print(f"   - p-value   = {p:.6f}")
    if p < 0.05:
        print("   - Conclusion: Statistically significant correlation (α=0.05).")
    else:
        print("   - Conclusion: No statistically significant correlation (α=0.05).")

    # 3) Hypothesis testing: Fiction vs Non-Fiction
    print("\n3) Hypothesis Testing (Independent t-test): Fiction vs Non-Fiction prices")
    alpha = 0.05

    # Normalize category names a bit
    df["category_norm"] = df["category"].astype(str).str.strip().str.lower()

    fiction = df[df["category_norm"] == "fiction"]["price_gbp"]
    nonfiction = df[df["category_norm"] == "nonfiction"]["price_gbp"]

    print(f"   - Fiction sample size    : {len(fiction)}")
    print(f"   - Non-Fiction sample size: {len(nonfiction)}")

    if len(fiction) < 2 or len(nonfiction) < 2:
        print("   [WARN] Not enough Fiction/Nonfiction rows to run t-test reliably.")
        print("          (Need at least 2 values in each group.)")
        return

    # Welch’s t-test (safer when variances differ)
    t_stat, p_val = stats.ttest_ind(fiction, nonfiction, equal_var=False)

    print(f"   - t-statistic = {t_stat:.4f}")
    print(f"   - p-value     = {p_val:.6f}")

    if p_val < alpha:
        print("   - Conclusion: Reject H0. Average prices differ between Fiction and Non-Fiction (α=0.05).")
    else:
        print("   - Conclusion: Fail to reject H0. No evidence of a price difference (α=0.05).")


def main():
    df = load_data()
    print(f"[INFO] Rows available for analysis: {len(df)}")

    descriptive_stats(df)
    inferential_stats(df)

    print("\n[SUCCESS] Statistical analysis completed.\n")


if __name__ == "__main__":
    main()