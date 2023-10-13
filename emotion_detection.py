"""The function takes a string as input and returns a list of emotions as strings."""

import requests

def emotion_detector(text_to_analyze):
  """The function takes a string as input and returns a list of emotions as strings."""

  url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
  myobj = {
    "raw_document": {
      "text": text_to_analyze
    }
  }
  header = {
    "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
  }
  response = requests.post(url, json=myobj, headers=header, timeout=10)

  return response.text
