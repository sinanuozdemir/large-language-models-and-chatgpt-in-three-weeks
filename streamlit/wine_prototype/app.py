# Import required modules
import os
import random

import openai  # OpenAI's Python client library
import streamlit as st  # The main library we're using to create a web interface
from datasets import load_dataset
from openai import OpenAI  # New import for OpenAI client

# Instantiate the OpenAI client with the API key from Streamlit secrets
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


@st.cache_resource
def load_wines():
    wine_dataset = load_dataset("alfredodeza/wine-ratings")
    return list(wine_dataset['test']) + list(wine_dataset['train']) + list(wine_dataset['validation'])


# make a table of wine_dataset to display and make clickable for the user
# Show the table
def convert_wine_to_string(wine):
    description = f'{wine["name"]} is from {wine["region"]} and is a {wine["variety"]}. {wine["notes"]}'

    return description


def get_recommendations(n=3, user_description=''):
    wines = random.sample(load_wines(), n)
    st.table(wines)
    wines_formatted = "\n---\n".join([convert_wine_to_string(w) for w in wines])
    print(f'User Description: {user_description}\nWines to select from:\n{wines_formatted}')

    chat_completion = client.chat.completions.create(
        model='gpt-3.5-turbo',
        messages=[
            {'role': 'system',
             'content': 'You are a wine bot that helps clients understand what kind of wine they want. '
                        'Given a list of wines and a description of the client, tell me what wines they '
                        'want by giving me the names of the wines. Include a reason preceding each pick '
                        'to explain to the user why they might like it. Give me the information  as a numbered list of'
                        ' wines with reasons why they might like it. I want the list in this format:\n'
                        'Reason 1: (the reason that the first wine matches the user description)\n'
                        'Wine 1: (the name of the first wine being recommended)\n'
                        'Reason 2: (the reason that the second wine matches the user description)\n'
                        'Wine 2: (the name of the second wine being recommended)\n'
                        'etc'},
            {'role': 'user',
             'content': f'User Description: {user_description}\nWines to select from:\n{wines_formatted}'}
        ]
    )
    st.write(chat_completion.choices[0].message.content)


user_description = st.text_input(
    "Describe the client", "The client likes red wine and is looking for a wine to drink with dinner."
)
n = st.number_input("How many wines to pull from the cellar?", min_value=1, max_value=10, value=3, step=1)
st.button("Get recommendations", on_click=get_recommendations, kwargs={'n': n, 'user_description': user_description})
