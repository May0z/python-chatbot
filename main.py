import random


intents ={
  "greetings":["hi","hello","yo","hey"],
  "farewell":["bye","goodbye","farewell"],
  "gratitude":["thanks","thankyou","thankyou so much"]
}
responses = {
  "greetings":["Hello there!!", "Hi", "Well Hello !", "Hey!", "Yo!"],
  "farewell":["Type 'exit' to quit", "Type 'exit', if you wish to quit"],
  "gratitude": ["You're very Welcome...","My pleasure!", "Don't mention it..."]
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
    print("Bot:",random.choice(responses.get(detected_intent)))
  else:
    print("Bot: I didn't get what you said.")