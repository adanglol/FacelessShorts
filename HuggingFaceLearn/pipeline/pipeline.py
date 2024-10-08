# PipLine makes it simple to apply NLP class
# preprocess text - applying tokenizer - feeds preprocess text model - apply to model - postprocess
from transformers import pipeline
classifier = pipeline("sentiment-analysis")
result = classifier("I hate you")
print(result)