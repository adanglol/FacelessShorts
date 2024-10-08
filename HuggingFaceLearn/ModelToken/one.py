from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification

# Sentiment analysis
classifier = pipeline('sentiment-analysis')
res = classifier("I've been waiting for a HuggingFace course my whole life.")
print(res)


# how pipeline works uses model and tokenizer
model_name = "distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)
classifier = pipeline('sentiment-analysis', model=model, tokenizer=tokenizer)
res = classifier("I've been waiting for a HuggingFace course my whole life.")
print(res)


# Tokenizer puts text into mathematical form which model can understand
sequence ="Using transformers is easy"
res = tokenizer(sequence)
print(res)
tokens = tokenizer.tokenize(sequence)
print(tokens)
ids = tokenizer.convert_tokens_to_ids(tokens)
print(ids)
decodedString = tokenizer.decode(ids)
print(decodedString)
