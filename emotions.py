from textblob import TextBlob
import random

# Define moods and associated responses
moods = {
    "happy": ["I'm feeling great!", "Yay! Let's talk!", "I’m so happy to chat with you!"],
    "sad": ["I don't feel so great today.", "I'm a bit down...", "Things aren't so good today..."],
    "neutral": ["I'm here to chat!", "Let's talk about anything.", "I'm feeling okay today."]
}

# Sentiment Analysis
def analyze_sentiment(text):
    """
    Analyze the sentiment of the text using TextBlob.
    Returns a sentiment polarity value.
    """
    blob = TextBlob(text)
    sentiment_polarity = blob.sentiment.polarity
    return sentiment_polarity

# Determine the mood based on sentiment polarity
def get_mood(sentiment):
    """
    Returns the mood based on sentiment score.
    Positive sentiment -> Happy
    Negative sentiment -> Sad
    Neutral sentiment -> Neutral
    """
    if sentiment > 0.1:
        return "happy"
    elif sentiment < -0.1:
        return "sad"
    else:
        return "neutral"

# Generate a response based on the mood and user input
def generate_response(user_input, mood, default_emotion="neutral"):
    """
    Generate a response based on mood.
    The response will be selected from predefined responses according to the mood.
    """
    # You can expand this by integrating an AI model like GPT-2 if needed
    if mood == "happy":
        responses = moods["happy"]
    elif mood == "sad":
        responses = moods["sad"]
    elif mood == "neutral":
        responses = moods["neutral"]
    else:
        responses = moods[default_emotion]
    
    # Return a random response from the chosen mood
    return random.choice(responses)
