
import pandas as pd
df = pd.read_csv('../data/Subscription.csv')
print(df.head())
print(df.info())
#%%
df["SubscriptionStartDate"] = pd.to_datetime(df["SubscriptionStartDate"], errors="coerce")
df["SubscriptionEndDate"] = pd.to_datetime(df["SubscriptionEndDate"], errors="coerce")
df["DiplomaDate"] = pd.to_datetime(df["DiplomaDate"], errors="coerce")
df["StudentBirthDate"] = pd.to_datetime(df["StudentBirthDate"], errors="coerce")

df["Country"] = df["Country"].str.title()
df["StudentGender"] = df["StudentGender"].str.upper()

df["SubscriptionProgress"] = (
    df["SubscriptionProgress"]
    .astype(str)
    .str.replace('%', '', regex=False)
    .str.strip()
)
df["SubscriptionProgress"] = pd.to_numeric(df["SubscriptionProgress"], errors='coerce')

df["SubscriptionMonth"] = df["SubscriptionStartDate"].dt.to_period("M")

df["StudentAge"] = 2025 - df["StudentBirthDate"].dt.year

df["Churned"] = df["SubscriptionEndDate"].notnull()
monthly_metrics = (
    df.groupby("SubscriptionMonth")
      .agg(subscriptions=("Student", "nunique"),
           average_progress=("SubscriptionProgress", "mean"),
           churned_students=("Churned", "sum"))
      .reset_index()
)
cohort_analysis = (
    df.groupby(["SubscriptionMonth", "Country", "TrackName"])
      .agg(num_students=("Student", "nunique"))
      .reset_index()
)
diploma_stats = (
    df.groupby("SubscriptionMonth")
      .agg(has_diploma=("SubscriptionHasDiploma", "sum"))
      .reset_index()
)
monthly_metrics.to_csv('../data/monthly_metrics.csv', index=False)
cohort_analysis.to_csv('../data/cohort_analysis.csv', index=False)
diploma_stats.to_csv('../data/diploma_stats.csv', index=False)
df.to_csv("../data/cleaned_olap_dataset.csv", index=False)