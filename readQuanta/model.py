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
from sympy import symbols, simplify

def infer_data_type(value):
    """
    Infer the data type of a given value.

    Parameters:
    value (str): The value to infer the data type from.

    Returns:
    str: The inferred data type of the value.
    """
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
def parse_value(value, variables):
    # Tokenize the value using spaCy
    tokens = nlp(value)

    # Check if the value contains letters (indicating variables)
    contains_letters = any(token.is_alpha for token in tokens)

    # Check if the value contains commas (indicating multiple values)
    contains_commas = "," in value

    # Check if the value contains operators (indicating a mathematical expression)
    contains_operators = any(token.text in "+-*/" for token in tokens)

    # Check if the value contains digits (indicating numeric values)
    contains_digits = any(token.text.isdigit() for token in tokens)

    # Check if the value contains a polynomial expression
    is_polynomial = False
    if contains_letters and contains_operators:
        # If the value contains letters and operators, it might be a polynomial
        # Check if the expression follows the pattern of a polynomial
        polynomial_pattern = r"([+-]?\d*[a-zA-Z]+\^?\d*)+([+-]?\d*[a-zA-Z]+\^?\d*)*"
        if re.fullmatch(polynomial_pattern, value):
            is_polynomial = True

    # Evaluate the value if it contains variables
    evaluated_value = None
    if contains_letters:
        if contains_commas:
            # Currently not supporting substitution for string containing multiple values
            value_type = "String containing multiple values"
        elif is_polynomial:
            # Create symbols for the variables
            vars = symbols(variables.keys())
            # Substitute variable values and simplify the expression
            substituted_value = simplify(value, dict(zip(vars, variables.values())))
            evaluated_value = substituted_value
            value_type = "Polynomial"
        else:
            # Replace variables with their values
            for var, val in variables.items():
                value = value.replace(var, str(val))
            evaluated_value = value
            value_type = "Variable expression"
    elif contains_digits and contains_operators:
        # Evaluate the mathematical expression
        evaluated_value = eval(value)
        value_type = "Mathematical expression"
    elif contains_digits or "." in value:
        # Check if the value contains a dot (indicating a float)
        evaluated_value = float(value)
        value_type = "Float"
    elif contains_digits:
        # Check if the value is an integer
        evaluated_value = int(value)
        value_type = "Integer"
    else:
        value_type = "Unknown"

    return value_type, evaluated_value

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
    

# Test the function with different types of values
values = [
    "Hello, world!",      # String containing multiple values
    "x + 2*y - 3",        # Polynomial expression
    "x * y + 5",          # Polynomial expression
    "42",                 # Integer
    "3.14",               # Float
    "2.7e-3",             # Float
    "12 + 34 / 5",        # Mathematical expression
]

variables = {
    'x': 5,
    'y': 3
}
for value in values:
    value_type, evaluated_value = parse_value(value, variables)
    print(f"Value: {value}, Type: {value_type}, Evaluated Value: {evaluated_value}")