# modules/notekeeper.py
import json
import os

NOTES_FILE = "data/notes.json"

def _load_notes():
    if not os.path.exists(NOTES_FILE):
        return []
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def _save_notes(notes):
    with open(NOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(notes, f, indent=2)

def handle(text):
    text_lower = text.lower()

    if "show" in text_lower or "list" in text_lower:
        notes = _load_notes()
        return "📝 Stored Notes:\n- " + "\n- ".join(notes) if notes else "No notes yet."

    elif "clear" in text_lower:
        _save_notes([])
        return "All notes cleared."

    else:
        notes = _load_notes()
        notes.append(text)
        _save_notes(notes)
        return "Note saved."
