# 📊 AI Trend Analysis Agent (App Reviews)
Overview

This project implements an Agentic AI pipeline that analyzes app store reviews and generates a 30-day trend analysis report of user issues, requests, and feedback.

The system simulates a daily batch ingestion pipeline, extracts high-level topics from reviews, consolidates similar feedback, and produces a trend table that can be directly consumed by product and business teams.

# Problem Statement

Product teams often struggle to identify:

What issues are increasing over time

Which user complaints are recurring

What new feedback trends are emerging

This AI agent addresses the problem by:

Processing daily app review batches

Extracting normalized topics from noisy text

Tracking topic frequency trends over time

# Key Features

✅ Daily Batch Processing (simulated production setup)

✅ Agent-based Architecture

✅ High-recall Topic Extraction

✅ Structured Trend Analysis Output

✅ End-to-End Runnable Pipeline

✅ Clean, Modular Codebase

# Architecture
Raw Reviews (Daily Batch)
        ↓
Review Ingestion Agent
        ↓
Topic Extraction Agent
        ↓
Trend Analysis Agent
        ↓
CSV Trend Report (T to T-30)

# Folder Structure
ai-trend-analysis-agent/
│
├── agents/
│   ├── review_ingestion_agent.py
│   ├── topic_extraction_agent.py
│   ├── trend_analysis_agent.py
│
├── data/
│   ├── raw_reviews/        # Daily batch JSON files
│   └── processed/          # Topic-level processed data
│
├── output/
│   └── trend_report.csv    # Final trend analysis output
│
├── main.py                 # Pipeline orchestrator
├── requirements.txt
└── README.md

# How It Works
## 1️⃣ Review Ingestion Agent

Simulates daily ingestion of app reviews

Stores each batch as a separate JSON file

Mimics real-world streaming or batch pipelines

## 2️⃣ Topic Extraction Agent

Analyzes raw review text

Extracts the main issue/request per review

Normalizes feedback into consistent topic categories

## 3️⃣ Trend Analysis Agent

Aggregates processed topics

Generates a pivot table:

Rows → Topics

Columns → Dates

Cells → Frequency of occurrence

Output Format

The final output is a CSV file:

output/trend_report.csv


Example:

Topic	2025-01-25
delivery partner rude	6
delivery delay	12
food quality issue	9
other feedback	173
Installation & Setup
Prerequisites

Python 3.10+

Git

VS Code (recommended)

Install Dependencies
pip install -r requirements.txt

How to Run

From the project root:

python main.py


On successful execution, you will see:

Trend report generated successfully

Assumptions & Design Decisions

Google Play does not guarantee reliable historical daily reviews

To ensure stability, daily review ingestion is simulated

This accurately reflects real-world batch processing systems

The pipeline is designed to be easily extendable with:

LLM-based topic extraction

Semantic topic deduplication

Multi-day rolling windows

Limitations

Current topic extraction uses rule-based logic for stability

Can be enhanced using:

LLMs (GPT / Mistral / LLaMA)

Embedding-based semantic clustering

Historical app review availability is platform-dependent

Future Improvements

🔹 LLM-powered topic extraction

🔹 Semantic topic deduplication using embeddings

🔹 Rolling 30-day automated trend generation

🔹 API / Dashboard integration

🔹 Multi-app support

Why This Approach Works

Agent-oriented design improves modularity

High-recall topic extraction avoids trend fragmentation

Output format is directly usable by product teams

Pipeline mirrors real production data systems


Submission Notes

Repository is private

Includes working code and sample output

Pipeline is fully reproducible

Ready for live demonstration

🚀 Status

✅ End-to-End Pipeline Completed
✅ Live Assignment Ready