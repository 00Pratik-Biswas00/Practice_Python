
import time
import speech_recognition as sr
from core import recognizer, tts, commands, config
from utils.logger import get_logger
logger = get_logger("Main")

logger.info("Starting Jarvis...")
if __name__ == "__main__":
    tts.speak("Hey Pratik, how can I help you?")

    while True:
        try:
            logger.info("Listening for wake word...")
            try:
                audio = recognizer.listen(timeout=config.LISTEN_TIMEOUT, phrase_time_limit=config.PHRASE_LIMIT)
                word = recognizer.recognize(audio)
                logger.info("Heard (wake):", word)
            except sr.UnknownValueError:
                logger.warning("Could not understand wake audio")
                continue
            except Exception as e:
                logger.warning("Wake recognition error:", e)
                continue

            if any(w in word.lower() for w in config.WAKE_WORDS):
                tts.speak("Yes Pratik")

                logger.info("Jarvis Active... (now listening for command)")
                try:
                    audio = recognizer.listen(timeout=config.LISTEN_TIMEOUT, phrase_time_limit=4)
                    command = recognizer.recognize(audio)
                    logger.info("Heard (command):", command)
                    commands.process_command(command)
                except sr.UnknownValueError:
                    logger.warning("Could not understand command.")
                    tts.speak("Sorry, I did not catch that.")
                except Exception as e:
                    logger.warning("Command recognition error:", e)
                    tts.speak("Something went wrong while understanding the command.")
            else:
                logger.warning("Wake word not detected.")

        except sr.WaitTimeoutError:
            logger.warning("Wake listening timed out — retrying.")
        except KeyboardInterrupt:
            logger.warning("Exiting.")
            break
        except sr.RequestError as e:
            logger.warning("Google API unavailable, error:", e)
            tts.speak("Sorry, I cannot reach Google right now.")
            continue
        except Exception as e:
            logger.warning("Unexpected error in loop:", e)
            time.sleep(0.5)
