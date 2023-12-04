import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('./harvard.wav')
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio1 = r.record(source, duration=4)

# r.recognize_google(audio1)

print(r.recognize_google(audio1))

# audio2 = r.record(source, duration=4)

