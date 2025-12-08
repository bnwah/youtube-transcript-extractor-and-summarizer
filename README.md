# 🎥 YouTube Transcription Extractor & Summarizer

A simple Python tool that extracts YouTube video transcripts and generates concise summaries using the OpenAI API.

This project is designed for learners, researchers, and content creators who want quick insights from long YouTube videos without watching the entire thing.

---

## ✨ Features
- **Extract transcripts** from YouTube videos (when available)
- **Automatically clean the transcript** (removes timestamps + formatting)
- **Generate summaries** using the OpenAI API
- **Save results** to output files
- **Simple, lightweight, and beginner-friendly**

---

## 🛠️ Tech Stack
- Python 3.10+
- `youtube-transcript-api`
- `openai`
- `python-dotenv`

---

## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/bnwah/youtube-transcript-summarizer.git
cd youtube-transcript-summarizer
```
### 2. Create a virtual environment
```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```
### 3. Install dependencies
```
pip install -r requirements.txt
```
### 4. Add your OpenAI API key

Create a .env file in the project root:
```
OPENAI_API_KEY=your_api_key_here
```

---

## ▶️ Usage
Run the script with a YouTube link:
```
python main.py https://www.youtube.com/watch?v=YOUR_VIDEO_ID
```

---

## 🚀 Future Improvements
- Add web or GUI interface
- Add bullet vs paragraph summary mode
- Add export options (PDF, Markdown)

---

## 🤝 Contributing
Pull requests and suggestions are welcome! Feel free to open an issue.

