"""
    Emotion detection test
"""
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    #unittest class for emotion detection
    def test_emotion_detector(self):
        #function will run against emotion_detector function
        request_one = emotion_detector("I am glad this happened")
        self.assertEqual(request_one["dominant_emotion"], "joy")

        request_two = emotion_detector("I am really mad about this")
        self.assertEqual(request_two["dominant_emotion"], "anger")

        request_three = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(request_three["dominant_emotion"], "disgust")

        request_four = emotion_detector("I am so sad about this")
        self.assertEqual(request_four["dominant_emotion"], "sadness")

        request_five = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(request_five["dominant_emotion"], "fear")

if __name__ == "__main__":
    unittest.main()