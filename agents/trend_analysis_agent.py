import json
import os
import pandas as pd


def generate_trend_report():
    records = []

    for file in os.listdir("data/processed"):
        with open(f"data/processed/{file}", "r", encoding="utf-8") as f:
            data = json.load(f)
            records.extend(data)

    if not records:
        print("No processed data found")
        return

    df = pd.DataFrame(records)

    trend = pd.pivot_table(
        df,
        index="topic",
        columns="date",
        aggfunc="size",
        fill_value=0
    )

    os.makedirs("output", exist_ok=True)
    trend.to_csv("output/trend_report.csv")

    print("Trend report generated")
