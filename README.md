# 🌐 LinkBrief AI

An AI-powered Streamlit application that summarizes content from YouTube videos and websites using LangChain and Groq LLMs.

---

## 🚀 Features

- Summarize YouTube videos using video URLs
- Summarize website/blog content from URLs
- Uses LangChain map-reduce summarization
- Powered by Groq Llama 3.3 70B model
- Clean and interactive Streamlit UI

---

## 🛠️ Tech Stack

- Python
- Streamlit
- LangChain
- Groq API
- WebBaseLoader
- YouTubeLoader

---

## 📦 Installation

Clone the repository:

```bash
git clone https://github.com/Meghana-Poojary/Youtube-Video-Web-Summarizer.git
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 🔑 Setup

Paste the Groq API key in the sidebar input field after running the app.

---

## 📄 Supported Inputs

- YouTube video URLs
- Website or blog URLs

Examples:

```text
https://www.youtube.com/watch?v=...
https://example.com/article
```

---

## ⚙️ How It Works

1. User provides a URL
2. Content is loaded using:
   - `YoutubeLoader`
   - `WebBaseLoader`
3. Text is split into chunks
4. LangChain Map-Reduce summarization chain processes the content
5. Final concise summary is displayed

---

## 📁 Project Structure

```text
├── app.py
├── requirements.txt
└── README.md
```

## 📜 License

This project is open-source and available under the MIT License.