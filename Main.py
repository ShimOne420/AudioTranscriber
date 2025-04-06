# 🔧 Installa le librerie necessarie
!pip install -q openai-whisper pydub python-docx fpdf tqdm
!sudo apt update && sudo apt install -y ffmpeg

# ✅ Importa le librerie
import whisper
import torch
from google.colab import files
from tqdm.notebook import tqdm
from docx import Document
from fpdf import FPDF
import time
import os

# ✅ Seleziona il dispositivo
device = "cuda" if torch.cuda.is_available() else "cpu"
print("📌 Dispositivo disponibile:", device)

# ✅ Carica il modello
model = whisper.load_model("large" if device == "cuda" else "medium", device=device)
print("✅ Modello Whisper caricato con successo!")

# 🔄 Funzione di trascrizione avanzata
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

# 📁 Carica il file audio
uploaded = files.upload()
file_name = next(iter(uploaded))
print(f"📥 File caricato: {file_name}")

# 🌍 Lingue supportate
lingue_supportate = ['zh', 'es', 'en', 'hi', 'ar', 'pt', 'ru', 'ja', 'de', 'fr', 'it', 'auto']
print("\n🌐 Lingue disponibili: zh (Cinese), es (Spagnolo), en (Inglese), hi (Hindi), ar (Arabo), pt (Portoghese), ru (Russo), ja (Giapponese), de (Tedesco), fr (Francese), it (Italiano), auto (rilevamento automatico)")
language = input("Inserisci la lingua (es. 'it' per italiano, 'en' per inglese, 'auto' per automatico): ").strip()

if language not in lingue_supportate:
    print("⚠️ Lingua non supportata. Uso 'auto' come default.")
    language = "auto"

# 📝 Trascrizione
transcription = transcribe_audio(file_name, language=language)

# 💾 Funzioni di salvataggio
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

# 🗂️ Esporta la trascrizione
print("\n📤 In quale formato vuoi salvare la trascrizione?")
print("1 = .txt\n2 = .pdf\n3 = .docx")
formato = input("Inserisci il numero corrispondente al formato desiderato: ").strip()

if formato == "1":
    save_as_txt(transcription)
elif formato == "2":
    save_as_pdf(transcription)
elif formato == "3":
    save_as_docx(transcription)
else:
    print("❌ Formato non valido. Nessun file salvato.")
