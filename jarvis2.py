import speech_recognition as sr
import pyttsx3
import os
import subprocess as sp
import webbrowser
import subprocess
from playsound import playsound
#import vlc


#paths = {
    #'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",}

   #def open_notepad():
   # os.startfile(paths['notepad'])


# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Initialize the speech recognition engine
r = sr.Recognizer()

# Function to listen for audio and convert it to text
def listen():
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print(f"You said: {text}")
            return text
        except:
            #speak("Sorry, I didn't catch that. Can you repeat it?")
            return listen()

# Function to handle user requests
def handle_request(request):
    if "hello" in request.lower():
        speak("Hi Mr Gehan")
    if "who are you" in request.lower():
        speak("I am cmd")
    if "can i help me" in request.lower():
        speak("yes sir")
    if "how are you" in request.lower():
        speak("i am good. Mr Gehan")
    if "cmd" in request.lower():
        speak("yes sir. what can i do for you ")    
    if "fuck you" in request.lower():
        speak("My One")

    elif "open link" in request.lower():
        # Extract the link from the user's request
        link = request.split("open link", 1)[1].strip()
        speak(f"Opening {link}")
        webbrowser.open(link) 

    elif "open notepad" in request.lower():
        speak("Opening Notepad")
        subprocess.Popen(["notepad.exe"]) 

    elif "open vlc" in request.lower():
        speak("Opening vlc")
        subprocess.Popen(["vlc.exe"])           
  
    elif "open w" in request.lower():
        # Extract the website name from the user's request
        website_name = request.split("open w", 1)[1].strip()
        speak(f"Opening {website_name}")
        webbrowser.open(f"https://www.{website_name}.com")

    elif "play song" in request.lower():
        # Replace the song path with the path to your desired song
        speak("Playing song")
        playsound('your.mp3')
        subprocess.Popen(["start",  playsound], shell=True)

    elif "stop song" in request.lower():
        speak("Stopping song")
        for proc in psutil.process_iter():
            if proc.name() == "MusicPlayer.exe":
                proc.kill()
                break   

    elif "play video" in request.lower():
        # Replace the video URL with the URL of your desired video
        video_url = "https://www.youtube.com/watch?v=H7HT576s6uc"
        speak("Playing video")
        webbrowser.open(video_url)      

    elif "what time is it" in request.lower():
        speak("I don't know.")
    #else:
        #speak("Sorry, I don't understand. Can you please repeat?")

# Main function to run the assistant
def main():
    while True:
        request = listen()
        handle_request(request)

if __name__ == "__main__":
    main()
