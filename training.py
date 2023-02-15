import random
import json
import pickle
import numpy as np
import nltk
# nltk.download('punkt')
from nltk.stem import WordNetLemmatizer

# import tensorflow as tf
# import keras as ks
# import Sequential as se
# from tensorflow.keras
# from tensorflow

# from tensorflow.keras.models import Sequential
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import Dense, Activation, Dropout
# from tensorflow.keras.optimizers import SGD

from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD


lemmatizer = WordNetLemmatizer()

intents = json.loads(open('intents.json').read())

words = []
classes = []
documents = []
ignore_letters = ['?', '!', '.', '.']

for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['tag']))
        if intent['tag'] not in classes:
            classes.append(intent['tag'])


print(documents)

