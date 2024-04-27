import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pydub import AudioSegment
from gtts import gTTS
import os
import time

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"User said: {query}")
        return query
    except sr.UnknownValueError:
        print("Could not understand audio")
        return ""
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return ""

# Function to generate and play response
def respond(response_text):
    print(response_text)
    tts = gTTS(text=response_text, lang='en')
    tts.save('response.mp3')
    os.system('afplay response.mp3')

# Function to open Chrome and search on YouTube
def search_youtube(query):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument("--no-sandbox")  

    driver = webdriver.Chrome(service=ChromeService(), options=options)
    driver.get("https://www.youtube.com/")
    time.sleep(2)

    search_box = driver.find_element(by=By.XPATH, value="//input[@id='search']")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5) 
    # driver.quit()

def process_command(command):
    if "open chrome" in command:
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")  
        driver = webdriver.Chrome(service=ChromeService(), options=options)
        driver.get("https://www.youtube.com/")
        time.sleep(3)
        respond("Chrome opened successfully.")
    elif "search youtube for" in command:
        query = command.replace("search youtube for", "").strip()
        search_youtube(query)
        respond(f"Searching YouTube for {query}.")
    elif "exit" in command:
        respond("Exiting.")
        return False
    else:
        respond("Command not recognized")
    return True

if __name__ == "__main__":
    while True:
        command = recognize_speech().lower()
        if "hey" in command and "blank" in command:
            respond("How can I assist you?")
            while True:
                next_command = recognize_speech().lower()
                if next_command and not process_command(next_command):
                    break
        elif "exit" in command:
            break
        else:
            print("Command not recognized")
