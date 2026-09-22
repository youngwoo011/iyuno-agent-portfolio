# \# 🤖 Iyuno AI Agent Portfolio

# 

# Iyuno의 \*\*AI Agent Engineer\*\* 채용공고에 제시된 기술 요구사항을 참고하여 제작한 AI Agent 포트폴리오 프로젝트입니다.

# 

# 사용자의 질문에 적합한 문서를 검색하고, 검색된 문서를 근거로 Gemini API가 답변을 생성합니다.  

# 또한 간단한 Calculator Tool Calling 기능과 30개의 질문을 이용한 검색 성능 평가 기능을 구현했습니다.

# 

# \---

# 

# \## 1. Target Job Posting

# 

# \*\*Company:\*\* Iyuno  

# \*\*Position:\*\* AI Agent Engineer  

# \*\*Location:\*\* Seoul

# 

# 채용공고에서 확인한 주요 기술 요구사항:

# 

# \- LLM 기반 AI Agent 시스템 설계 및 개발

# \- RAG 검색·응답 시스템

# \- Tool Calling

# \- API 연동

# \- 다단계 Workflow

# \- Evaluation 및 성능 개선

# 

# Job Posting:

# 

# https://iyuno.wd3.myworkdayjobs.com/careers/job/seoul/ai-agent-engineer\_jr101122

# 

# \---

# 

# \## 2. Project Goal

# 

# 채용공고의 기술 요구사항을 단순히 문서로 정리하는 것이 아니라 실제로 동작하는 프로그램으로 구현하여 GitHub에서 확인할 수 있도록 하는 것이 목표입니다.

# 

# 프로젝트의 기본 동작 과정은 다음과 같습니다.

# 

# ```text

# 사용자 질문

# &#x20;   ↓

# 질문 분석

# &#x20;   ↓

# 관련 문서 검색

# &#x20;   ↓

# Gemini API

# &#x20;   ↓

# 문서를 근거로 답변 생성

# &#x20;   ↓

# 답변 + 참고 문서 표시

# ```

# 

# 계산식이 입력된 경우에는 Calculator Tool을 사용합니다.

# 

# ```text

# 사용자 계산 질문

# &#x20;   ↓

# Calculator Tool 호출

# &#x20;   ↓

# 계산 결과 반환

# ```

# 

# \---

# 

# \## 3. Job Requirement Mapping

# 

# | 채용공고 요구사항 | 프로젝트 구현 내용 |

# |---|---|

# | LLM 기반 AI Agent | 사용자 질문에 따라 RAG 또는 Calculator Tool을 사용하는 흐름 구현 |

# | RAG 검색·응답 | 로컬 보안 문서에서 관련 문서를 검색한 후 Gemini에 전달 |

# | Tool Calling | Calculator Tool 구현 |

# | API Integration | Google Gemini API 연동 |

# | Multi-step Workflow | 질문 → 검색/Tool → AI 응답의 다단계 처리 구현 |

# | Evaluation | 30개의 질문으로 문서 검색 정확도와 검색 시간 측정 |

# 

# \---

# 

# \## 4. Main Features

# 

# \### RAG

# 

# 현재 프로젝트에는 다음과 같은 보안 관련 문서가 포함되어 있습니다.

# 

# ```text

# data/documents/

# ├── sql\_injection.txt

# ├── xss.txt

# └── password\_security.txt

# ```

# 

# 사용자가 질문하면 질문에 포함된 단어와 각 문서의 내용을 비교하여 가장 관련성이 높은 문서를 선택합니다.

# 

# 검색된 문서 내용은 Gemini에게 Context로 전달되며, Gemini는 해당 문서를 참고하여 답변을 생성합니다.

# 

# \---

# 

# \### Citation

# 

# AI 답변 아래에 실제 검색에 사용된 문서 이름을 표시합니다.

# 

# 예:

# 

# ```text

# 질문:

# SQL Injection을 어떻게 방어해?

# 

# AI 답변:

# Prepared Statement 또는 Parameterized Query를 사용하는 것이 중요합니다.

# 

# 참고 문서:

# sql\_injection.txt

# ```

# 

# \---

# 

# \### Tool Calling

# 

# 계산식이 포함된 질문은 Calculator Tool을 사용합니다.

# 

# 예:

# 

# ```text

# 질문:

# 125 \* 48 계산해줘

# 

# Tool:

# calculator

# 

# 결과:

# 6000.0

# ```

# 

# 지원 연산:

# 

# \- Addition

# \- Subtraction

# \- Multiplication

# \- Division

# 

# \---

# 

# \## 5. Evaluation

# 

# 총 \*\*30개의 평가 질문\*\*을 사용하여 문서 검색 성능을 평가했습니다.

# 

# 평가 데이터:

# 

# ```text

# evaluation/questions.json

# ```

# 

# 평가 결과:

# 

# ```text

# evaluation/metrics.json

# ```

# 

# \### Evaluation Result

# 

# | Metric | Result |

# |---|---:|

# | Total Questions | 30 |

# | Correct Retrievals | 26 |

# | Retrieval Accuracy | 86.67% |

# | Average Retrieval Time | 0.000397 sec |

# 

# 평가 질문은 SQL Injection, XSS, Password Security 분야별로 구성했습니다.

# 

# \---

# 

# \## 6. Tech Stack

# 

# \- Python

# \- Streamlit

# \- Google Gemini API

# \- python-dotenv

# 

# \---

# 

# \## 7. Project Structure

# 

# ```text

# iyuno-agent-portfolio/

# │

# ├── app/

# │   ├── main.py

# │   ├── rag.py

# │   ├── tools.py

# │   └── test\_rag.py

# │

# ├── data/

# │   └── documents/

# │       ├── sql\_injection.txt

# │       ├── xss.txt

# │       └── password\_security.txt

# │

# ├── evaluation/

# │   ├── questions.json

# │   ├── evaluate.py

# │   └── metrics.json

# │

# ├── tests/

# │

# ├── .gitignore

# ├── README.md

# └── requirements.txt

# ```

# 

# \---

# 

# \## 8. Installation

# 

# \### 1. Repository Clone

# 

# ```bash

# git clone https://github.com/yungwoo011/iyuno-agent-portfolio.git

# cd iyuno-agent-portfolio

# ```

# 

# \### 2. Virtual Environment

# 

# ```bash

# python -m venv .venv

# ```

# 

# Windows PowerShell:

# 

# ```powershell

# .\\.venv\\Scripts\\Activate.ps1

# ```

# 

# \### 3. Install Packages

# 

# ```bash

# pip install -r requirements.txt

# ```

# 

# \---

# 

# \## 9. Environment Variable

# 

# 프로젝트 최상위 폴더에 `.env` 파일을 생성합니다.

# 

# ```env

# GEMINI\_API\_KEY=YOUR\_GEMINI\_API\_KEY

# ```

# 

# 보안을 위해 `.env` 파일은 GitHub에 업로드하지 않습니다.

# 

# \---

# 

# \## 10. Run Application

# 

# ```bash

# python -m streamlit run app/main.py

# ```

# 

# 브라우저에서 다음 주소로 접속합니다.

# 

# ```text

# http://localhost:8501

# ```

# 

# \---

# 

# \## 11. Run Evaluation

# 

# ```bash

# python evaluation/evaluate.py

# ```

# 

# 평가가 완료되면 다음과 같은 결과가 출력됩니다.

# 

# ```text

# 총 질문 수: 30

# 정답 수: 26

# 정확도: 86.67%

# 평균 검색 시간: 0.000397초

# ```

# 

# 결과는 `evaluation/metrics.json`에도 저장됩니다.

# 

# \---

# 

# \## 12. Limitations

# 

# 현재 프로젝트는 과제용 최소 구현 버전이므로 다음과 같은 한계가 있습니다.

# 

# \- 현재 RAG 검색은 Embedding 기반 Vector Search가 아닌 단순 단어 일치 기반 검색을 사용합니다.

# \- 현재 테스트 문서는 3개만 사용하고 있습니다.

# \- Calculator Tool은 간단한 사칙연산만 지원합니다.

# \- 실제 서비스 수준의 데이터베이스 연동은 구현하지 않았습니다.

# \- Feedback Loop는 구현하지 않았습니다.

# 

# 향후에는 Embedding과 Vector Database를 적용하여 의미 기반 검색 기능을 개선할 수 있습니다.

# 

# \---

# 

# \## 13. Result

# 

# 본 프로젝트를 통해 채용공고에 나온 AI Agent 관련 요구사항을 실제 코드로 구현해 보았습니다.

# 

# 특히 다음 기능을 직접 구현했습니다.

# 

# \- LLM API 연동

# \- RAG 기반 문서 검색 및 답변

# \- Citation

# \- Tool Calling

# \- Multi-step Workflow

# \- 정량 평가

# 

# 단순히 AI에게 질문하는 프로그램이 아니라, 외부 문서를 검색하고 Tool을 선택하여 사용할 수 있는 기본적인 AI Agent 구조를 구현하는 것을 목표로 했습니다.

