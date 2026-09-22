import os
import re


DOCUMENT_DIR = "data/documents"


def tokenize(text):
    text = text.lower()
    words = re.findall(r"[가-힣a-zA-Z0-9]+", text)
    return words


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


def find_relevant_document(question):
    documents = load_documents()
    question_words = tokenize(question)

    best_document = None
    best_score = 0

    for document in documents:
        document_words = tokenize(document["content"])

        score = 0

        for word in question_words:
            score += document_words.count(word)

        if score > best_score:
            best_score = score
            best_document = document

    return best_document, best_score