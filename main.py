import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("コードアシスタント")

# プログラミング言語の選択
language = st.selectbox(
    "プログラミング言語を選択してください",
    ("python", "VBA", "c", "java")
)

# 機能の選択
function_choice = st.selectbox(
    "機能を選択してください（コード生成、コード解説、コードの改良、コードのエラー修正）",
    ("コード生成", "コード解説", "コードの改良", "コードのエラー修正")
)

# 入力フィールドの表示
user_code = ""
error_message = ""
original_code = ""
improvement_instructions = ""
user_message = ""

if function_choice == "コードのエラー修正":
    user_code = st.text_area(label="修正したいコードを入力してください")
    error_message = st.text_area(label="エラーメッセージを入力してください")
elif function_choice == "コードの改良":
    original_code = st.text_area(label="元のコードを入力してください")
    improvement_instructions = st.text_area(label="改良方針を入力してください（例.コードを読みやすくしてください）")
elif function_choice == "コード生成":
    user_message = st.text_input(label="コードに関するリクエストを入力してください")
elif function_choice == "コード解説":
    user_message = st.text_area(label="コードを入力してください")

# 実行ボタン
execute = st.button("実行")

if execute:
    if function_choice == "コードのエラー修正" and user_code and error_message:
        prompt = f"あなたはユーザーの指示に基づいて{language}コードのエラーを修正する親切なアシスタントです。以下のコードのエラーを修正してください。コード：{user_code}。エラーメッセージ：{error_message}"
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
            ],
        )
        response = completion.choices[0].message.content
        st.subheader(f"修正された{language.capitalize()}コード:")
        st.code(response)

    elif function_choice == "コードの改良" and original_code and improvement_instructions:
        prompt = f"あなたはユーザーの指示に基づいて{language}コードを改良する親切なアシスタントです。以下のコードを指示に従って改良してください。元のコード：{original_code}。改良方針：{improvement_instructions}"
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
            ],
        )
        response = completion.choices[0].message.content
        st.subheader(f"改良された{language.capitalize()}コード:")
        st.code(response)

    elif function_choice == "コード生成" and user_message:
        prompt = f"あなたはユーザーの指示に基づいて{language}コードを提供する親切なアシスタントです。"
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_message},
            ],
        )
        response = completion.choices[0].message.content
        st.subheader(f"生成された{language.capitalize()}コード:")
        st.code(response)

    elif function_choice == "コード解説" and user_message:
        prompt = f"あなたはユーザーの指示に基づいて{language}コードの詳細な解説を提供する親切なアシスタントです。"
        completion = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_message},
            ],
        )
        response = completion.choices[0].message.content
        st.subheader(f"{language.capitalize()}コードの解説:")
        st.write(response)
