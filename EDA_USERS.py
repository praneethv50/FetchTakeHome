import pandas as pd

# Load Users Data
users = pd.read_csv("C:/Users/vorug/Downloads/USER_TAKEHOME.csv")

# Convert Date Columns to Datetime
users["CREATED_DATE"] = pd.to_datetime(users["CREATED_DATE"], errors="coerce")
users["BIRTH_DATE"] = pd.to_datetime(users["BIRTH_DATE"], errors="coerce")

# Check Initial Data Quality
def data_quality_report(df, df_name):
    total_values = df.shape[0]
    null_counts = df.isnull().sum()
    null_percentage = (null_counts / total_values) * 100

    duplicate_count = df.duplicated().sum()
    duplicate_percentage = (duplicate_count / total_values) * 100

    summary_df = pd.DataFrame({
        "Total Values": total_values,
        "Null Count": null_counts,
        "Null Percentage": null_percentage.round(2)
    })

    print(f"\n=== Data Quality Report: {df_name} ===")
    print(summary_df)
    print(f"\nExact Duplicates: {duplicate_count} ({duplicate_percentage:.2f}%)\n")
    return summary_df

users_report = data_quality_report(users, "Users")

from datetime import datetime

# Calculate age only for non-null birthdates
users.loc[users["BIRTH_DATE"].notnull(), "AGE"] = users.loc[users["BIRTH_DATE"].notnull(), "BIRTH_DATE"].apply(
    lambda birth_date: datetime.today().year - birth_date.year - (
        (datetime.today().month, datetime.today().day) < (birth_date.month, birth_date.day)
    )
)
# Set unrealistic ages (>100) to NaN
users.loc[users["AGE"] > 100, "BIRTH_DATE"] = pd.NaT

median_age = users["AGE"].median()
users["AGE"].fillna(median_age, inplace=True)


print(users.head())

export_path="C:/Users/vorug/Downloads/USERS_cleaned.csv"
users.to_csv(export_path, index=False)


