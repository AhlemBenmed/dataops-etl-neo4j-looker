import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")
# Load your OLAP data
monthly = pd.read_csv("../data/monthly_metrics.csv")
monthly["SubscriptionMonth"] = pd.to_datetime(monthly["SubscriptionMonth"].astype(str))

# Plotting monthly subscriptions and churned students
plt.figure(figsize=(12,6))
plt.plot(monthly["SubscriptionMonth"], monthly["subscriptions"], label="Subscriptions", marker='o')
plt.plot(monthly["SubscriptionMonth"], monthly["churned_students"], label="Churned", marker='x')
plt.title("Monthly Subscriptions vs. Churn")
plt.xlabel("Month")
plt.ylabel("Number of Students")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_churn_vs_subscriptions.png")
plt.show()

cohort = pd.read_csv("../data/cohort_analysis.csv")

# filter to a single month or track for clarity
subset = cohort[cohort["SubscriptionMonth"] == "2024-01"]

# Plotting students per country per track
plt.figure(figsize=(10,6))
sns.barplot(data=subset, x="Country", y="num_students", hue="TrackName")
plt.title("Students per Country per Track - Jan 2024")
plt.xlabel("Country")
plt.ylabel("Number of Students")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("studentspercountry.png")
plt.show()

# Load diploma statistics
diplomas = pd.read_csv("../data/diploma_stats.csv")
diplomas["SubscriptionMonth"] = pd.to_datetime(diplomas["SubscriptionMonth"].astype(str))
# Plotting diplomas awarded over time
plt.figure(figsize=(10,5))
sns.lineplot(data=diplomas, x="SubscriptionMonth", y="has_diploma", marker="o", color="green")
plt.title("Diplomas Awarded Over Time")
plt.xlabel("Month")
plt.ylabel("Number of Diplomas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("diplomastati.png")
plt.show()
