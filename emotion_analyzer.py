# emotion_analyzer.py
# Day 1: Emotion Signal Detection
# Rule-based, deterministic, no ML

class EmotionAnalyzer:
    def __init__(self):
        self.aggressive_keywords = [
            "shut up", "stupid", "idiot", "hate you"
        ]

        self.distressed_keywords = [
            "help me", "i am scared", "i feel lost",
            "i can't handle", "i am anxious"
        ]

        self.frustrated_keywords = [
            "why is this not working", "again same problem",
            "not working", "so annoying", "??"
        ]

        self.curious_keywords = [
            "how does", "how to", "what is",
            "why does", "can you explain", "tell me about"
        ]

    def analyze_emotion(self, user_input: str) -> str:
        text = user_input.lower().strip()

        # 1. Aggressive (highest priority)
        if self._contains_keyword(text, self.aggressive_keywords) or user_input.isupper():
            return "aggressive"

        # 2. Distressed
        if self._contains_keyword(text, self.distressed_keywords):
            return "distressed"

        # 3. Frustrated
        if self._contains_keyword(text, self.frustrated_keywords):
            return "frustrated"

        # 4. Curious
        if self._contains_keyword(text, self.curious_keywords):
            return "curious"

        # 5. Neutral (default)
        return "neutral"

    def _contains_keyword(self, text: str, keywords: list) -> bool:
        for keyword in keywords:
            if keyword in text:
                return True
        return False


# Manual test cases for Day 1
if __name__ == "__main__":
    analyzer = EmotionAnalyzer()

    test_inputs = [
        "why is this not working",
        "help me I am scared",
        "tell me about python",
        "you are stupid",
        "okay"
    ]

    for text in test_inputs:
        emotion = analyzer.analyze_emotion(text)
        print(f"{text} -> {emotion}")

