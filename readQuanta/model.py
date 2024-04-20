import numpy as np
import tensorflow as tf
from difflib import SequenceMatcher
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
def find_most_similar_code(code_string, code_snippets):
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer().fit_transform([code_string] + code_snippets)
    vectors = vectorizer.toarray()

    # Calculate the cosine similarity
    csim = cosine_similarity(vectors)

    # The first row of csim contains the similarity of the code_string to each code snippet
    # We ignore the first column because it's the similarity of the code_string to itself
    similarities = csim[0, 1:]

    # Find the index of the most similar code snippet
    most_similar_index = np.argmax(similarities)

    # Return the most similar code snippet
    return code_snippets[most_similar_index]


def compare_code(code, snippets):
    max_similarity = 0
    best_match = None
    for snippet in snippets:
        similarity = SequenceMatcher(None, code, snippet).ratio()
        if similarity > max_similarity:
            max_similarity = similarity
            best_match = snippet
    return best_match

# Define the code snippets
code_snippets = [
    "import math",
    "let int a = 4",
    "qubit q1 = (2,3)",
    "if (q1 < 0): probe.str(Nice)",
    "else-if (q1 > 0): probe.int(0)",
    "else: probe a",
    "function non_probalistic_func(): probe.str(This is not probabilistic)",
    "struct{ int b = 3 qubit q2 = (1,0)}"
]

labels = ["import", "variable_declaration", "qubit_declaration", "if_statement", "else_if_statement", "else_statement", "function_declaration", "struct_declaration"]
# Tokenize the code snippets
# Feature extraction and model pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),  # Convert text data into numerical TF-IDF features
    ('clf', SVC(kernel='linear')),  # Support Vector Machine classifier
])

# Train the model
model.fit(code_snippets, labels)

# Given code string
given_code = "let int b = 5"

# Predict the label for the given code
predicted_label = model.predict([given_code])[0]
print("Predicted label:", predicted_label)

# This is the other part

tokenizer = Tokenizer()
tokenizer.fit_on_texts(code_snippets)

max_length = max([len(text.split()) for text in code_snippets])

sequences = tokenizer.texts_to_sequences(code_snippets)
padded_sequences = pad_sequences(sequences, maxlen=max_length, padding='post')

# Define the model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Embedding(input_dim=len(tokenizer.word_index)+1, output_dim=64, input_length=max_length+1),
    tf.keras.layers.LSTM(64, return_sequences=True),
    tf.keras.layers.Dense(len(tokenizer.word_index)+1, activation='softmax')
])

model.compile(loss='sparse_categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Pad the sequences with zeros to match the expected input shape
X = pad_sequences(sequences, maxlen=max_length+1, padding='post')

# Separate input and output sequences
y = np.roll(X, -1, axis=1)
y[:, -1] = 0  # Set the last token to 0 as it does not have a corresponding output

# Train the model
model.fit(X, y, epochs=50, verbose=1)



# Generate compiled output
for snippet in code_snippets:
    sequence = tokenizer.texts_to_sequences([snippet])[0]
    padded_sequence = pad_sequences([sequence], maxlen=max_length+1, padding='post')  # Change to max_length+1
    prediction = model.predict(padded_sequence)
    predicted_token_index = np.argmax(prediction[0])  # Find the index with the highest probability
    predicted_token = tokenizer.index_word.get(predicted_token_index, '<UNK>')  # Use get method with default value
    print("Predicted next token:", predicted_token)

from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

code_string = "for i in range(10): print(i)"
print(find_most_similar_code(code_string, code_snippets))

given_code = "let int b = 5"
best_snippet = compare_code(given_code, code_snippets)
print("Given code resembles:", best_snippet)