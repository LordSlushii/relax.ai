import openai
import pyttsx3

openai.api_key = ""

prompt = f"i am a write a story about a random topic in about 100 words"
def con_ai(prompt):
    global resp
    response = openai.chat.completions.create(
        model = "gpt-3.5-turbo",
        messages = [
            {"role" : "user", "content" : prompt}
            ]
    )


    resp = response.choices[0].message.content.strip()
    print(resp)
        
    
def text_to_speech(text):
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
    con_ai(prompt)
    text_to_speech(resp)

