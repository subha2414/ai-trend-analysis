import json
import os
from datetime import timedelta


def fetch_daily_reviews(app_id, batch_date, count=200):
    """
    Simulate daily Google Play review ingestion starting from June 1, 2024.
    """

    os.makedirs("data/raw_reviews", exist_ok=True)

    # Sample realistic reviews (simulation)
    sample_reviews = [
        "Delivery partner was rude and unprofessional",
        "Food was cold and stale",
        "Delivery was very late",
        "Great service and fast delivery",
        "App crashes sometimes while ordering"
    ]

    daily_reviews = []

    for text in sample_reviews:
        daily_reviews.append({
            "batch_date": str(batch_date),
            "review_date": str(batch_date),
            "text": text,
            "rating": 3
        })

    file_path = f"data/raw_reviews/{batch_date}.json"

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(daily_reviews, f, indent=2)

    print(f"Saved batch for {batch_date}")
