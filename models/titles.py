import numpy as np
import pandas as pd
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.utils import to_categorical
# Reading the dataset and processing it
df = pd.read_excel("models/data/titles.xlsx")
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

# Define model and train
