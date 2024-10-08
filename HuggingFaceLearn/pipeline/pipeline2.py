from transformers import pipeline


# can use different models with pipeline
generator = pipeline("text-generation",model="distilgpt2")

# different availble arguments refer to the documentation
res = generator(
    "In this course we will teach you how to",
    max_length=30,
    num_return_sequences=2
)

print(res)