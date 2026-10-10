
def clean_data(df):
    df_clean = df.copy()

    df_clean = df_clean.drop_duplicates()

    numeric_cols = df_clean.select_dtypes(
        include="number"
    ).columns

    df_clean[numeric_cols] = df_clean[numeric_cols].fillna(
        df_clean[numeric_cols].median()
    )

    print("Cleaned dataset shape:", df_clean.shape)
    print(
        "Missing values remaining:",
        df_clean.isnull().sum().sum()
    )

    return df_clean
