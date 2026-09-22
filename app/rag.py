import os

import numpy as np
from dotenv import load_dotenv
from google import genai


DOCUMENT_DIR = "data/documents"

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)


def load_documents():
    documents = []

    for filename in os.listdir(DOCUMENT_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(DOCUMENT_DIR, filename)

            with open(filepath, "r", encoding="utf-8") as file:
                content = file.read()

            documents.append({
                "filename": filename,
                "content": content
            })

    return documents


def chunk_text(text, chunk_size=500):
    chunks = []

    for i in range(0, len(text), chunk_size):
        chunk = text[i:i + chunk_size]

        if chunk.strip():
            chunks.append(chunk)

    return chunks


def get_embedding(text, is_query=False):
    if is_query:
        prepared_text = f"task: search result | query: {text}"
    else:
        prepared_text = f"title: none | text: {text}"

    result = client.models.embed_content(
        model="gemini-embedding-2",
        contents=prepared_text
    )

    return np.array(
        result.embeddings[0].values,
        dtype=np.float32
    )


def cosine_similarity(vector_a, vector_b):
    denominator = (
        np.linalg.norm(vector_a)
        * np.linalg.norm(vector_b)
    )

    if denominator == 0:
        return 0.0

    return float(
        np.dot(vector_a, vector_b)
        / denominator
    )


def find_relevant_document(question):
    documents = load_documents()

    question_embedding = get_embedding(
        question,
        is_query=True
    )

    best_document = None
    best_score = -1

    for document in documents:
        chunks = chunk_text(document["content"])

        document_best_score = -1

        for chunk in chunks:
            chunk_embedding = get_embedding(
                chunk,
                is_query=False
            )

            similarity = cosine_similarity(
                question_embedding,
                chunk_embedding
            )

            if similarity > document_best_score:
                document_best_score = similarity

        if document_best_score > best_score:
            best_score = document_best_score
            best_document = document

    return best_document, round(best_score, 4)