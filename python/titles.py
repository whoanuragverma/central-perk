import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import models, layers
import json
# Reading the dataset and processing it
df = pd.read_excel("data/titles.xlsx")
titles = list(df['Title'])
titles = [title.lower() for title in titles]

# Conversion to tokens
tokenizer = Tokenizer()
tokenizer.fit_on_texts(titles)

tot_words = len(tokenizer.word_index) + 1

input_sentences = []
for line in titles:
    sentences = tokenizer.texts_to_sequences([line])[0]
    for i in range(len(sentences)+1):
        sequences = sentences[:i+1]
        input_sentences.append(sequences)

# Conversion to padded sequences
max_len = max([len(x) for x in input_sentences])
input_sentences = np.array(pad_sequences(
    input_sentences, maxlen=max_len, padding='pre'))

xs, labels = input_sentences[:, :-1], input_sentences[:, -1]
ys = to_categorical(labels, num_classes=tot_words)
print(max_len)
# Define model and train
model = models.Sequential([
    layers.Embedding(tot_words, 150, input_length=max_len-1),
    layers.Bidirectional(layers.LSTM(150)),
    layers.Dense(tot_words, activation='softmax')]
)

model.summary()

model.compile(optimizer='adam',
              loss='categorical_crossentropy', metrics=['acc'])
history = model.fit(xs, ys, epochs=50, verbose=1)

model.save('models/title/model.h5')
with open('models/title/tokens.json', 'w', encoding='utf-8') as f:
    json.dump(tokenizer.to_json(), f)
