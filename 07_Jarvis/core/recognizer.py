import speech_recognition as sr
from core import config


recognizer = sr.Recognizer()

def listen(timeout=config.LISTEN_TIMEOUT, phrase_time_limit=config.PHRASE_LIMIT):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
    return audio

def recognize(audio):
    return recognizer.recognize_google(audio)
