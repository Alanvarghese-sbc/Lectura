
# 🎓 Lectura: AI-Powered Lecture Voice-to-Notes Generator

**Lectura** is an AI-powered assistant that transforms spoken lectures into structured study materials, helping students focus on learning rather than note-taking. It automatically generates summaries, quizzes, and flashcards from lecture audio.  

---

## 📝 Problem Statement
Students often struggle to listen and take notes simultaneously during lectures, which can lead to missing key points. **Lectura** solves this by converting spoken lectures into:  
- Clear, concise study notes  
- Practice quizzes for active recall  
- Flashcards for quick revision  

This ensures students can focus on understanding while retaining key concepts efficiently.

---

## 🛠 Tech Stack
- **Python** – Core logic and scripting  
- **Whisper (OpenAI)** – Speech-to-text transcription  
- **BART (Hugging Face)** – Text summarization  
- **T5 (Google)** – Quiz and flashcard generation  
- **Streamlit** – Interactive web dashboard  

---

## ✨ Features
1. **Automated Transcription** – Converts lecture audio into text.  
2. **Summarization** – Generates concise study notes from transcripts.  
3. **Active Recall** – Automatically creates quizzes and flashcards.  
4. **Downloadable Content** – Allows exporting summaries for offline study.  

---

## ⚡ How It Works
1. Upload your lecture audio (MP3, WAV, M4A) through the sidebar.  
2. AI processes the audio using **Whisper** to transcribe the lecture.  
3. **BART** summarizes the transcript into actionable study notes.  
4. **T5** generates quizzes and flashcards based on the summary.  
5. Access results via tabs: Summary, Practice Quiz, Flashcards, Full Transcript.  

---

## 📂 Installation & Requirements

Install dependencies via `pip`:

```bash
pip install streamlit openai-whisper transformers torch torchaudio
````

Ensure `ffmpeg` is installed for audio processing.

Run the app:

```bash
streamlit run app.py
```

---

## 🖥 Usage

* Upload lecture audio in the sidebar.
* Click **"🚀 Process Lecture"** to analyze.
* Explore results in four tabs:

  * **Summary** – Key takeaways
  * **Practice Quiz** – Test your knowledge
  * **Flashcards** – Quick revision cards
  * **Full Transcript** – Complete lecture text

---

## 📦 Project Files

* `app.py` – Main Streamlit application
* `requirements.txt` – Python packages
* Audio dependencies – `ffmpeg`

---

## 📚 References

* Whisper (OpenAI) – Speech-to-Text transcription
* BART (Hugging Face) – Summarization model
* T5 (Google) – Text-to-text generation for quizzes & flashcards

```

