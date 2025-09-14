from utils.logger import get_logger
import pyttsx3

logger = get_logger(__name__)

def speak(text: str):
    try:
        logger.info(f"TTS speaking: {text}")
        engine = pyttsx3.init()
        engine.setProperty('volume', 1.0)
        engine.say(text)
        engine.runAndWait()
        engine.stop()
        logger.debug("TTS finished speaking")
    except Exception as e:
        logger.error(f"TTS error: {e}")
