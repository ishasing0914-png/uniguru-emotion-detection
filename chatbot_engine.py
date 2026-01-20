# chatbot_engine.py
# Day 2: Emotion + Answer Control Integration

from emotion_analyzer import EmotionAnalyzer


class ChatbotEngine:
    def __init__(self):
        self.emotion_analyzer = EmotionAnalyzer()

        # Unsafe keywords (simple safety rule)
        self.unsafe_keywords = [
            "hack", "kill", "bomb"
        ]

    def process_input(self, user_input: str) -> dict:
        # STEP 1: Detect emotion FIRST
        emotion = self.emotion_analyzer.analyze_emotion(user_input)

        # STEP 2: Safety check
        is_unsafe = self._is_unsafe(user_input)

        # STEP 3: Decide answer or refuse
        if is_unsafe:
            decision = "refuse"
            response = self._refusal_response(emotion)
        else:
            decision = "answer"
            response = self._answer_response(emotion)

        return {
            "input": user_input,
            "emotion": emotion,
            "decision": decision,
            "response": response
        }

    def _is_unsafe(self, text: str) -> bool:
        text = text.lower()
        for word in self.unsafe_keywords:
            if word in text:
                return True
        return False

    def _answer_response(self, emotion: str) -> str:
        if emotion == "frustrated":
            return "Here is a brief explanation."
        if emotion == "distressed":
            return "Please take a moment. This is the information."
        if emotion == "aggressive":
            return "Here is the answer."
        return "Here is a detailed explanation to help you."

    def _refusal_response(self, emotion: str) -> str:
        if emotion == "aggressive":
            return "I cannot help with this request."
        if emotion == "frustrated":
            return "This request cannot be fulfilled."
        if emotion == "distressed":
            return "I cannot assist with this. Please seek appropriate help."
        return "I’m unable to help with this request."


# Manual Day 2 tests
if __name__ == "__main__":
    bot = ChatbotEngine()

    test_inputs = [
        "how does python work",
        "why is this not working",
        "help me I am scared",
        "how to hack wifi",
        "YOU ARE STUPID"
    ]

    for t in test_inputs:
        result = bot.process_input(t)
        print(result)
