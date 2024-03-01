import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('./harvard.wav')
moha = sr.AudioFile('./moha.wav')

# Increase Wthe duration for individuals with slower speech
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio1 = r.record(source, duration=60)

with moha as source:
    r.adjust_for_ambient_noise(source)
    audio2 = r.record(source, duration=10)  # Adjust duration as needed

# Adjust the language model and other parameters
try:
    transcription1 = r.recognize_google(audio1, language='en-US', show_all=True)
    print("Transcription 1: ", transcription1)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio 1")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service for audio 1; {0}".format(e))

# Recognize speech in audio2
try:
    transcription2 = r.recognize_google(audio2, language='en-US', show_all=True)
    print("Transcription 2: ", transcription2)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio 2")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service for audio 2; {0}".format(e))

# Example using the Sphinx recognizer
try:
    transcription_sphinx = r.recognize_sphinx(audio1)
    print("Sphinx Transcription: ", transcription_sphinx)
except sr.UnknownValueError:
    print("Sphinx could not understand audio 1")
except sr.RequestError as e:
    print("Could not request Sphinx results; {0}".format(e))

# Customization using a user-specific language model (not a direct implementation, requires additional steps)
# CustomModel = ...  # Load or train a custom language model
# try:
#     transcription_custom = r.recognize_custom(audio1, model=CustomModel)
#     print("Custom Transcription: ", transcription_custom)
# except CustomModelError as e:
#     print("Error in custom recognition; {0}".format(e))
    """_summary_
    
    
    """