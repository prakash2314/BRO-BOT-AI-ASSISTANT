import pyttsx3
import speech_recognition as sr
import keyboard
import os
import imdb
import time
import pyautogui
import webbrowser
import subprocess as sp
from decouple import config
import wolframalpha
from datetime import datetime
from selenium import webdriver
from online import find_my_ip,search_on_google,search_on_wikipedia,youtube,weather_forecast

import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    raise ValueError("API key not found! Set the GOOGLE_API_KEY environment variable.")

# Configure Google AI Client
genai.configure(api_key=API_KEY)

import time

def generate_ai_essay():
    model = genai.GenerativeModel("gemini-2.0-flash")

    while True:  # Keep listening for new queries
        try:
            query = take_command()
            if query.lower() in ["exit", "quit", "stop"]:  # Exit condition
                print("Exiting...")
                speak("Goodbye!")
                break  

            if not query or query == "None":  
                continue  # If no input, continue listening

            response = model.generate_content(query)
            full_response = response.text

            # Summarizing response
            summary_prompt = f"Summarize this in 2-3 sentences: {full_response}"
            summary = model.generate_content(summary_prompt).text  

            print(summary)
            speak(summary)

            time.sleep(1)  # Pause before the next command

        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, something went wrong.")
            time.sleep(2)  # Pause to prevent crashing






APP_ID = config("WOLFRAM_APP_ID")
client = wolframalpha.Client(APP_ID)

engine = pyttsx3.init('sapi5')
engine.setProperty('volume',1.5)
voice =engine.getProperty('voices')
engine.setProperty('voice', voice[0].id)

USER =config('USER')
HOSTNAME =config('BOT')











def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if (hour>=6) and (hour < 12):
        speak(f"Good Morning {USER}")
    elif (hour >=12) and (hour <=16):
        speak(f"Good afternoon {USER}")
    elif(hour>=16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you? {USER}")

listening= False








def start_listening():
    global listening
    listening=True
    print("Started Listening")

def pause_listening():
    global listening
    listening=False
    print("Stopped Listening")

keyboard.add_hotkey('ctrl+alt+k',start_listening)
keyboard.add_hotkey('ctrl+alt+p',pause_listening)








def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=5)
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except sr.WaitTimeoutError:
            print("Timeout: No speech detected!")
            return "None"
        except sr.UnknownValueError:
            print("Could not understand audio")
            return "None"
        except sr.RequestError:
            print("Speech Recognition service error")
            return "None"
        





        


def send_whatsapp_message():
    """Automates sending a WhatsApp message"""
    speak("that's cool bro...")
    speak("Opening WhatsApp Web for messaging")
    webbrowser.open("https://web.whatsapp.com/")
    time.sleep(10)  # Wait for WhatsApp to load

    speak("Whom do you want to send a message bro?")
    recipient = take_command()
    speak(f"Searching for {recipient} in WhatsApp")

    # Click search box (use dynamic positioning if needed)
    search_box = (309, 257)  # Adjust based on screen resolution
    pyautogui.moveTo(*search_box, duration=1)
    pyautogui.click()
    pyautogui.typewrite(recipient, interval=0.1)
    time.sleep(2)  # Wait for results

    # Select the first contact (assuming it's correct)
    contact_position = (308, 513)  # Adjust this for your screen
    pyautogui.moveTo(*contact_position, duration=1)
    pyautogui.click()

    speak("bro,,.Tell the message to send")
    message = take_command()

    speak(f"Sending the message: {message}. Should I proceed?")
    msg_box_position = (1098, 964)  # Adjust as per screen
    pyautogui.moveTo(*msg_box_position, duration=1)
    pyautogui.click()
    pyautogui.typewrite(message, interval=0.1)
    pyautogui.press("enter")
    speak(" bro Message sent successfully")
    

# Example usage inside main program
query = take_command()
       
if __name__ =='__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("Yes BRO iam fine.... What about you")
                
            elif "i am fine" in query:
                speak("That's cool BRO......")
            elif "schedule" in query:
                speak("BRO today you have a project presentation....... and its about me .  so be prepared. and do well ")
            
            elif "do my best" in query:
                speak("That's cool bro......     you are really awsome ")
                
                  
            elif "open ai" in query:
                speak("yes bro iam working on it")
                speak("NOW its turned on to open ai...... ask anything you want")
                generate_ai_essay()
                      
            
            elif "command prompt" in query:
                speak("yes bro")
                speak("Opening command prompt")
                sp.Popen("start cmd", shell=True)

            elif "chrome" in query:
                speak("Opening chrome")
                sp.Popen("start chrome",shell=True)

            elif "ip address" in query:
                ip_address= find_my_ip()
                speak(f"Your ip address is {ip_address}")
                print(f"Your IP Address is {ip_address}")

            elif "open youtube" in query:
                print("what do you want me to play on youtube BRO?")
                speak("what do you want me to play on youtube BRO?")
                video=take_command().lower()
                youtube(video)

            
            elif "close youtube" in query:
                speak("yes bro......closing youtube")
                pyautogui.hotkey("ctrl", "w")


            elif "love" in query:
                print("yes bro i play the beautiful song for your loved one 😍🤗")
                speak("yes bro i play the beautiful song for your loved one ")
                time.sleep(2)
                webbrowser.open("https://www.youtube.com/watch?v=cNGjD0VG4R8")

            elif "google" in query:
                speak(f"what do you want me to search on google bro")
                query=take_command().lower()
                search_on_google(query)

            elif "wikipedia" in query:
                speak("what do you want me to search on wikipedia sir?")
                search=take_command().lower()
                result=search_on_wikipedia(search)
                speak(f"Accrding to wikipedia,{result}")
                speak(f"Iam printing it on Terminal {USER}")
                print(result)
                                   
            elif "open facebook" in query:
                speak(" yes bro .....opening facebook ")
                driver= webdriver.Chrome()
                driver.get("http://www.facebook.com/")
                
            elif "open instagram" in query:
                speak("opeing instagram reels.......enjoy the reels bro")
                webbrowser.open("https://www.instagram.com/reels/")
                time.sleep(5)
                speak("now give the command unmute")
                order=take_command()
                if "now unmute" or "unmute" in order:
                    pyautogui.moveTo(1276, 216, 1)
                    pyautogui.click(x=1276, y=216)
                    time.sleep(6)
                    speak("Now I will scroll the reels")
                    for _ in range(5):  # Scroll through 5 reels
                        pyautogui.press("down")  # Moves to the next reel
                        time.sleep(6)

                    pyautogui.moveTo(1276, 216, 1)
                    pyautogui.click(x=1276, y=216)
                

            
            elif "open whatsapp" in query:
                speak("opening whatsapp for you bro")
                driver= webdriver.Chrome()
                driver.get("http://www.whatsapp.com/")


            elif "whatsapp message" in query:
                send_whatsapp_message()



            elif "close message" in query:
                speak("ok bro as your wish .......closing whatapp message")
                pyautogui.hotkey("ctrl", "w")
    
            elif "college" in query:
                speak("opening Dr.Mgr university website")
                webbrowser.open("https://www.drmgrdu.ac.in/")   

            elif "close facebook" in query:
                speak("closing facebook")
                driver.close()  
                
            elif "close instagram" in query:
                speak("yes bro......closing instagram")
                pyautogui.hotkey("ctrl", "w")
            
            elif "close whatsapp" in query:
                speak("closing whatsapp")
                driver.close()     
  
            elif "increase the volume" in query:
                pyautogui.press("volumeup")
                speak("volume increased")
                               
            elif "decrease the volume" in query:
                pyautogui.press("volumedown")
                speak("volume decreased")
                   
            elif "mute" in query:
                pyautogui.press("volumemute") 
                speak("volume muted")
                
            elif "weather" in query:
                ip_address=find_my_ip()
                speak("bro tell me the name of your city ")
                speak("so that i can tell the current temperature")
                city=take_command()
                speak(f"Getting weather report for the city{city}")
                weather ,temp, feels_like = weather_forecast(city)
                speak(f"The current temperature is {temp},but it feels like{feels_like}")
                speak(f"Also, the weather report talks about{weather}")
                speak(f"For your convenience, I am printing it on the screen sir.")
                print(f"Description:{weather}\nTemperature: {temp}\nFeels like:{feels_like} ")

            elif "imdb" in query:
                movies_db = imdb.IMDb()
                speak("Please tell me the movie name: ")
                text = take_command()
                movies = movies_db.search_movie(text)
                if not movies:
                    speak("Sorry, I couldn't find any movie with that name.")
                else:
                    speak(f"Searching for {text}")
                    speak("I found this movie:")
                    movie = movies[0]  # Take the first matching movie
                    title = movie["title"]
                    year = movie.get("year", "Unknown Year")
                    speak(f"{title} - {year}")
                    
                    info = movie.getID()
                    movie_info = movies_db.get_movie(info)
                    
                    rating = movie_info.get('rating', 'N/A')
                    cast = movie_info.get('cast', [])  # Get cast safely
                    actor = cast[:5] if cast else "No cast information available"
                    plot = movie_info.get('plot outline', 'Plot summary not available')
                    speak(f"{title} was released in {year} and has an IMDb rating of {rating}. "
                          f"The plot summary of the movie is: {plot}")
                    print(f"{title} was released in {year} and has an IMDb rating of {rating}. "
                          f"It has a cast of {actor}. The plot summary of the movie is: {plot}")

            elif "calculate" in query:
                try:
                    ind = query.lower().split().index("calculate")
                    text = query.split()[ind + 1:]
                    result = client.query(" ".join(text))
                    ans = next(result.results).text
                    speak("The answer is " + ans)
                    print("The answer is " + ans)
                except (StopIteration, IndexError):
                    speak("I couldn't find that. Please try again") 

            elif any(x in query for x in ["what is", "who is", "which is"]):
                try:
                    result = client.query(query)
                    ans = next(result.results).text
                    speak("The answer is " + ans)
                except StopIteration:
                   speak("I couldn't find that. Please try again")

            elif "subscribe" in query:
                speak("yes sir . what channel do you want to subscribe")
                channel=take_command()
                channel += " channel"
                speak("Firstly go to youtube")
                webbrowser.open("https://www.youtube.com/")
                time.sleep(4)
                speak("wait bro the browser needs to load properly")
                speak("click on the search bar")
                pyautogui.moveTo(741, 178, 1)
                pyautogui.click(x=741, y=178, clicks=1, interval=0, button='left')
                speak(channel)
                pyautogui. typewrite(channel, 0.1)
                time.sleep(1)
                speak("press enter")
                pyautogui.press('enter')
                pyautogui.moveTo(1750, 382, 1)
                speak(f"Here you will see{channel}")
                speak(f"Click here to subscribe{channel}")
                pyautogui.click(x=1750, y=382, clicks=2, interval=0, button='left')
                speak("And also Don't forget to press the bell icon")
                pyautogui.moveTo(1724, 454, 1)
                pyautogui.click(x=1724, y=454, clicks=1, interval=0, button='left')
                speak("turn on all notifications")
                pyautogui.click(x=1724, y=454, clicks=1, interval=0, button='left')           

            elif "stop" in query or "exit" in query or "quit" in query:
                speak("okay, stopping now. call me if iam needed!")
                print("Exiting....")
                break


  



