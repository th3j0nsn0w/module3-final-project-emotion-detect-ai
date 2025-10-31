
'''
Emotion detection application using the Watson NLP library.
'''

import json
import requests
import operator

def emotion_detector(text_to_analyze):
    '''
    Function to detect the emotion from a text.
    Returns the emotion with the highest probability.
    '''

    url = (
        'https://sn-watson-emotion.labs.skills.network/v1/'
        'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    )
    headers = { "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock" }
    json_input = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json = json_input, headers = headers, timeout=20)

    if response.status_code == 200:
        json_response = json.loads(response.text)
        emotion_predictions = json_response['emotionPredictions']
        if emotion_predictions:
            if len(emotion_predictions) == 1:
                emotion_components = emotion_predictions[0]['emotion']
                predominant_emotion = max(
                    emotion_components.items(), key=operator.itemgetter(1)
                )[0] # get the emotion with the highest probability

                emotion_components['dominant_emotion'] = predominant_emotion
                
                return emotion_components
            else:
                pass # TODO: What to do if there is more than one prediction?

    return {'emotion': None}
