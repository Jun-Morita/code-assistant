# コードアシスタント

## 概要

GPT-4oを用いたコードアシスタントウェブアプリ

## 環境構築

> conda create -n code-assistant python=3.11
> pip install openai==1.35.10
> pip install streamlit==1.36.0

## OpenAI API Key

.streamlitフォルダ内にsecrets.tomlファイルを用意し、以下のコードを記述のこと。

> OPENAI_API_KEY = "xxxxxxxx"

## 実行方法

> conda activate code-assistant
> streamlit run main.py

