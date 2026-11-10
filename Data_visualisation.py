"""
Create charts for the AI Tools Usage Analytics project.
Run after data_cleaning.py: python Data_visualisation.py
"""
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "clean_dataset.csv"
CHART_DIR = BASE_DIR / "charts"
CHART_DIR.mkdir(exist_ok=True)

def save_bar(data, x, y, title, xlabel, ylabel, filename):
    plt.figure(figsize=(9, 5))
    plt.bar(data[x].astype(str), data[y])
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.savefig(CHART_DIR / filename, dpi=150)
    plt.close()

def create_visualisations():
    if not INPUT_FILE.exists():
        raise FileNotFoundError("clean_dataset.csv not found. Run data_cleaning.py first.")
    df = pd.read_csv(INPUT_FILE)

    # 1. Daily AI usage distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df["Daily_AI_Usage_Hours"], bins=15, edgecolor="black")
    plt.title("Daily AI Usage Hours Distribution")
    plt.xlabel("Hours per day")
    plt.ylabel("Number of users")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "daily_ai_usage_distribution.png", dpi=150)
    plt.close()

    # 2. Average productivity by number of AI tools
    grouped = df.groupby("Num_AI_Tools_Used", as_index=False)["Productivity_Rating"].mean()
    save_bar(grouped, "Num_AI_Tools_Used", "Productivity_Rating",
             "Average Productivity by Number of AI Tools",
             "Number of AI tools used", "Average productivity rating",
             "productivity_by_tools.png")

    # 3. Average satisfaction and trust
    scores = pd.DataFrame({
        "Score": ["Satisfaction", "Trust"],
        "Average": [df["Satisfaction_Score"].mean(), df["Trust_Score"].mean()]
    })
    save_bar(scores, "Score", "Average", "Average Satisfaction and Trust Scores",
             "Score type", "Average score (0-10)", "satisfaction_trust.png")

    # 4. Weekly time saved distribution
    plt.figure(figsize=(8, 5))
    plt.hist(df["Time_Saved_Hours_Per_Week"], bins=15, edgecolor="black")
    plt.title("Weekly Time Saved Through AI Tools")
    plt.xlabel("Hours saved per week")
    plt.ylabel("Number of users")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "weekly_time_saved.png", dpi=150)
    plt.close()

    # 5. Usage vs productivity scatter plot
    plt.figure(figsize=(8, 5))
    plt.scatter(df["Daily_AI_Usage_Hours"], df["Productivity_Rating"], alpha=0.6)
    plt.title("Daily AI Usage vs Productivity")
    plt.xlabel("Daily AI usage (hours)")
    plt.ylabel("Productivity rating")
    plt.tight_layout()
    plt.savefig(CHART_DIR / "usage_vs_productivity.png", dpi=150)
    plt.close()

    print("Charts saved in:", CHART_DIR)

if __name__ == "__main__":
    create_visualisations()
