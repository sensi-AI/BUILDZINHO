import os
import openai

from senha import API_KEY

openai.api_key = API_KEY

response = openai.Completion.create(
engine="davinci",
prompt="This is a Sentence sentiment classifier\n\n\nSentence: \"I loved the new Batman movie!\"\nSentiment: Positive\n###\nSentence: \"I hate it when my phone battery dies.\"\nSentiment: Negative\n###\nSentence: \"My day has been 👍\"\nSentiment: Positive\n###\nSentence: \"This is the link to the article\"\nSentiment: Neutral\n###\nSentence: \"This new music video blew my mind\"\nSentiment:",
temperature=0.3,
max_tokens=60,
top_p=1.0,
frequency_penalty=0.5,
presence_penalty=0.0,
stop=["###"])
print (response)