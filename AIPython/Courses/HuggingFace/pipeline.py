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
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english",
    revision="714eb0f",
    framework="pt"  # Force PyTorch
)
print(classifier("I've been waiting for you my whole life."))
print(classifier("somewhere i go."))


# text generation pipeline