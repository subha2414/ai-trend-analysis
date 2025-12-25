import json
import os


def extract_topics():
    os.makedirs("data/processed", exist_ok=True)

    raw_files = os.listdir("data/raw_reviews")

    if not raw_files:
        print("No raw review files found")
        return

    for file in raw_files:
        input_path = f"data/raw_reviews/{file}"
        output_path = f"data/processed/{file}"

        with open(input_path, "r", encoding="utf-8") as f:
            reviews = json.load(f)

        processed = []

        for r in reviews:
            text = r.get("text", "").lower()

            if "delivery" in text and "rude" in text:
                topic = "delivery partner rude"
            elif "delivery" in text and "late" in text:
                topic = "delivery delay"
            elif "cold" in text or "stale" in text:
                topic = "food quality issue"
            else:
                topic = "other feedback"

            processed.append({
                "date": r.get("batch_date"),
                "topic": topic
            })

        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(processed, f, indent=2)

        print(f"Processed topics for {file}")
