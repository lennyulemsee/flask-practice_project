import unittest
from EmotionDetector.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):
        data = emotion_detector("I am glad this happened")
        dom_emotion = data["dominant_emotion"]
        self.assertEqual(dom_emotion, "joy")
        data = emotion_detector("I am really mad about this")
        dom_emotion = data["dominant_emotion"]
        self.assertEqual(dom_emotion, "anger")
        data = emotion_detector("I feel disgusted just hearing about this")
        dom_emotion = data["dominant_emotion"]
        self.assertEqual(dom_emotion, "disgust")
        data = emotion_detector("I am so sad about this")
        dom_emotion = data["dominant_emotion"]
        self.assertEqual(dom_emotion, "sadness")
        data = emotion_detector("I am really afraid that this will happen")
        dom_emotion = data["dominant_emotion"]
        self.assertEqual(dom_emotion, "fear")

unittest.main()
