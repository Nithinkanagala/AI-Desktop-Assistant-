import text_speech
import datetime
import webbrowser
import weather

def respond_to_user(message):
    text_speech.text_to_speech(message)
    return message

def get_current_time():
    current_time = datetime.datetime.now()
    formatted_time = f"{current_time.hour} Hours {current_time.minute} Minutes"
    return respond_to_user(formatted_time)

def open_website(url, site_name):
    webbrowser.open(url)
    return respond_to_user(f'{site_name} is ready for you')

def actions(user_data):
    responses = {
        "what is your name": "My name is Bujji, developed by Venkat and team",
        "hello": "Hey, sir how can I help you?",
        "hey": "Hey, sir how can I help you?",
        "hi": "Hey, sir how can I help you?",
        "god": "Yes, my god is Venkat",
        "develope": "Team of Venkat developed me",
        "srustinchinavadu": "Nannu srustinchindhi Venkat devudu unnadu",
        "good morning": "Good morning sir"
    }

    # Simple response-based actions
    for trigger, response in responses.items():
        if trigger in user_data:
            return respond_to_user(response)

    # Time query
    if 'time now' in user_data:
        return get_current_time()

    # System shutdown
    if "shutdown" in user_data:
        respond_to_user('Okay sir')
        
        return 'Okay sir'

    # Website interactions
    if "music" in user_data:
        return open_website('https://open.spotify.com/', 'Spotify')

    if "youtube" in user_data:
        return open_website('https://www.youtube.com/', 'YouTube')

    if "google" in user_data:
        return open_website('https://www.google.com/', 'Google')
    
    if "food" in user_data:
        return open_website('https://www.zomato.com/hyderabad/delivery?dishv2_id=142242&category=1', 'food')
    
    # Weather update
    if "weather" in user_data:
        weather_info = weather.weather()
        return respond_to_user(weather_info)

    # Fallback response
    return respond_to_user('Can you please repeat?')

