"""
5_prediction.py

Predictive Analysis:
Linear Regression model to predict book price

Features:
- rating
- category (one-hot encoded)

Evaluation:
- R² Score
- Mean Absolute Error (MAE)

Outputs interpretation of feature importance.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.preprocessing import OneHotEncoder


CLEAN_FILE = "question2_data_analysis/data/cleaned_books_data.csv"


def load_data():
    df = pd.read_csv(CLEAN_FILE)

    df["price_gbp"] = pd.to_numeric(df["price_gbp"], errors="coerce")
    df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
    df["category"] = df["category"].astype(str).str.strip()

    df = df.dropna(subset=["price_gbp", "rating", "category"])
    return df


def build_model(df):
    # Features
    X = df[["rating", "category"]]
    y = df["price_gbp"]

    # One-hot encode category
    encoder = OneHotEncoder(drop="first", sparse_output=False)
    category_encoded = encoder.fit_transform(X[["category"]])

    encoded_df = pd.DataFrame(
        category_encoded,
        columns=encoder.get_feature_names_out(["category"])
    )

    # Combine rating + encoded category
    X_final = pd.concat([X[["rating"]].reset_index(drop=True),
                         encoded_df.reset_index(drop=True)], axis=1)

    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(
        X_final, y, test_size=0.2, random_state=42
    )

    # Model
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Evaluation
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)

    return model, r2, mae, X_final.columns


def interpret_model(model, feature_names):
    coefficients = pd.Series(model.coef_, index=feature_names)

    print("\nFeature Coefficients:")
    print(coefficients.sort_values(key=abs, ascending=False))

    # Identify strongest feature
    strongest_feature = coefficients.abs().idxmax()

    print("\nInterpretation:")
    print(f"The feature with the strongest influence on price is: {strongest_feature}")

    if strongest_feature == "rating":
        print("This suggests rating has the strongest linear relationship with price.")
    else:
        print("This suggests category has stronger influence than rating on price.")


def main():
    print("Loading cleaned dataset...")
    df = load_data()

    print(f"Dataset size: {len(df)} books")

    model, r2, mae, feature_names = build_model(df)

    print("\nModel Evaluation Results")
    print("-------------------------")
    print(f"R² Score: {r2:.4f}")
    print(f"Mean Absolute Error (MAE): £{mae:.2f}")

    interpret_model(model, feature_names)

    print("\n[SUCCESS] Predictive analysis completed.")


if __name__ == "__main__":
    main()