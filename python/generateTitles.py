from tensorflow.keras import models
import json
from keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences
import random
with open("models/title/tokens.json", encoding='utf-8') as f:
    tokenizer = tokenizer_from_json(json.load(f))

model = models.load_model("models/title/model.h5")


while True:
    seed_text = "The one with the " + \
        list(tokenizer.word_index.keys())[random.randint(
            0, (len(tokenizer.word_index)-1))]
    for _ in range(random.randint(2, 6)):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=10, padding='pre')
        predicted = model.predict_classes(token_list, verbose=0)
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        if(output_word != "ii" and len(output_word) > 1):
            seed_text += " " + output_word
    print(seed_text)
