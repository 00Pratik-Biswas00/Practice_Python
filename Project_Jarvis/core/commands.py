import webbrowser
from core.tts import speak
from data import music_library
from core.ai_process import aiProcess

def process_command(command: str):
    cmd = command.lower()
    if "open google" in cmd:
        webbrowser.open("https://google.com")
    elif "open facebook" in cmd:
        webbrowser.open("https://facebook.com")
    elif "open youtube" in cmd:
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in cmd:
        webbrowser.open("https://linkedin.com")
    elif cmd.startswith("play"):
        parts = cmd.split()
        if len(parts) >= 2:
            song = " ".join(parts[1:])  # join words into one string
            link = music_library.music.get(song)
            if link:
                webbrowser.open(link)
            else:
                speak(f"I don't have {song} in library.")
        else:
            speak("Please tell me which song to play.")
    
    else:
        output = aiProcess(cmd)
        speak(output)

