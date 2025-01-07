from requests_html import HTMLSession

def weather(location="Ghatkesar"):
    # Initialize HTML session
    session = HTMLSession()

    # Query for weather, location passed as argument
    url = f"https://www.google.com/search?q=weather+{location}"

    # Headers to mimic a real browser
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    }

    try:
        # Fetch the page with headers
        response = session.get(url, headers=headers)
        
        # Check for successful request
        if response.status_code == 200:
            # Extract the temperature
            temp = response.html.find('span#wob_tm', first=True)
            if temp:
                return f"Temperature in {location} is {temp.text}°C"
            else:
                return "Could not find the temperature data."
        else:
            return f"Failed to retrieve data. Status code: {response.status_code}"

    except Exception as e:
        return f"An error occurred: {e}"
    
    finally:
        # Always close the session
        session.close()

# Example usage
# print(weather("Ghatkesar"))
