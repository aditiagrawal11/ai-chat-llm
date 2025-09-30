# AI Chat LLM 🤖

An intelligent chatbot powered by a large language model (LLM), built using Hugging Face Transformers and Flask. This project demonstrates how to integrate a pretrained LLM (like GPT-2) into a modular Python application with preprocessing, API endpoints, and test coverage.

---

## 🚀 Features
- Text-based chatbot interface
- Uses GPT-2 (~124M) or GPT-2 Medium (~345M) via Hugging Face
- Configurable generation parameters (temperature, top-p, max length)
- Modular codebase: model, preprocessing, API, and tests
- Sample conversation data for training or testing
- Flask-based REST API for integration

---

## 🧱 Project Structure
ai-chat-llm/ ├── config/ # YAML config for model parameters ├── data/ # Sample conversation data ├── models/ # LLM wrapper class ├── utils/ # Preprocessing functions ├── app/ # Flask app and chat interface ├── tests/ # Unit tests ├── requirements.txt # Python dependencies ├── README.md # Project overview


---

## ⚙️ Setup Instructions

### 1. Clone the repo
```bash
git clone https://github.com/aditiagrawal11/ai-chat-llm.git
cd ai-chat-llm
pip install -r requirements.txt
python app/main.py
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d "{\"message\": \"Hello\"}"
pytest tests/
This project uses Hugging Face’s gpt2 or gpt2-medium models. You can switch models by editing config/config.yaml.
MIT License

Copyright (c) 2025 Aditi Agrawal

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


