# 🎧 Audio Transcription Tool
Use this code on google colab to transcribe your audio for free with whisper openAI open source model

It transcribes audio files directly from your computer and allows you to:
	•	✅ See real-time transcription with progress percentage.
	•	🌍 Transcribe in the top 10 most spoken languages in the world.
	•	📄 Export the transcription to TXT, PDF, or Word (.docx) formats.


⚙️ 1. Open Google Colab
Go to Google Colab and create a new notebook.

⚡️ 2. Enable GPU Runtime
For better performance (especially with large audio files):
	1.	Click on Runtime > Change runtime type
	2.	Set Hardware accelerator to GPU
	3.	Make sure the GPU is a T4

📥 3. Copy and Paste the Code
Copy the entire script from the notebook or source and paste it into a single cell in your Google Colab notebook.

🔧 4. Run the Cell
Run the cell by clicking ▶️ or pressing Shift + Enter.

📁 5. Upload Your Audio File
After executing the code:
	•	A file upload window will appear.
	•	Choose the audio file you want to transcribe.
	•	Supported formats include .mp3, .wav, .m4a, etc.

 🌐 6. Select the Transcription Language
You’ll be asked to choose the language of the audio.
	•	Examples:
 'it' for italian
 'en' for english
 'es' for spanish

 📢 Disclaimer
	•	The Whisper model can process large audio files, but GPU is highly recommended.
	•	The T4 GPU available in Colab ensures significantly faster transcription time.
	•	Performance may vary depending on internet speed and audio file length.

 👨‍💻 Credits
	•	Built using Whisper by OpenAI
	•	Designed for educational and productivity purposes
