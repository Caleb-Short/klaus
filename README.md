Klaus is a fully local, bilingual(sometimmes) AI assistant built with Python, Gradio, and Ollama. 

Features

- Text-based chatbot UI powered by Gradio
- Expert in programming (C, Python, Java) and math
- Translator module: English and German
- Notekeeper module: Save and recall short notes
- Code helper module: Programming advice and fixes
- 100% local – no API keys, no cloud, no spying

Getting Started

Requirements:

- Python 3.10+
- [Ollama](https://ollama.com/) installed locally
- A model like `mistral` downloaded (`ollama pull mistral`)

Setup

```bash
git clone https://github.com/yourusername/klaus.git
cd klaus
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
ollama serve
python app.py
