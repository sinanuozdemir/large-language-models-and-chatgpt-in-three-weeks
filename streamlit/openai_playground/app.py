import os

import streamlit as st  # Streamlit library for creating web apps
from openai import OpenAI  # New import for OpenAI client

# Instantiate the OpenAI client with the API key from Streamlit secrets
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


# Define a function for running a conversation with OpenAI
def run_prompt_through_openai(system_prompt, user_prompt, model):
    # Use the OpenAI client to create a ChatCompletion instance for the conversation
    chat_completion = client.chat.completions.create(
        model=model,  # Specify the model to use for the conversation
        messages=[  # Define the messages for the conversation
            {'role': 'system', 'content': system_prompt},  # The initial system message
            {'role': 'user', 'content': user_prompt}  # The user's message
        ]
    )
    # Extract and return the AI's response from the conversation
    return chat_completion.choices[0].message.content


# Rest of your Streamlit app code remains the same...


# Set a title for the Streamlit app
st.title("OpenAI Playground")

# Create a text input field for the system prompt, with a default value
system_prompt = st.text_input(
    "System Prompt", value="You are a language translator. You translate between English and Turkish."
)

# Create a text input field for the user prompt, with a default value
user_prompt = st.text_input("User Prompt", value="Hello, how are you?")

# Create a select box for choosing the OpenAI model
model = st.selectbox("Model", ['gpt-3.5-turbo', 'gpt-4', 'gpt-3.5-turbo-16k'])

# Create a button for executing the AI conversation
if st.button("Run"):
    # If the button is clicked, run the user and system prompts through the chosen AI model
    response = run_prompt_through_openai(system_prompt, user_prompt, model)

    # Write the AI's response in the app
    st.write(f"Response:\n---\n{response}")
