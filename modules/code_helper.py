# modules/code_helper.py
import requests

def handle(text):
    prompt = (
        "You are Klaus, an expert in software development. "
        "Help with the following programming-related question:\n\n"
        f"{text}\n\nAnswer:"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Code helper module is offline."
