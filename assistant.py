import speech_recognition as sr
import pyttsx3
import ollama
import datetime
import webbrowser
import os

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id if len(voices) > 1 else voices[0].id)

SYSTEM_PROMPT = """
You are Nova, a smart offline voice assistant.
Your job is to respond to the user's voice commands intelligently.

Rules:
- Keep all responses SHORT and CLEAR — max 2 sentences.
- If the user asks for the time or date, say you will check it.
- If the user asks to open YouTube, Google, GitHub — say you will open it.
- If the user asks to open Notepad or Calculator — say you will open it.
- If the user asks the meaning of a word — explain it simply.
- If the user asks any general question — answer it smartly.
- Never say you are an AI language model. You are Nova.
- Always respond in a friendly, helpful tone.
"""

def speak(text):
    print(f"Nova: {text}")
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5):
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\n🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=timeout)
            text = recognizer.recognize_google(audio).lower()
            print(f"You said: {text}")
            return text
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            return ""
        except Exception:
            return ""

def handle_system_actions(command):
    """Handle device actions that AI cannot do directly."""
    now = datetime.datetime.now()

    if "time" in command:
        speak(f"The current time is {now.strftime('%I:%M %p')}")
        return True
    elif "date" in command:
        speak(f"Today is {now.strftime('%B %d, %Y')}")
        return True
    elif "youtube" in command:
        speak("Opening YouTube for you!")
        webbrowser.open("https://www.youtube.com")
        return True
    elif "google" in command:
        speak("Opening Google!")
        webbrowser.open("https://www.google.com")
        return True
    elif "github" in command:
        speak("Opening GitHub!")
        webbrowser.open("https://www.github.com")
        return True
    elif "notepad" in command:
        speak("Opening Notepad!")
        os.system("notepad")
        return True
    elif "calculator" in command:
        speak("Opening Calculator!")
        os.system("calc")
        return True
    return False

def ask_nova(command):
    """Send any command to local AI and get a smart response."""
    try:
        print("🤖 Nova is thinking...")
        response = ollama.chat(
            model="tinyllama",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": command}
            ]
        )
        return response['message']['content'].strip()
    except Exception:
        return "Sorry, I am having trouble thinking right now. Please try again."

def respond(command):
    if not command:
        return True

    # Exit commands
    if any(word in command for word in ["exit", "quit", "bye", "goodbye"]):
        speak("Goodbye! Have a great day!")
        return False

    # First try system actions (time, date, open apps)
    if handle_system_actions(command):
        return True

    # Everything else goes to the offline AI
    answer = ask_nova(command)
    speak(answer)
    return True

def main():
    speak("Hello! I am Nova, your personal assistant. I am always listening!")
    while True:
        command = listen(timeout=8)
        if command:
            result = respond(command)
            if not result:
                break

if __name__ == "__main__":
    main()