import speech_recognition as sr
from ibm_watson import SpeechToTextV1
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Text to Speech service credentials
stt_api = 'YOUR_API_KEY'
stt_url = 'YOUR_URL'

# Speech to Text service credentials
tts_api = 'YOUR_API_KEY'
tts_url = 'YOUR_URL'

r = sr.Recognizer()
speech = sr.Microphone()
stt_authenticator = IAMAuthenticator(stt_api)
speech_to_text = SpeechToTextV1(authenticator=stt_authenticator)
speech_to_text.set_service_url(stt_url)

with speech as source:
    print("Say Something!\n")
    audio_file = r.adjust_for_ambient_noise(source)
    audio_file = r.listen(source)
    data = speech_to_text.recognize(audio=audio_file.get_wav_data(), content_type='audio/wav').get_result()
speech_recognition_results = data['results'][0]['alternatives'][0]['transcript']
print("IBM Watson thinks you said: \n" + speech_recognition_results)

# save STT as txt file
with open('result.txt', mode='w') as file:
    file.write(speech_recognition_results)
print("\nYour speech has been exported to result.txt")

# Insert API Key in place of
# 'YOUR UNIQUE API KEY'
tts_authenticator = IAMAuthenticator(tts_api)
tts = TextToSpeechV1(authenticator=tts_authenticator)

# Insert URL in place of 'API_URL'
tts.set_service_url(tts_url)

# recognize text using IBM Text to Speech
# save TTS as mp3 file

f = open("result.txt", "r")
text = f.read()
with open('./speech.mp3', 'wb') as audio_file:
    res = tts.synthesize(text, accept='audio/mp3', voice='en-GB_KateV3Voice').get_result()
    audio_file.write(res.content)  # write the content to the audio file
print("Your text has been converted to speech and saved as mp3 file successfully")
