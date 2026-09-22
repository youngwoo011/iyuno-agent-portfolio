import os
import re

import streamlit as st
from dotenv import load_dotenv
from google import genai

from rag import find_relevant_document
from tools import calculator

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

st.set_page_config(
    page_title="Iyuno AI Agent Portfolio",
    page_icon="🤖"
)

st.title("🤖 Iyuno AI Agent Portfolio")
st.write("AI Agent Engineer 채용공고의 요구 기술을 구현하는 포트폴리오 프로젝트입니다.")

question = st.text_input("질문을 입력하세요")

def try_calculator(question):
    pattern = r"(\d+)\s*([\+\-\*/xX×])\s*(\d+)"
    match = re.search(pattern, question)

    if not match:
        return None

    a = float(match.group(1))
    symbol = match.group(2)
    b = float(match.group(3))

    if symbol == "+":
        operation = "add"
    elif symbol == "-":
        operation = "subtract"
    elif symbol in ["*", "x", "X", "×"]:
        operation = "multiply"
    elif symbol == "/":
        operation = "divide"
    else:
        return None

    result = calculator(a, b, operation)

    return {
        "a": a,
        "b": b,
        "operation": operation,
        "result": result
    }


if st.button("질문하기"):
    if not question:
        st.warning("질문을 입력해주세요.")

    elif not api_key:
        st.error("Gemini API 키를 찾을 수 없습니다.")

    else:
        try:
            tool_result = try_calculator(question)

            if tool_result:
                st.subheader("Tool Calling 결과")
                st.write(f"사용된 Tool: calculator")
                st.write(f"결과: {tool_result['result']}")

            else:
                document, score = find_relevant_document(question)

                if document is None:
                    st.warning("관련 문서를 찾지 못했습니다.")

                else:
                    client = genai.Client(api_key=api_key)

                    prompt = f"""
다음 문서를 참고해서 사용자의 질문에 답변하세요.

반드시 제공된 문서의 내용을 우선적으로 사용하세요.
문서에 없는 내용은 확실하지 않다면 추측하지 마세요.

[참고 문서]
{document["content"]}

[사용자 질문]
{question}
"""

                    with st.spinner("AI가 문서를 검색하고 답변을 생성하고 있습니다..."):
                        response = client.models.generate_content(
                            model="gemini-3.5-flash-lite",
                            contents=prompt
                        )

                    st.subheader("AI 답변")
                    st.markdown(response.text)

                    st.subheader("참고 문서")
                    st.write(document["filename"])

                    st.caption(f"문서 관련도 점수: {score}")

        except Exception as e:
            st.error(f"오류가 발생했습니다: {e}")