import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Function to recognize speech
def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
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

# Function to open Chrome and search on YouTube
def search_youtube(query):
    options=webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  


    service = webdriver.ChromeService('../chromedriver-mac-arm64/chromedriver')  
    driver=webdriver.Chrome(service=service, options=options)
    driver.get("https://www.youtube.com/")
    search_box = driver.find_element_by_xpath("//input[@id='search']")
    search_box.send_keys(query)
    search_box.send_keys(Keys.RETURN)
    time.sleep(5) 
    driver.quit()

if __name__ == "__main__":
    while True:
        command = recognize_speech().lower()
        if "open chrome" in command:
            service = webdriver.ChromeService('../chromedriver-mac-arm64/chromedriver')  
            driver=webdriver.Chrome(service=service)
            driver.get("https://www.youtube.com/")
            time.sleep(3)
            driver.quit()
        elif "search youtube for" in command:
            query = command.replace("search youtube for", "").strip()
            search_youtube(query)
        elif "exit" in command:
            break
        else:
            print("Command not recognized")
