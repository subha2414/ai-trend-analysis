from agents.review_ingestion_agent import fetch_daily_reviews
from agents.topic_extraction_agent import extract_topics
from agents.trend_analysis_agent import generate_trend_report
from datetime import datetime, timedelta

APP_ID = "in.swiggy.android"

start_date = datetime(2024, 6, 1).date()
end_date = datetime.now().date()

current_date = start_date

while current_date <= end_date:
    fetch_daily_reviews(APP_ID, current_date)
    current_date += timedelta(days=1)

extract_topics()
generate_trend_report()
