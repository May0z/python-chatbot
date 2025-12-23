responses = {
  'hi':'Hello, how are you?',
  'i am fine': 'That\'s good to know.',
  'how are you': 'I am just a code, but I\'m doing great',
  'good': 'Thankyou!',
  'bye':'Goodbye, please type "exit" to quit'
}

print('Hi! I\'m a simple chatbot')

while True:
  user_msg = input('You: ').lower()

  if user_msg.lower() == 'exit' :
    print('Bot: Goodbye, I\'m out...')
    break

  reply = responses.get(user_msg, 'I don\'t understand')
  print('Bot:',reply)
