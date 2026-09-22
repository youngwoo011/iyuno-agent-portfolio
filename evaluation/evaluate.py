import json
import os
import sys
import time

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "app"))

from rag import find_relevant_document


QUESTIONS_FILE = os.path.join(
    os.path.dirname(__file__),
    "questions.json"
)

METRICS_FILE = os.path.join(
    os.path.dirname(__file__),
    "metrics.json"
)


with open(QUESTIONS_FILE, "r", encoding="utf-8") as file:
    questions = json.load(file)


correct = 0
total_time = 0
results = []


for item in questions:
    question = item["question"]
    expected_document = item["expected_document"]

    start_time = time.perf_counter()

    document, score = find_relevant_document(question)

    end_time = time.perf_counter()

    elapsed_time = end_time - start_time
    total_time += elapsed_time

    predicted_document = (
        document["filename"]
        if document is not None
        else None
    )

    is_correct = predicted_document == expected_document

    if is_correct:
        correct += 1

    results.append({
        "question": question,
        "expected_document": expected_document,
        "predicted_document": predicted_document,
        "score": score,
        "correct": is_correct,
        "response_time": round(elapsed_time, 6)
    })


total_questions = len(questions)

accuracy = (
    correct / total_questions * 100
    if total_questions > 0
    else 0
)

average_response_time = (
    total_time / total_questions
    if total_questions > 0
    else 0
)


metrics = {
    "total_questions": total_questions,
    "correct_answers": correct,
    "accuracy_percent": round(accuracy, 2),
    "average_response_time_seconds": round(
        average_response_time,
        6
    ),
    "results": results
}


with open(METRICS_FILE, "w", encoding="utf-8") as file:
    json.dump(
        metrics,
        file,
        ensure_ascii=False,
        indent=2
    )


print("평가 완료")
print(f"총 질문 수: {total_questions}")
print(f"정답 수: {correct}")
print(f"정확도: {accuracy:.2f}%")
print(
    f"평균 검색 시간: "
    f"{average_response_time:.6f}초"
)
print("metrics.json 파일이 생성되었습니다.")