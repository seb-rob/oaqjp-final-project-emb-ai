"""
    emotion detectector functions
"""
import requests
import json

def emotion_detector(text_to_analyse):
    """
        function sends requests to IBM Watson NLP library
        to get emotion out of text
    """
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyse } }

    try:
        response = requests.post(URL, json = input_json, headers = HEADERS)
        # Raise an error for bad responses (4xx or 5xx)
        # response.raise_for_status()
        r_json = json.loads(response.text)
        if response.status_code == 200:
            # Extract the 'emotion' dictionary
            emotion_predictions = r_json['emotionPredictions'][0]['emotion']
            # Find the dominant emotion
            dominant_emotion = max(emotion_predictions, key=emotion_predictions.get)
            emotions = {
                "anger": emotion_predictions["anger"],
                "disgust": emotion_predictions["disgust"],
                "fear": emotion_predictions["fear"],
                "joy": emotion_predictions["joy"],
                "sadness": emotion_predictions["sadness"],
                "dominant_emotion": dominant_emotion,
            }
        elif response.status_code == 400:
            emotions = {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "dominant_emotion": None,
            }
        return emotions
    except requests.exceptions.RequestException as e:
        # Handle network-related errors
        print(f"Error making the request: {e}")
        return {"error": "Network error"}
    except json.JSONDecodeError as e:
        # Handle JSON decoding errors
        print(f"Error decoding JSON: {e}")
        return {"error": "JSON decoding error"}
    except KeyError as e:
        # Handle missing keys in the JSON response
        print(f"Key not found in JSON: {e}")
        return {"error": "Key not found in JSON"}
