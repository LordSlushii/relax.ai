import speech_recognition as sr
import openai
import pyttsx3

recognizer = sr.Recognizer()
openai.api_key = ""

def vTT():
    with sr.Microphone() as source:
        print("Start Speaking...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print("User:", text)
            return text;''
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

    

def ttAI(text):
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        max_tokens=100,
        messages = [
            {"role" : "user", "content" : text}
            ]
    )
    resp = response.choices[0].message.content.strip()
    print("Generating Response...")
    return resp

def tTS(text):
    global resp
    engine = pyttsx3.init()
    engine = pyttsx3.init()
    engine.setProperty('volume', 1.0)
    engine.setProperty('rate', 130)
    voices = engine.getProperty('voices')
    for voice in voices:
        if 'Zoe (Premium)' in voice.name:
            engine.setProperty('voice', voice.id)
            break
    engine.say(text)
    engine.runAndWait()

if __name__ == "__main__":
    
    tTS(ttAI(vTT()))

