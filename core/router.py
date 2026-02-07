# core/router.py
from core.llm_client import ask_klaus
from modules import translator, notekeeper, code_helper

def route_input(user_input, chat_history):
    lowered = user_input.lower()

    if "translate" in lowered:
        return translator.handle(user_input)
    elif "note" in lowered or "remember" in lowered:
        return notekeeper.handle(user_input)
    elif any(word in lowered for word in ["code", "bug", "python", "java", "c++"]):
        return code_helper.handle(user_input)
    else:
        return ask_klaus(user_input, chat_history)
