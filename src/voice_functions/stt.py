def stt(filename):
  try: 
    import speech_recognition as sr
  except:
    import os
    os.system("pip install SpeechRecognition")
    import speech_recognition as sr

  r = sr.Recognizer()
  audiofile = sr.AudioFile(filename)
  with audiofile as source:
    audio = r.record(source)
  return(r.recognize_google(audio))