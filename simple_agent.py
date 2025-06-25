import os
from openai import OpenAI

#set open api key
# os.environ["OPENAI_API_KEY"]="key"

# client = OpenAI()

# Set your actual OpenAI API key
client = OpenAI(api_key="api-key")

response = client.chat.completions.create(

    model="gpt-3.5-turbo",
    messages=[
        {"role": "user",
        "content": "What are OOPS Concepts in Java?"
        }
    ],
    max_tokens=100
)


print(response.choices[0].message.content.strip())

