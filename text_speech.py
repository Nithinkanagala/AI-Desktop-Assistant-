import pyttsx3

# Initialize the engine once
engine = pyttsx3.init()
voices = engine.getProperty('voices')

def text_to_speech(text, gender='female'):
    # Set voice based on gender
    if gender == 'female':
        engine.setProperty('voice', voices[1].id)  # Female voice
    else:
        engine.setProperty('voice', voices[0].id)  # Male voice
    
    engine.say(text)
    engine.runAndWait()
