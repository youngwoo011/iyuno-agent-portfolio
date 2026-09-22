# 🤖 Iyuno AI Agent Portfolio

Iyuno의 **AI Agent Engineer** 채용공고에 제시된 기술 요구사항을 참고하여 제작한 AI Agent 포트폴리오 프로젝트입니다.

사용자의 질문을 입력받아 관련 문서를 검색하고, 검색된 문서를 기반으로 Gemini API가 답변을 생성합니다.  
또한 Calculator Tool Calling, 30개의 평가 질문을 이용한 정량 평가, pytest, GitHub Actions를 구현했습니다.

---

## 1. Target Job Posting

**Company:** Iyuno  
**Position:** AI Agent Engineer  
**Location:** Seoul

채용공고의 주요 요구사항:

- LLM 기반 AI Agent 시스템 설계 및 개발
- RAG 검색·응답 시스템
- Tool Calling
- API Integration
- Multi-step Workflow
- Evaluation 및 성능 개선

Job Posting:

https://iyuno.wd3.myworkdayjobs.com/careers/job/seoul/ai-agent-engineer_jr101122

---

## 2. Project Goal

채용공고에 작성된 기술 요구사항을 단순히 문서로 정리하는 것이 아니라 실제 동작하는 프로그램으로 구현하여 GitHub에서 확인할 수 있도록 하는 것이 목표입니다.

본 프로젝트는 다음과 같은 흐름으로 동작합니다.

```text
사용자 질문
    ↓
문서 Chunking
    ↓
Embedding 생성
    ↓
Vector Similarity Search
    ↓
관련 문서 선택
    ↓
Gemini API
    ↓
문서 기반 답변 생성
    ↓
참고 문서 표시
```

계산식이 입력된 경우에는 Calculator Tool을 사용합니다.

```text
계산 질문
    ↓
Calculator Tool 호출
    ↓
계산 결과 반환
```

---

## 3. Job Requirement Mapping

| 채용공고 요구사항 | 프로젝트 구현 내용 |
|---|---|
| LLM 기반 AI Agent | 사용자 질문에 따라 RAG 또는 Calculator Tool을 사용하는 흐름 구현 |
| RAG | 문서 검색 후 검색된 문서를 Gemini Context로 전달 |
| Chunking | 문서를 일정 길이의 Chunk 단위로 분리 |
| Embedding | Gemini Embedding API를 이용해 질문과 문서를 Vector로 변환 |
| Vector Search | Cosine Similarity를 이용해 질문과 가장 유사한 문서 검색 |
| Tool Calling | Calculator Tool 구현 |
| API Integration | Google Gemini API 연동 |
| Multi-step Workflow | 질문 → 검색/Tool → 답변의 다단계 처리 |
| Evaluation | 30개 질문으로 검색 정확도 및 검색 시간 측정 |
| Reliability | pytest와 GitHub Actions를 이용한 자동 테스트 |

---

## 4. Main Features

### 4.1 RAG

현재 프로젝트에서는 보안 관련 문서를 사용합니다.

```text
data/documents/
├── sql_injection.txt
├── xss.txt
└── password_security.txt
```

사용자가 질문하면 다음 과정을 수행합니다.

```text
문서 불러오기
↓
문서 Chunking
↓
각 Chunk Embedding 생성
↓
질문 Embedding 생성
↓
Cosine Similarity 계산
↓
가장 유사한 문서 선택
↓
Gemini에게 Context로 전달
↓
답변 생성
```

---

## 5. Chunking

문서 전체를 한 번에 처리하지 않고 일정 길이의 Chunk로 나누어 사용합니다.

예:

```text
문서
↓
Chunk 1
Chunk 2
Chunk 3
...
```

각 Chunk는 개별적으로 Embedding Vector로 변환됩니다.

---

## 6. Embedding & Vector Search

질문과 문서 Chunk를 Gemini Embedding API를 이용하여 숫자 Vector로 변환합니다.

그 후 질문 Vector와 문서 Vector 사이의 **Cosine Similarity**를 계산합니다.

```text
질문 Embedding
        ↓
Cosine Similarity
        ↑
문서 Embedding
```

가장 높은 유사도 점수를 가진 문서를 검색 결과로 선택합니다.

예:

```text
질문:
SQL Injection을 어떻게 방어해?

검색 결과:
sql_injection.txt

Similarity Score:
0.7751
```

---

## 7. Citation

검색된 문서의 파일명을 AI 답변 아래에 표시합니다.

예:

```text
질문:
SQL Injection을 어떻게 방어해?

AI 답변:
Prepared Statement 또는 Parameterized Query를 사용하는 것이 중요합니다.

참고 문서:
sql_injection.txt

문서 관련도 점수:
0.7751
```

---

## 8. Tool Calling

계산식이 포함된 질문은 Calculator Tool을 사용합니다.

예:

```text
질문:
125 * 48 계산해줘
```

결과:

```text
Tool Calling 결과

사용된 Tool:
calculator

결과:
6000.0
```

지원 연산:

- Addition
- Subtraction
- Multiplication
- Division

---

## 9. Evaluation

총 **30개의 질문**을 사용하여 문서 검색 성능을 평가했습니다.

질문 구성:

```text
SQL Injection        10개
XSS                  10개
Password Security    10개
```

평가 데이터:

```text
evaluation/questions.json
```

평가 결과:

```text
evaluation/metrics.json
```

### Evaluation Result

| Metric | Result |
|---|---:|
| Total Questions | 30 |
| Correct Retrievals | 29 |
| Retrieval Accuracy | 96.67% |
| Average Retrieval Time | 2.221191 sec |

Embedding 기반 Vector Search를 적용한 후 30개의 질문 중 29개의 질문에서 예상 문서를 정확하게 검색했습니다.

---

## 10. Streamlit Demo

프로젝트의 사용자 인터페이스는 Streamlit으로 구현했습니다.

실행 후 사용자는 웹 화면에서 질문을 입력할 수 있습니다.

```text
질문 입력
↓
RAG 검색
↓
Gemini 답변
↓
참고 문서 표시
```

실행 주소:

```text
http://localhost:8501
```

---

## 11. Testing

Calculator Tool의 기능을 확인하기 위해 pytest 테스트를 작성했습니다.

테스트 항목:

- Addition
- Subtraction
- Multiplication
- Division
- Divide by Zero

테스트 실행:

```bash
python -m pytest
```

테스트 결과:

```text
5 passed in 0.04s
```

---

## 12. GitHub Actions

GitHub Actions를 이용하여 main 브랜치에 Push할 때 자동으로 pytest가 실행되도록 구성했습니다.

Workflow 파일:

```text
.github/workflows/test.yml
```

Workflow:

```text
GitHub Push
↓
GitHub Actions 실행
↓
Python 환경 설정
↓
pytest 실행
↓
Success / Failure 확인
```

현재 GitHub Actions 테스트는 정상적으로 통과합니다.

---

## 13. Tech Stack

- Python 3.14
- Streamlit
- Google Gemini API
- Gemini Embedding API
- NumPy
- python-dotenv
- pytest
- Git
- GitHub
- GitHub Actions

---

## 14. Project Structure

```text
iyuno-agent-portfolio/
│
├── .github/
│   └── workflows/
│       └── test.yml
│
├── app/
│   ├── main.py
│   ├── rag.py
│   ├── tools.py
│   └── test_rag.py
│
├── data/
│   └── documents/
│       ├── sql_injection.txt
│       ├── xss.txt
│       └── password_security.txt
│
├── evaluation/
│   ├── questions.json
│   ├── evaluate.py
│   └── metrics.json
│
├── tests/
│   └── test_tools.py
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 15. Installation

### 1. Repository Clone

```bash
git clone https://github.com/youngwoo011/iyuno-agent-portfolio.git
```

```bash
cd iyuno-agent-portfolio
```

### 2. Virtual Environment

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install Packages

```bash
pip install -r requirements.txt
```

---

## 16. Environment Variable

프로젝트 최상위 폴더에 `.env` 파일을 생성합니다.

```env
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

`.env` 파일은 `.gitignore`에 등록하여 GitHub에 업로드되지 않도록 설정했습니다.

---

## 17. Run Application

```bash
python -m streamlit run app/main.py
```

브라우저에서 다음 주소로 접속합니다.

```text
http://localhost:8501
```

---

## 18. Run Evaluation

```bash
python evaluation/evaluate.py
```

실행 결과:

```text
평가 완료
총 질문 수: 30
정답 수: 29
정확도: 96.67%
평균 검색 시간: 2.221191초
metrics.json 파일이 생성되었습니다.
```

---

## 19. Limitations

현재 프로젝트는 과제용 최소 구현 버전이므로 다음과 같은 한계가 있습니다.

- 테스트 문서가 3개로 제한되어 있습니다.
- 별도의 Vector Database는 사용하지 않고 NumPy를 이용하여 Vector Similarity를 계산합니다.
- 문서 Embedding을 실행 중 반복 생성하기 때문에 검색 시간이 길어질 수 있습니다.
- Calculator Tool만 구현되어 있습니다.
- 실제 데이터베이스 연동은 구현하지 않았습니다.
- Feedback Loop는 구현하지 않았습니다.

---

## 20. Future Improvements

향후 다음과 같은 기능을 추가할 수 있습니다.

- 문서 20개 이상으로 확대
- Vector Database 적용
- Embedding Vector 사전 저장 및 Cache 적용
- 검색 Tool 추가
- 외부 API Tool 추가
- Feedback Loop 구현
- Retrieval 성능 지표 확대
- 실제 서비스 배포

---

## 21. Result

본 프로젝트를 통해 AI Agent Engineer 채용공고에 제시된 기술 요구사항을 실제 코드로 구현해 보았습니다.

주요 구현 내용:

- LLM API Integration
- RAG
- Chunking
- Embedding
- Vector Search
- Citation
- Tool Calling
- Multi-step Workflow
- Evaluation
- pytest
- GitHub Actions

특히 단순히 Gemini에게 질문을 전달하는 프로그램이 아니라, 외부 문서를 검색하고 검색된 정보를 기반으로 답변을 생성하는 RAG 구조를 구현했습니다.

또한 정량 평가와 자동 테스트를 통해 프로젝트의 동작 결과를 확인할 수 있도록 구성했습니다.