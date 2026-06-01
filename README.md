# Groq LangChain Minimal Example

This workspace contains a very simple example to show your team how to call the Groq API (OpenAI-compatible endpoint) using Python.

Files:
- [example.py](example.py) — Minimal Groq API example
- [.env.example](.env.example) — Example environment variables
- [requirements.txt](requirements.txt) — Python dependencies

## Quick start

1. Create and activate a Python virtual environment (optional but recommended):

```bash
python -m venv .venv
source .venv/Scripts/activate   # Windows: .venv\Scripts\activate
```

2. Install dependencies:

pip install langchain langchain-core langchain-groq

```bash
pip install -r requirements.txt
```

3. Set your Groq API key and base URL (copy `.env.example` to `.env` if preferred):

```bash
export GROQ_API_KEY="gsk-..."                              # PowerShell: $env:GROQ_API_KEY="gsk-..."
export OPENAI_BASE_URL="https://api.groq.com/openai/v1"   # optional
export MODEL="llama-3.3-70b-versatile"                     # optional
```

4. Run the example:

```bash
python example.py
```

## What the example does

- Uses Python's `requests` library to call Groq's OpenAI-compatible endpoint.
- Sends a simple chat prompt and prints the model response.
- No external LLM SDKs required — just HTTP + JSON.

## Notes

- Replace `GROQ_API_KEY` with your actual Groq API key from https://console.groq.com.
- The `OPENAI_BASE_URL` defaults to `https://api.groq.com/openai/v1` if not set.
- The `MODEL` defaults to `llama-3.3-70b-versatile` if not set.

