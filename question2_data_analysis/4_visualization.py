"""
4_visualization.py

Creates 4 visualizations (Rubric-aligned + Polished):

1) Histogram (Matplotlib): Price distribution with mean line
2) Interactive Box Plot (Plotly): Price comparison across top 5 categories
3) Interactive Scatter (Plotly): Price vs Rating with regression line + jitter
4) Bar Chart (Matplotlib): Average rating by category (top 8)

Outputs saved in: question2_data_analysis/visualizations/
"""

import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

CLEAN_FILE = "question2_data_analysis/data/cleaned_books_data.csv"
OUT_DIR = "question2_data_analysis/visualizations"


def ensure_out_dir():
    os.makedirs(OUT_DIR, exist_ok=True)


def load_data() -> pd.DataFrame:
    df = pd.read_csv(CLEAN_FILE)

    df["price_gbp"] = pd.to_numeric(df["price_gbp"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["category"] = df["category"].astype(str).str.strip()

    df = df.dropna(subset=["price_gbp", "rating", "category"])
    return df


# -------------------------------------------------
# 1) Histogram (Matplotlib) – Price + mean line
# -------------------------------------------------
def plot_histogram_price(df: pd.DataFrame) -> None:
    ensure_out_dir()

    mean_price = df["price_gbp"].mean()

    plt.figure(figsize=(10, 6))
    plt.hist(df["price_gbp"], bins=20, edgecolor="black", alpha=0.75, label="Prices")
    plt.axvline(mean_price, color="red", linestyle="--", linewidth=2,
                label=f"Mean = £{mean_price:.2f}")

    plt.title("Price Distribution of Books")
    plt.xlabel("Price (£)")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()

    out_path = os.path.join(OUT_DIR, "1_histogram_price_distribution.png")
    plt.savefig(out_path, dpi=200)
    plt.close()
    print(f"[SAVED] {out_path}")


# -------------------------------------------------
# 2) Interactive Box Plot (Plotly) – Top 5 categories
# -------------------------------------------------
def plot_interactive_boxplot_top5(df: pd.DataFrame) -> None:
    ensure_out_dir()

    top5 = df["category"].value_counts().head(5).index.tolist()
    sub = df[df["category"].isin(top5)].copy()

    fig = px.box(
        sub,
        x="category",
        y="price_gbp",
        points="outliers",
        title="Price Comparison Across Top 5 Categories (Interactive)",
        labels={"category": "Category", "price_gbp": "Price (£)"}
    )
    fig.update_layout(template="plotly_white")

    out_path = os.path.join(OUT_DIR, "2_boxplot_price_top5_categories_interactive.html")
    fig.write_html(out_path)
    print(f"[SAVED] {out_path} (Interactive)")


# -------------------------------------------------
# 3) Interactive Scatter (Plotly) – Price vs Rating + regression + jitter
# -------------------------------------------------
def plot_interactive_scatter_price_vs_rating(df: pd.DataFrame) -> None:
    ensure_out_dir()

    # Jitter ratings slightly so points don't stack perfectly at 1,2,3,4,5
    df = df.copy()
    df["rating_jitter"] = df["rating"] + np.random.uniform(-0.08, 0.08, size=len(df))

    fig = px.scatter(
        df,
        x="rating_jitter",
        y="price_gbp",
        trendline="ols",
        opacity=0.65,
        title="Price vs Rating (Interactive with Regression Line)",
        labels={"rating_jitter": "Rating (1–5)", "price_gbp": "Price (£)"},
        hover_data=["title", "category", "availability"]
    )
    fig.update_layout(template="plotly_white")

    out_path = os.path.join(OUT_DIR, "3_scatter_price_vs_rating_interactive.html")
    fig.write_html(out_path)
    print(f"[SAVED] {out_path} (Interactive)")


# -------------------------------------------------
# 4) Bar Chart (Matplotlib) – Avg rating top 8 categories
# -------------------------------------------------
def plot_bar_avg_rating_top8(df: pd.DataFrame) -> None:
    ensure_out_dir()

    top8 = df["category"].value_counts().head(8).index.tolist()
    sub = df[df["category"].isin(top8)]

    avg_rating = (
        sub.groupby("category")["rating"]
        .mean()
        .reindex(top8)
    )

    plt.figure(figsize=(11, 6))
    plt.bar(avg_rating.index, avg_rating.values, alpha=0.85, edgecolor="black")

    plt.title("Average Rating by Category (Top 8)")
    plt.xlabel("Category")
    plt.ylabel("Average Rating (1–5)")
    plt.legend(["Avg Rating"])
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()

    out_path = os.path.join(OUT_DIR, "4_bar_avg_rating_top8_categories.png")
    plt.savefig(out_path, dpi=200)
    plt.close()
    print(f"[SAVED] {out_path}")


def main():
    df = load_data()
    print(f"[INFO] Rows used for visualization: {len(df)}")

    plot_histogram_price(df)
    plot_interactive_boxplot_top5(df)
    plot_interactive_scatter_price_vs_rating(df)
    plot_bar_avg_rating_top8(df)

    print("\n[SUCCESS] All visualizations created.")
    print("Open interactive charts from:")
    print(f"  {OUT_DIR}")


if __name__ == "__main__":
    main()