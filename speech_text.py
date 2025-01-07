import speech_recognition as sr

def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        try:
            audio = recognizer.listen(source)
            # Recognizing the audio using Google Web Speech API
            voice = recognizer.recognize_google(audio)
            print(f"You said: {voice}")
            return voice
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
            return "Sorry, I couldn't understand what you said."
        except sr.RequestError:
            print("Sorry, there was a problem with the recognition service.")
            return "Sorry, there was a problem with the recognition service."

# speech_to_text()
