# core/llm_client.py
import requests

def ask_klaus(user_input, chat_history):
    system_prompt = (
        "You are Klaus, a highly intelligent, formal AI assistant who speaks in a precise and serious tone. "
        "You are blunt when necessary, with a stiff German sense of humor. "
        "You specialize in mathematics and software engineering. "
        "You explain things clearly and logically. You will admit it—reluctantly—when you do not know something."
    )

    full_prompt = system_prompt + "\n\n"
    for entry in chat_history:
        if "user" in entry:
            full_prompt += f"User: {entry['user']}\n"
        elif "klaus" in entry:
            full_prompt += f"Klaus: {entry['klaus']}\n"
    full_prompt += f"User: {user_input}\nKlaus:"

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": "mistral", "prompt": full_prompt, "stream": False}
    )

    if response.status_code == 200:
        return response.json()["response"].strip()
    else:
        return "I'm having trouble thinking right now. Check that the Ollama server is running."
