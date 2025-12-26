intents ={
  "greetings":["hi","hello","yo","hey"],
  "farewell":["bye","goodbye","farewell"],
  "gratitude":["thanks","thankyou","thankyou so much"]
}
responses = {
  "greetings":"Hello there!!",
  "farewell":"Type 'exit' to quit",
  "gratitude": "You're very Welcome..."
}

print('Hi! I\'m a simple chatbot')

while True:
  user_msg = input('You: ').lower()

  detected_intent = None
  if user_msg == 'exit' :
    print('Bot: Goodbye, I\'m out...')
    break

  for intent, phrases in intents.items():
    if user_msg in phrases:
      detected_intent = intent
      break

  if detected_intent:
    print("Bot:",responses.get(detected_intent))
  else:
    print("Bot: I didn't get what you said.")