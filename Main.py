# 🔧 Installa le librerie necessarie
!pip install -q openai-whisper pydub python-docx fpdf tqdm
!sudo apt update && sudo apt install -y ffmpeg

# ✅ Import library
import whisper
import torch
from google.colab import files
from tqdm.notebook import tqdm
from docx import Document
from fpdf import FPDF
import time
import os

# ✅ Choose device
device = "cuda" if torch.cuda.is_available() else "cpu"
print("📌 Dispositivo disponibile:", device)

# ✅ load the model
model = whisper.load_model("large" if device == "cuda" else "medium", device=device)
print("✅ Modello Whisper caricato con successo!")

# 🔄 Transcription function
def transcribe_audio(file_path, language="auto"):
    print("🔍 Inizio trascrizione...\n")
    result = model.transcribe(file_path, language=language, word_timestamps=True, verbose=False)
    segments = result.get("segments", [])
    full_text = ""
    for i, segment in enumerate(tqdm(segments, desc="⏳ Avanzamento trascrizione", unit="segmento")):
        print(segment['text'], end=" ", flush=True)
        full_text += segment['text'] + " "
        time.sleep(0.05)  # Simula avanzamento per renderlo visibile
    print("\n\n✅ Trascrizione completata!")
    return full_text.strip()

# 📁 upload audio file
uploaded = files.upload()
file_name = next(iter(uploaded))
print(f"📥 File caricato: {file_name}")

# 🌍 Supported languages
lingue_supportate = ['zh', 'es', 'en', 'hi', 'ar', 'pt', 'ru', 'ja', 'de', 'fr', 'it', 'auto']
print("\n🌐 Languages: zh (Cinese), es (Spagnolo), en (Inglese), hi (Hindi), ar (Arabo), pt (Portoghese), ru (Russo), ja (Giapponese), de (Tedesco), fr (Francese), it (Italiano), auto (rilevamento automatico)")
language = input("Choose the language (es. 'it' for italian, 'en' for inglese, 'auto' for automatic): ").strip()

if language not in lingue_supportate:
    print("⚠️ not supported language. Use 'auto' as default.")
    language = "auto"

# 📝 Transcription
transcription = transcribe_audio(file_name, language=language)

# 💾 saving function
def save_as_txt(text, filename="trascrizione.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
    files.download(filename)

def save_as_pdf(text, filename="trascrizione.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, text)
    pdf.output(filename)
    files.download(filename)

def save_as_docx(text, filename="trascrizione.docx"):
    doc = Document()
    doc.add_paragraph(text)
    doc.save(filename)
    files.download(filename)

# 🗂️ Export transcription
print("\n📤 In which format do you want to save your transcription?")
print("1 = .txt\n2 = .pdf\n3 = .docx")
formato = input("Enter the corresponding  number to the desired format: ").strip()

if formato == "1":
    save_as_txt(transcription)
elif formato == "2":
    save_as_pdf(transcription)
elif formato == "3":
    save_as_docx(transcription)
else:
    print("❌ Formato non valido. Nessun file salvato.")
