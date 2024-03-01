### README.md - Speech Recognition with Python

#### Overview

This Python script demonstrates the usage of the SpeechRecognition library to transcribe audio files using Google Speech Recognition and PocketSphinx. The script provides examples for transcribing two audio files, `harvard.wav` and `moha.wav`, using different recognition engines.

#### Instructions

1. **Installation**

   Ensure that you have the `speech_recognition` library installed:
   ```bash
   pip install SpeechRecognition
   ```

2. **Audio Files**

   Make sure you have the audio files, `harvard.wav` and `moha.wav`, in the same directory as the script.

3. **Adjusting Duration**

   The script transcribes `harvard.wav` for up to 60 seconds and `moha.wav` for up to 10 seconds. Adjust these durations based on your audio files.

4. **Running the Script**

   Execute the script in a Python environment:
   ```bash
   python script_name.py
   ```

#### Code Explanation

```python
import speech_recognition as sr

# Initialize the Recognizer
r = sr.Recognizer()

# Load audio files
harvard = sr.AudioFile('./harvard.wav')
moha = sr.AudioFile('./moha.wav')

# Adjust for ambient noise and record audio
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio1 = r.record(source, duration=60)

with moha as source:
    r.adjust_for_ambient_noise(source)
    audio2 = r.record(source, duration=10)

# Transcribe using Google Speech Recognition
try:
    transcription1 = r.recognize_google(audio1, language='en-US', show_all=True)
    print("Transcription 1: ", transcription1)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio 1")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service for audio 1; {0}".format(e))

# Transcribe second audio file
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
```

#### Notes

- Adjust the durations according to the length of your audio files.
- Ensure proper dependencies for Google Speech Recognition and Sphinx.
- Follow additional steps if using a custom language model.

Feel free to reach out if you have any questions or need further assistance!
# en español
## Reconocimiento de voz con Python y Python Speech Library (PySpeech)
### README.md - Reconocimiento de Voz con Python

#### Descripción General

Este script en Python demuestra el uso de la biblioteca SpeechRecognition para transcribir archivos de audio utilizando el reconocimiento de voz de Google y PocketSphinx. El script proporciona ejemplos para transcribir dos archivos de audio, `harvard.wav` y `moha.wav`, utilizando diferentes motores de reconocimiento.

#### Instrucciones

1. **Instalación**

   Asegúrese de tener instalada la biblioteca `speech_recognition`:
   ```bash
   pip install SpeechRecognition
   ```

2. **Archivos de Audio**

   Asegúrese de tener los archivos de audio, `harvard.wav` y `moha.wav`, en el mismo directorio que el script.

3. **Ajuste de Duración**

   El script transcribe `harvard.wav` hasta 60 segundos y `moha.wav` hasta 10 segundos. Ajuste estas duraciones según sus archivos de audio.

4. **Ejecutar el Script**

   Ejecute el script en un entorno de Python:
   ```bash
   python nombre_del_script.py
   ```

#### Explicación del Código

```python
import speech_recognition as sr

# Inicializar el Reconocedor
r = sr.Recognizer()

# Cargar archivos de audio
harvard = sr.AudioFile('./harvard.wav')
moha = sr.AudioFile('./moha.wav')

# Ajustar para el ruido ambiental y grabar audio
with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio1 = r.record(source, duration=60)

with moha as source:
    r.adjust_for_ambient_noise(source)
    audio2 = r.record(source, duration=10)

# Transcribir usando Google Speech Recognition
try:
    transcription1 = r.recognize_google(audio1, language='es-ES', show_all=True)
    print("Transcripción 1: ", transcription1)
except sr.UnknownValueError:
    print("Google Speech Recognition no pudo entender el audio 1")
except sr.RequestError as e:
    print("No se pudieron solicitar resultados del servicio de reconocimiento de voz de Google para el audio 1; {0}".format(e))

# Transcribir el segundo archivo de audio
try:
    transcription2 = r.recognize_google(audio2, language='es-ES', show_all=True)
    print("Transcripción 2: ", transcription2)
except sr.UnknownValueError:
    print("Google Speech Recognition no pudo entender el audio 2")
except sr.RequestError as e:
    print("No se pudieron solicitar resultados del servicio de reconocimiento de voz de Google para el audio 2; {0}".format(e))

# Ejemplo utilizando el reconocedor Sphinx
try:
    transcription_sphinx = r.recognize_sphinx(audio1, language='es-ES')
    print("Transcripción Sphinx: ", transcription_sphinx)
except sr.UnknownValueError:
    print("Sphinx no pudo entender el audio 1")
except sr.RequestError as e:
    print("No se pudieron solicitar resultados de Sphinx; {0}".format(e))

# Personalización utilizando un modelo de lenguaje específico del usuario (no es una implementación directa, requiere pasos adicionales)
# ModeloPersonalizado = ...  # Cargar o entrenar un modelo de lenguaje personalizado
# try:
#     transcription_custom = r.recognize_custom(audio1, model=ModeloPersonalizado)
#     print("Transcripción Personalizada: ", transcription_custom)
# except CustomModelError as e:
#     print("Error en el reconocimiento personalizado; {0}".format(e))
```

#### Notas

- Ajuste las duraciones de acuerdo con la longitud de sus archivos de audio.
- Asegúrese de tener las dependencias adecuadas para el reconocimiento de voz de Google y Sphinx.
- Siga los pasos adicionales si usa un modelo de lenguaje personalizado.

¡No dude en contactarnos si tiene alguna pregunta o necesita más ayuda!
en mi opinion
<s>Esto es una opinión
  los comunicación son importantes 
  la url es [https://realpython.com/python-speech-recognition/](https://realpython.com/python-speech-recognition/)</
  pero también es importante ser capaz de escuchar pero saca.py no funcion 

```python
import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('./harvard.wav')
moha = sr.AudioFile('./moha.wav')

with harvard as source:
    r.adjust_for_ambient_noise(source)
    audio1 = r.record(source, duration=40)

with moha as source:
    r.adjust_for_ambient_noise(source)
    audio2 = r.record(source, duration=4)

# r.recognize_google(audio1)

print(r.recognize_google(audio1))
print(r.recognize_google(audio2))

# audio2 = r.record(source, duration=4)


```

Explaination
This script uses the `speech_recognition` library to record and recognize audio files in
different languages using Google's Speech Recognition API. The `duration` parameter is the duration of the recognition

in my opinionm is the same as the `duration` parameter of the `sr.listen()` function. It is true  that this value can be adjusted according to the different languages using Google's Speech Rec
English and Arabic. The `duration` parameter is used to set the length of each recording.

explicación
Este script utiliza la biblioteca `speech_recognition` para grabar y reconocer archivos de audio en
diferentes idiomas utilizando la API de reconocimiento de voz de Google. El parámetro `duración` es la duración del reconocimiento.

en mi opinión es lo mismo que el parámetro `duración` de la función `sr.listen()`. Es cierto que este valor se puede ajustar a los diferentes idiomas mediante Speech Rec de Google.
Inglés y Árabe. El parámetro "duración" se utiliza para establecer la duración de cada grabación.