

````markdown
# 🎙️ Nova — Offline AI Voice Assistant

Nova is a fully offline AI voice assistant built with Python. It listens to your voice, understands natural language using a local AI model, and responds out loud — without requiring an internet connection.

---

## 🚀 Why This Project

Most voice assistants rely on cloud APIs, which leads to:
- Privacy concerns  
- Internet dependency  
- Slower response times  

Nova runs completely offline using local models, making it faster, private, and reliable.

---

## ✨ Features

- 🎙️ Always listening — no wake word required  
- 🤖 Offline AI brain using TinyLlama  
- 🔊 Voice response using text-to-speech  
- 🌐 Opens websites (YouTube, Google, GitHub)  
- 💻 Opens applications (Notepad, Calculator)  
- 🕐 Provides time and date  
- 📖 Explains words and concepts  
- 😄 Answers general questions  

---

## 🏗️ How It Works

Voice Input → SpeechRecognition → TinyLlama (via Ollama) → pyttsx3 → Voice Output

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|--------|
| Python 3.9 | Core programming |
| SpeechRecognition | Voice to text |
| pyttsx3 | Text to speech |
| Ollama | Run local AI model |
| TinyLlama | Language model |
| webbrowser | Open websites |
| datetime | Time and date |

---

## ⚙️ Installation

### 1. Clone the Repository
```bash
git clone https://github.com/WhiteHorse2209/voice-assistant-python.git
cd voice-assistant-python
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Ollama

Download from: [https://ollama.com](https://ollama.com)

### 4. Download TinyLlama Model

```bash
ollama run tinyllama
```

(Wait for download, then press Ctrl + D)

### 5. Run the Assistant

```bash
python assistant.py
```

---

## 🗣️ Usage

Just run the assistant and speak naturally.

### Example Commands:

* "What time is it?"
* "Open YouTube"
* "Explain artificial intelligence"
* "Open calculator"
* "Tell me a joke"
* "Goodbye"

---

## 📂 Project Structure

```
voice-assistant-python/
├── assistant.py
├── requirements.txt
└── README.md
```

---

## ⚠️ Limitations

* Accuracy depends on TinyLlama (not as powerful as cloud AI)
* No wake word may cause unintended activation
* Continuous listening may use more CPU
* Limited system-level controls

---

## 🔧 Improvements You Can Add

* Add wake word detection (Porcupine / Snowboy)
* Add GUI for better interaction
* Add memory for conversations
* Add custom commands or plugins

---

## 📈 Future Scope

* Wake-word activation
* Context-aware responses
* More app integrations
* Better local AI models

---

## 👨‍💻 Author

WhiteHorse2209
[https://github.com/WhiteHorse2209](https://github.com/WhiteHorse2209)
