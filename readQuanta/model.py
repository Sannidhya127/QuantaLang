import numpy as np
import tensorflow as tf
from difflib import SequenceMatcher
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
import spacy
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def infer_data_type(value):
    # Check for numeric types
    try:
        int_value = int(value)
        return "int"
    except ValueError:
        pass

    try:
        float_value = float(value)
        return "float"
    except ValueError:
        pass

    # Check for boolean type
    if value.lower() in ["true", "false", "1", "0"]:
        return "bool"

    # Check for date and time types (not implemented in this example)

    # Fallback to string type
    return "str"
# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Define regular expressions for matching variable declarations
var_declaration_pattern = r"(let|var|const)\s+(\w+)\s*[:=]\s*(\w+|\d+)"


def extract_variable_info(code_snippet):
    # Tokenize the code snippet using spaCy
    doc = nlp(code_snippet)
    
    # Initialize variables to store extracted information
    variable_info = []

    # Find variable declarations using regular expressions
    var_declarations = re.findall(var_declaration_pattern, code_snippet)
    
    # Process each variable declaration
    for declaration in var_declarations:
        declaration_type, variable_name, value = declaration
        data_type = infer_data_type(value)
        variable_info.append({
            "type": data_type,
            "name": variable_name,
            "value": value
        })
    
    return variable_info


# Example code snippet
code_snippet = "let x = 10"
variable_info = extract_variable_info(code_snippet)
print(variable_info)


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
    "int a = 4",
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
given_code = "b = 5"

# Predict the label for the given code
predicted_label = model.predict([given_code])[0]
print("Predicted label:", predicted_label)

# if predicted_label == "variable_declaration":
    

