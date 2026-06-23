import speech_recognition as sr

# Create recognizer
r = sr.Recognizer()

# Read audio file
with sr.AudioFile("audio.wav.wav") as source:
    audio = r.record(source)

# Convert speech to text
text = r.recognize_google(audio)

print("Transcription:")
print(text)