import requests
import json

def emotion_detector(text_to_analyse):
    """ This function uses watson NLP library to detect emotions in strings """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyse } }
    response = requests.post(url, json = myobj, headers = headers)
    formatedResponse = json.loads(response.text)
    emotions = formatedResponse["emotionPredictions"][0]["emotion"]
    dominantEmotion = ''
    dominantScore = 0
    for key, value in emotions.items():
        if value > dominantScore:
            dominantScore = value
            dominantEmotion = key
    emotions["dominant_emotion"] = dominantEmotion
    return emotions

