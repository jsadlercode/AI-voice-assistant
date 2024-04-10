import speech_recognition as sr

r = sr.Recognizer()
with sr.Microphone() as source:
    print("I'm listening...")
    audio = r.listen(source)

try:
    print("I think you said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("I didn't quite get that...")
except sr.RequestError as e:
    print("Sphinx error: {0}".format(e))