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
classifier = pipeline(
    "sentiment-analysis"
)
# Neutral/factual statements
print(classifier("The weather is 20 degrees today."))
print(classifier("Python is a programming language."))

# Questions
print(classifier("What time is it?"))
print(classifier("How do you install packages?"))

# Instructions/commands
print(classifier("Please turn off the lights."))
print(classifier("Save the file to the desktop."))

# Descriptions
print(classifier("The book has 300 pages."))
print(classifier("The car is parked outside."))


# text generation pipeline