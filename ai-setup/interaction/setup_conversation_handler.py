from transformers import pipeline

class SetupConversationHandler:
    def __init__(self):
        self.classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

    def classify_intent(self, text):
        return self.classifier(text)[0]

    def handle_input(self, user_input):
        intent = self.classify_intent(user_input)
        if intent['label'] == 'POSITIVE' and intent['score'] > 0.85:
            print("It seems like you're confident with technology! Let's proceed with advanced setup options.")
        elif intent['label'] == 'NEGATIVE' and intent['score'] > 0.85:
            print("No worries! We'll guide you through the basic setup process.")
        else:
            print("I'm not quite sure about your preference. We'll start with a general setup, and you can customize it later.")

if __name__ == "__main__":
    handler = SetupConversationHandler()
    print("Welcome to the Setup Assistant! How comfortable are you with technology? (e.g., very comfortable, not comfortable)")
    user_input = input()
    handler.handle_input(user_input)
