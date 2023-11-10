"""
    main file that handles route
"""
from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
        emotion detector route
        route will be called once the button is clicked
    """
    query_string = request.args.get("textToAnalyze")
    received_dict = emotion_detector(query_string)
    if received_dict["dominant_emotion"] is not None:
        anger = received_dict["anger"]
        disgust = received_dict["disgust"]
        fear = received_dict["fear"]
        joy = received_dict["joy"]
        sadness = received_dict["sadness"]
        d_emotion = received_dict["dominant_emotion"]

        return f"For the given statement, the system response is\
        'anger': {anger}, 'disgust': {disgust}, 'fear': {fear},\
        'joy': {joy} and 'sadness': {sadness}. The dominant emotion is {d_emotion}."
    return "Invalid text! Please try again!."

@app.route("/")
def index():
    """fuction only renders one templates"""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
