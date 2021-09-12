def transcribe_gcs(gcs_uri):
    from google.cloud import speech
#    from google.cloud.speech import enums
#    from google.cloud.speech import types

    client = speech.SpeechClient()
    audio = speech.RecognitionAudio(uri=gcs_uri)
    config = speech.RecognitionConfig(
    encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=8000,
        language_code='en-US')

    operation = client.long_running_recognize(config=config, audio=audio)
    response = operation.result()

    return response

response = transcribe_gcs("gs://tuv_0907/TUV_0907_mono_8000.wav")

with open("speech3.txt", "w") as script:
    for result in response.results:
        script.write(u'{}'.format(result.alternatives[0].transcript)+"\n")

print("completed")