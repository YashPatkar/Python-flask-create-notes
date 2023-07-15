# import pyttsx3

# engine = pyttsx3.init()

# text = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Illo omnis, ad recusandae excepturi placeat fugit in totam, quo maiores, quisquam ipsam illum obcaecati eos. Quos tenetur iusto quia porro ad fuga nisi, alias et rerum, aliquam reprehenderit ducimus nesciunt aut ex, delectus velit cum."
# engine.say(text)
# engine.runAndWait()

import pyttsx3

engine = pyttsx3.init()

# Changing the voice
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Index 1 corresponds to a different voice

# Changing the speed
rate = engine.getProperty('rate')
engine.setProperty('rate', rate - 500)  # Decrease the rate by 50 (adjust as desired)

text = "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Illo omnis, ad recusandae excepturi placeat fugit in totam, quo maiores, quisquam ipsam illum obcaecati eos. Quos tenetur iusto quia porro ad fuga nisi, alias et rerum, aliquam reprehenderit ducimus nesciunt aut ex, delectus velit cum."
engine.say(text)
engine.runAndWait()

