import os
import warnings

# Set environment variables BEFORE importing any ML libraries
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # Suppress all TensorFlow logs
os.environ['TRANSFORMERS_VERBOSITY'] = 'error'  # Reduce transformers verbosity

from transformers import pipeline
import torch

# Suppress warnings
warnings.filterwarnings('ignore')

# Force PyTorch backend to avoid TensorFlow compatibility issues
# classifier = pipeline(
#     "sentiment-analysis"
# )
# # Neutral/factual statements
# print(classifier("The weather is 20 degrees today."))
# print(classifier("Python is a programming language."))

# # Questions
# print(classifier("What time is it?"))
# print(classifier("How do you install packages?"))

# # Instructions/commands
# print(classifier("Please turn off the lights."))
# print(classifier("Save the file to the desktop."))

# # Descriptions
# print(classifier("The book has 300 pages."))
# print(classifier("The car is parked outside."))


# # zero-shot classification with a smaller model
# classifier = pipeline(
#     "zero-shot-classification",
#     model="typeform/distilbert-base-uncased-mnli",  # Smaller, faster model
#     # device=0 if torch.cuda.is_available() else -1
# )

# # Zero-shot classification examples
# print(classifier("The weather is 20 degrees today.", candidate_labels=["weather", "temperature", "climate"]))
# print(classifier("The car is parked outside.", candidate_labels=["vehicle", "transportation", "parking"]))



# generator = pipeline("text-generation")
# generator("In this course, we will teach you how to")

# unmasker = pipeline("fill-mask")
# unmasker("This course will teach you all about <mask> models.", top_k=2)

# ner = pipeline("ner", grouped_entities=True)
# ner("My name is Sylvain and I work at Hugging Face in Brooklyn.")


# question_answerer = pipeline("question-answering")
# question_answerer(
#     question="Where do I work?",
#     context="My name is Sylvain and I work at Hugging Face in Brooklyn",

# classifier = pipeline(
#     "zero-shot-classification",
#     model="typeform/distilbert-base-uncased-mnli",  # Smaller, faster model
# )

# # # Example usage:
# print(classifier("Today will be a good day", candidate_labels=["optimistic", "temperature", "climate"]))

classifier = pipeline(
    "text-generation",
    model="HuggingFaceTB/SmolLM2-360M",
)

# Example usage:
print(classifier("Burada sadece dondurma yapmayi ogreneceksiniz", max_length=50, num_return_sequences=2))