import streamlit as st
import whisper
from transformers import pipeline
import os

# --- Page Setup ---
st.set_page_config(page_title="Lectura - AI Lecture Assistant", page_icon="📝", layout="wide")
st.title("🎓 Lectura an AI Lecture Voice-to-Notes Generator")
st.markdown("Automated Transcription, Summarization, and Study Material Generation.")

# --- Load Models (Cached for speed) ---
@st.cache_resource
def load_ai_models():
    # 1. Speech-to-Text: OpenAI Whisper (Free/Local)
    st.info("🔄 Loading Whisper (Transcription)...")
    transcriber = whisper.load_model("base")
    
    # 2. Summarization: BART-Large-CNN
    st.info("🔄 Loading BART (Summarization)...")
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    
    # 3. Flashcards/Quiz: FLAN-T5
    st.info("🔄 Loading T5 (Study Aids)...")
    generator = pipeline("text2text-generation", model="google/flan-t5-base")
    
    return transcriber, summarizer, generator

# Store models in session state
if 'models' not in st.session_state:
    st.session_state.models = load_ai_models()

transcriber, summarizer, generator = st.session_state.models

# --- Sidebar ---
st.sidebar.header("Step 1: Upload Audio")
audio_file = st.sidebar.file_uploader("Upload Lecture (MP3, WAV, M4A)", type=["mp3", "wav", "m4a"])

if audio_file:
    st.sidebar.audio(audio_file)
    if st.sidebar.button("🚀 Process Lecture"):
        with st.spinner("AI is analyzing your lecture..."):
            # Save temporary file
            with open("temp.mp3", "wb") as f:
                f.write(audio_file.getbuffer())
            
            # Step 1: Transcription [cite: 30]
            st.session_state.transcript = transcriber.transcribe("temp.mp3")["text"]
            
            # Step 2: Summarization [cite: 30]
            # Limiting text length for the free model buffer
            summary_output = summarizer(st.session_state.transcript[:1024], max_length=150, min_length=50)
            st.session_state.summary = summary_output[0]['summary_text']
            
            # Step 3: Quiz Generation [cite: 30]
            q_prompt = f"generate 3 questions from: {st.session_state.summary}"
            st.session_state.quiz = generator(q_prompt, max_length=150)[0]['generated_text']
            
            # Step 4: Flashcard Generation [cite: 3]
            f_prompt = f"create flashcards from: {st.session_state.summary}"
            st.session_state.flashcards = generator(f_prompt, max_length=150)[0]['generated_text']
            
            os.remove("temp.mp3") # Clean up
            st.success("✅ Analysis Done!")

# --- Main Results Display ---
if 'transcript' in st.session_state:
    t1, t2, t3, t4 = st.tabs(["📝 Summary", "❓ Practice Quiz", "🗂️ Flashcards", "📜 Full Transcript"])
    
    with t1:
        st.subheader("Key Takeaways")
        st.write(st.session_state.summary)
        st.download_button("Download Summary", st.session_state.summary, file_name="lecture_summary.txt")

    with t2:
        st.subheader("Knowledge Check")
        st.write(st.session_state.quiz)

    with t3:
        st.subheader("Flashcard Concepts")
        st.info(st.session_state.flashcards)
        
    with t4:
        st.subheader("Full Text Transcript")
        st.text_area("Original Content", st.session_state.transcript, height=400)
else:
    st.warning("Please upload an audio file to begin.")