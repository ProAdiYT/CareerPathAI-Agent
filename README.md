  # CareerPathAI Agent 🎓🤖

This is an AI-powered Career Guidance Agent built with FastAPI that helps users explore suitable career paths based on their interests and preferences.

## 🚀 Features

- Uses OpenAI + HuggingFace API for intelligent response
- User input-based career suggestions
- Lightweight and fast with FastAPI
- Clean and modular structure

## 🧠 Tech Stack

- Python
- FastAPI
- OpenAI API
- HuggingFace Transformers

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/ProAdiYT/CareerPathAI-Agent.git
cd CareerPathAI-Agent

2️⃣ Create and Activate Virtual Environment

python -m venv venv
venv\Scripts\activate   # For Windows

3️⃣ Install Dependencies

pip install -r requirements.txt

4️⃣ Setup Environment Variables
Create a .env file in the root directory like this:

OPENAI_API_KEY=your_openai_key
HUGGINGFACEHUB_API_TOKEN=your_huggingface_key

Or copy from the example:

copy .env.example .env  # On Windows

5️⃣ Run the App

uvicorn app.main:app --reload
Visit: http://127.0.0.1:8000

📂 Project Structure

CareerPathAI-Agent/
├── app/
│   ├── main.py
│   └── ...
├── requirements.txt
├── .env.example
├── README.md
└── ...

📃 License
This project is open-source. Feel free to fork and enhance.

