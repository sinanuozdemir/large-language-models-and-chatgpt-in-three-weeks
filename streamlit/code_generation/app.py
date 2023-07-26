# Import necessary libraries
import openai  # Library for OpenAI API
import requests  # Library for making HTTP requests
import streamlit as st  # Library for creating web apps
from bs4 import BeautifulSoup  # Library for parsing HTML and XML documents

# Set the OpenAI API key from Streamlit secrets
openai.api_key = st.secrets["openai_key"]


# Define function to communicate with OpenAI's GPT model
def code_gpt(task, html):
    # Initialize conversation prompts with user's question and context
    prompts = [{'role': 'user', 'content': f"Using the following html context, write javascript code to "
                                           f"write in the console of the browser to "
                                           f"perform the task using the code in the website."
                                           f"\n\nWebsite Code:{html}\n\nTask: {task}\n\nJS Code:"}]

    # Send conversation prompts to GPT model and get response
    chat_completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-16k",
        messages=prompts
    )

    # Extract response content and return as a dictionary
    return {'response_text': chat_completion.choices[0].message.content}


# Set title for the Streamlit app
st.title('Code Generation Example')

# Create a text input field for users to enter a URL
url = st.text_area(
    label="URL to scrape for context",
    value="https://ai-office-hours.beehiiv.com"
)

# Create a text input field for users to enter their question
task = st.text_input("Task to perform", value="Subscribe to Sinan's newsletter")

# Process query if there is one
if st.button("Run"):
    html = requests.get(url).text  # Get the HTML from the URL
    print(html)

    # Call the GPT model function with the extracted text and user's question
    answer = code_gpt(task, html)

    # Display the model's response on the web app
    st.write(answer["response_text"])
