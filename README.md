# 📊 AI Trend Analysis Agent (App Reviews)
**Overview**

This project implements an Agentic AI pipeline that analyzes Google Play Store app reviews and generates a trend analysis report of user issues, requests, and feedback over time.

The system is designed to simulate daily batch ingestion starting from June 1, 2024, process reviews using modular AI agents, and produce a structured trend table (T to T-30) that can be directly used by product and business teams.

# Problem Statement

- Product teams need a scalable way to understand:

  - Which user issues are increasing over time

  - What feedback patterns are recurring

  - What new issues or requests are emerging

- This assignment requires building an AI agent that:

  - Consumes daily app review batches

  - Extracts meaningful topics

  - Tracks topic frequency trends across days

# Key Features

✅ Daily Batch Processing (simulated production setup)

✅ Agent-based Architecture

✅ High-recall Topic Extraction

✅ Structured Trend Analysis Output

✅ End-to-End Runnable Pipeline

✅ Clean, Modular Codebase

# Architecture
```text
Raw Reviews (Daily Batch)
        ↓
Review Ingestion Agent
        ↓
Topic Extraction Agent
        ↓
Trend Analysis Agent
        ↓
CSV Trend Report (T to T-30)
```

# Folder Structure
```text
ai-trend-analysis/
│
├── agents/
│   ├── review_ingestion_agent.py
│   ├── topic_extraction_agent.py
│   └── trend_analysis_agent.py
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
```


# How It Works
**1️⃣ Review Ingestion Agent**

- Simulates daily ingestion of Google Play Store reviews

- Creates one batch per day starting from June 1, 2024

- Stores each batch as a separate JSON file
(YYYY-MM-DD.json)

**2️⃣ Topic Extraction Agent**

- Reads raw daily review batches

- Extracts and normalizes the main issue / request / feedback topic

- Produces structured topic-level data per day

**3️⃣ Trend Analysis Agent**

- Aggregates topic data across all days

- Computes topic frequency per day

- Generates a CSV trend table for analysis

# Output Format

**The final output is a CSV file:**

output/trend_report.csv


**Example:**

| Topic                  | 2024-06-01 | 2024-06-02 | ... | 2025-01-25 |
|------------------------|------------|------------|-----|------------|
| Delivery delay         | 12         | 8          | ... | 23         |
| Delivery partner rude  | 5          | 7          | ... | 9          |
| Food quality issue     | 9          | 6          | ... | 11         |

# Installation & Setup
**Prerequisites**

- Python 3.10+

- Git

- VS Code (recommended)

**Install Dependencies**


pip install -r requirements.txt

**How to Run**

***From the project root:***

python main.py

***On successful execution, you will see:***

- Daily batch files are generated from June 1, 2024 → current date

- Topics are extracted and processed

- Final trend report is created in output/

# Assumptions & Design Decisions

***Note:**
Google Play Store does not guarantee reliable access to historical daily reviews.
To handle this limitation, the system simulates daily review batches starting from
June 1, 2024, while preserving the exact batch-based architecture required
for trend analysis.

This approach mirrors real-world production pipelines where ingestion and analysis
are decoupled from data availability constraints.


# Future Improvements

- LLM-based high-recall topic extraction

- Semantic topic deduplication using embeddings

- Rolling 30-day automated trend window

- REST API or dashboard for product teams

- Multi-app support (Swiggy, Zomato, etc.)

# Why This Approach Works

- Agent-oriented design improves modularity

- High-recall topic extraction avoids trend fragmentation

- Output format is directly usable by product teams

- Pipeline mirrors real production data systems


# Submission Notes

- Repository contains complete runnable code

- Architecture aligns with assignment requirements

- Daily batch assumption clearly documented

- Ready for live demonstration and evaluation

# 🚀 Status

✅ End-to-End Pipeline Completed

✅ Live Assignment Ready