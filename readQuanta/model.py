import numpy as np
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Expanded synthetic dataset (code snippets with corresponding labels)
code_snippets = [
    "for i in range(10): print(i)",
    "x = 5",
    "def add(a, b): return a + b"
]

# Corresponding labels for language constructs
labels = np.array(["loop", "variable", "function"])

tokenizer = Tokenizer()
tokenizer.fit_on_texts(code_snippets)

max_length = max([len(text.split()) for text in code_snippets])

sequences = tokenizer.texts_to_sequences(code_snippets)
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64, input_length=max_length),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(3, activation='softmax')  # Output layer with 3 units for 3 language constructs
])
# Convert labels to integer encoding
label_mapping = {"loop": 0, "variable": 1, "function": 2}
encoded_labels = np.array([label_mapping[label] for label in labels])

model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64, input_length=max_length),
    tf.keras.layers.LSTM(64),
    tf.keras.layers.Dense(3, activation='softmax')  # Output layer with 3 units for 3 language constructs
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(padded_sequences, encoded_labels, epochs=10, verbose=1)

# Example code snippet for testing
test_code = "x is 5"

test_sequence = tokenizer.texts_to_sequences([test_code])
padded_test_sequence = pad_sequences(test_sequence, maxlen=max_length, padding='post')

# Predict the type of language construct for the test code snippet
prediction = model.predict(padded_test_sequence)
predicted_label = np.argmax(prediction)
if predicted_label == 0:
    print("Loop detected!")
elif predicted_label == 1:
    print("Variable assignment detected!")
elif predicted_label == 2:
    print("Function definition detected!")
