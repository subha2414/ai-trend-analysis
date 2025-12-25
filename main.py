from agents.review_ingestion_agent import fetch_daily_reviews
from agents.topic_extraction_agent import extract_topics
from agents.trend_analysis_agent import generate_trend_report
from datetime import datetime

APP_ID = "in.swiggy.android"
BATCH_DATE = datetime.now().date()

fetch_daily_reviews(APP_ID, BATCH_DATE)
extract_topics()
generate_trend_report()
