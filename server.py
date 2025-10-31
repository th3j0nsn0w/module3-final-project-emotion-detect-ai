'''
Server using Flask.
'''

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def detect_emotion():
    '''
    Process text to detect the dominant emotion
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    if text_to_analyze:
        emotion_info = emotion_detector(text_to_analyze)
        if emotion_info and emotion_info['dominant_emotion']:
            emotion_response = (
                f"For the given statement, the system response is 'anger': "
                f"{ emotion_info['anger'] }, 'disgust': { emotion_info['disgust'] }, 'fear': "
                f"{ emotion_info['fear'] }, 'joy': { emotion_info['joy'] } and 'sadness': "
                f"{ emotion_info['sadness'] }. The dominant emotion is "
                f"{ emotion_info['dominant_emotion'] }."
            )

            return emotion_response

    return "Invalid text! Please try again!."

@app.route("/")
def render_index_page():
    '''
    Render main application page
    '''

    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
