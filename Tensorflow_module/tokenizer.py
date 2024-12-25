import tensorflow as tf 

from tensorflow import keras 

from tensorflow.keras.preprocessing.text import Tokenizer

from tensorflow.keras.preprocessing.sequence import pad_sequences


sentences = ['I love my dog', 'I love my cat', 'You love my dog', 'I love my cat!', 'Do you think my dog is amazing?'] # The tokenizer won't produce a new tokken for the cat!

tokenizer = Tokenizer(num_words = 100, oov_token='<OOV>') # The oov tokken is a word that represents a out of vocabulary token meaning it's a marker for tokkens that are out of context of tokkens

tokenizer.fit_on_texts(sentences)

word_index = tokenizer.word_index

sequence = tokenizer.texts_to_sequences(sentences)

padded = pad_sequences(sequence)

print(word_index)

print(sequence)

print(padded)