from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import json
import os

model = SentenceTransformer("all-MiniLM-L6-v2")

def deduplicate_topics():
    all_topics = []

    for file in os.listdir("data/processed"):
        with open(f"data/processed/{file}") as f:
            data = json.load(f)
            all_topics.extend([d["topic"] for d in data])

    unique_topics = list(set(all_topics))
    embeddings = model.encode(unique_topics)

    index = faiss.IndexFlatL2(embeddings.shape[1])
    index.add(np.array(embeddings))

    topic_map = {}
    for i, topic in enumerate(unique_topics):
        D, I = index.search(np.array([embeddings[i]]), 1)
        topic_map[topic] = unique_topics[I[0][0]]

    return topic_map
