from rag import find_relevant_document

question = "SQL Injection을 어떻게 방어해?"

document, score = find_relevant_document(question)

if document:
    print("가장 관련 있는 문서:")
    print(document["filename"])
    print("관련도 점수:", score)
else:
    print("관련 문서를 찾지 못했습니다.")