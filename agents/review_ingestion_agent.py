import json
import os


def fetch_daily_reviews(app_id, batch_date, count=200):
    os.makedirs("data/raw_reviews", exist_ok=True)

    test_data = [
        {
            "batch_date": str(batch_date),
            "review_date": "2025-01-01",
            "text": "Delivery partner was rude",
            "rating": 1
        },
        {
            "batch_date": str(batch_date),
            "review_date": "2025-01-01",
            "text": "Food was cold and stale",
            "rating": 2
        }
    ]

    file_path = f"data/raw_reviews/{batch_date}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(test_data, f, indent=2)

    print("TEST FILE WRITTEN:", file_path)
