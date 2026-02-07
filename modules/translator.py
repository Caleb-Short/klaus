# modules/translator.py
import requests

def handle(text):
    prompt = (
        "Translate the following text to the most appropriate language (German or English). "
        "Keep the translation clean and literal unless the phrase is idiomatic.\n\n"
        f"Text: {text}\nTranslation:"
    )

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": prompt, "stream": False}
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "Translation module is offline."
