"""
2_data_cleaning.py

Question 2 – Data Cleaning & Preprocessing (8 marks)

Performs:
1. Price standardization (remove £, convert to float)
2. Rating validation (ensure numeric 1–5)
3. Handle missing values
4. Remove duplicates
5. Create derived columns:
   - price_category
   - in_stock (boolean)

Also prints before/after statistics for report documentation.
"""

import pandas as pd
import os

# File paths
RAW_FILE = "question2_data_analysis/data/raw_books_data.csv"
CLEAN_FILE = "question2_data_analysis/data/cleaned_books_data.csv"


def load_data():
    print("\n[INFO] Loading raw dataset...")
    df = pd.read_csv(RAW_FILE)
    return df


def report_basic_stats(df, stage="Before Cleaning"):
    print(f"\n========== {stage} ==========")
    print("\nShape:", df.shape)
    print("\nMissing Values:\n", df.isnull().sum())
    print("\nData Types:\n", df.dtypes)
    print("\nDuplicate Rows:", df.duplicated().sum())


def clean_price(df):
    print("\n[INFO] Cleaning price column...")
    df["price_gbp"] = (
        df["price_gbp"]
        .astype(str)
        .str.replace("£", "", regex=False)
        .str.replace("Â", "", regex=False)
    )
    df["price_gbp"] = pd.to_numeric(df["price_gbp"], errors="coerce")
    return df


def clean_rating(df):
    print("\n[INFO] Validating rating column...")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    return df


def handle_missing(df):
    print("\n[INFO] Handling missing values...")
    df = df.dropna()
    return df


def remove_duplicates(df):
    print("\n[INFO] Removing duplicate rows...")
    df = df.drop_duplicates()
    return df


def create_price_category(df):
    print("\n[INFO] Creating price_category column...")

    def categorize(price):
        if price < 20:
            return "Budget"
        elif 20 <= price <= 40:
            return "Mid-range"
        else:
            return "Premium"

    df["price_category"] = df["price_gbp"].apply(categorize)
    return df


def create_in_stock(df):
    print("\n[INFO] Creating in_stock boolean column...")
    df["in_stock"] = df["availability"].str.contains("In stock", case=False)
    return df


def save_cleaned_data(df):
    os.makedirs("question2_data_analysis/data", exist_ok=True)
    df.to_csv(CLEAN_FILE, index=False)
    print(f"\n[SUCCESS] Cleaned dataset saved to: {CLEAN_FILE}")


def main():
    df = load_data()

    # Report before cleaning
    report_basic_stats(df, "Before Cleaning")

    # Cleaning steps
    df = clean_price(df)
    df = clean_rating(df)
    df = handle_missing(df)
    df = remove_duplicates(df)
    df = create_price_category(df)
    df = create_in_stock(df)

    # Report after cleaning
    report_basic_stats(df, "After Cleaning")

    save_cleaned_data(df)


if __name__ == "__main__":
    main()