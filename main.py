print('Hi! I\'m a simple chatbot')
print('Type "exit" to stop')

while True:
  user_msg = input('You: ')

  if user_msg.lower() == 'exit' :
    print('Bot: Goodbye...')
    break
  elif user_msg.lower() == 'hi':
    print('Bot: Hello! how are you?')
  elif user_msg.lower() == 'how are you':
    print('Bot: I am just a code, but I am fine')
  else:
    print('Bot: I didn\'t understand what you just said')
    
