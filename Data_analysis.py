"""
Exploratory data analysis for AI Tools Usage Analytics.
Run after data_cleaning.py: python Data_analysis.py
"""
from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
INPUT_FILE = BASE_DIR / "clean_dataset.csv"
OUT_DIR = BASE_DIR / "outputs"
OUT_DIR.mkdir(exist_ok=True)

def analyse():
    if not INPUT_FILE.exists():
        raise FileNotFoundError("clean_dataset.csv not found. Run data_cleaning.py first.")

    df = pd.read_csv(INPUT_FILE)
    numeric = df.select_dtypes(include="number")

    summary = numeric.describe().round(2)
    summary.to_csv(OUT_DIR / "descriptive_statistics.csv")

    corr = numeric.corr().round(3)
    corr.to_csv(OUT_DIR / "correlation_matrix.csv")

    # Useful grouped comparisons (when columns are present).
    if "Num_AI_Tools_Used" in df.columns:
        tool_usage = df.groupby("Num_AI_Tools_Used").agg(
            Users=("User_ID", "count"),
            Avg_Productivity=("Productivity_Rating", "mean"),
            Avg_Satisfaction=("Satisfaction_Score", "mean"),
            Avg_Time_Saved=("Time_Saved_Hours_Per_Week", "mean")
        ).round(2)
        tool_usage.to_csv(OUT_DIR / "analysis_by_number_of_tools.csv")

    if "Daily_AI_Usage_Hours" in df.columns:
        df["Usage_Group"] = pd.cut(
            df["Daily_AI_Usage_Hours"],
            bins=[-0.01, 1, 3, 5, 24],
            labels=["Low (0-1 hr)", "Moderate (1-3 hrs)", "High (3-5 hrs)", "Very high (5+ hrs)"]
        )
        usage = df.groupby("Usage_Group", observed=False).agg(
            Users=("User_ID", "count"),
            Avg_Productivity=("Productivity_Rating", "mean"),
            Avg_Satisfaction=("Satisfaction_Score", "mean"),
            Avg_Time_Saved=("Time_Saved_Hours_Per_Week", "mean")
        ).round(2)
        usage.to_csv(OUT_DIR / "analysis_by_usage_group.csv")

    # Generate a concise text report with dataset-specific figures.
    lines = [
        "AI TOOLS USAGE ANALYTICS - ANALYSIS SUMMARY",
        f"Number of records: {len(df)}",
        f"Number of columns: {len(df.columns)}",
        "",
        "Average values:"
    ]
    for col in numeric.columns:
        lines.append(f"- {col}: {numeric[col].mean():.2f}")
    if "Time_Saved_Hours_Per_Week" in df.columns:
        lines += ["", f"Average weekly time saved: {df['Time_Saved_Hours_Per_Week'].mean():.2f} hours"]
    if "Productivity_Rating" in df.columns:
        lines.append(f"Average productivity rating: {df['Productivity_Rating'].mean():.2f}/10")
    if "Satisfaction_Score" in df.columns:
        lines.append(f"Average satisfaction score: {df['Satisfaction_Score'].mean():.2f}/10")

    (OUT_DIR / "analysis_summary.txt").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))
    print(f"\nAnalysis files saved in: {OUT_DIR}")

if __name__ == "__main__":
    analyse()
