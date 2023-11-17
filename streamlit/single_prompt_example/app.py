import os

import streamlit as st  # Streamlit library for creating web apps
from openai import OpenAI  # New import for OpenAI client

# Instantiate the OpenAI client with the API key from Streamlit secrets
client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])


# Define a function for running a conversation with OpenAI
def run_prompt_through_openai(system_prompt, user_prompt, model='gpt-3.5-turbo'):
    # Use the OpenAI client to create a ChatCompletion instance for the conversation
    chat_completion = client.chat.completions.create(
        model=model,  # Specify the model to use for the conversation
        messages=[  # Define the messages for the conversation
            {'role': 'system', 'content': system_prompt},  # The initial system message
            {'role': 'user', 'content': user_prompt}  # The user's message
        ],
        temperature=0.9,
        top_p=1,
    )
    # Extract and return the AI's response from the conversation
    return chat_completion.choices[0].message.content


# Set a title for the Streamlit app
st.title("Single Input Example")
st.write("This is an example of a single input field for a conversation with the AI.")

# Create a text input field for the system prompt, with a default value
system_prompt = "You are a Twitter bot that helps people with their tweets"

# Create a text input field for the user prompt, with a default value
user_input = st.text_input("Description of a tweet you want", value="I need a tweet about GPT-4")

user_prompt = '''
Input: I need a tweet about GPT-4
Tweet: "Wow! I just read about GPT-4 and it's amazing! I can't wait to see what it can do! #gpt4 #ai #machinelearning"
Input: Dogs in the summer and avoiding fleas and ticks
Tweet: "I love my dog, but I hate the fleas and ticks that come with him. I'm going to try to avoid them this summer."
Input: San Francisco's Golden Gate Bridge
Tweet: "I love the Golden Gate Bridge. It's a beautiful sight to see. I can't wait to go back to San Francisco."
Input: {user_input}'''  # This is where the user's input will be added

# Create a button for executing the AI conversation
if st.button("Run"):
    user_prompt = user_prompt.format(user_input=user_input)
    # If the button is clicked, run the user and system prompts through the chosen AI model
    response = run_prompt_through_openai(system_prompt, user_prompt)

    # Write the AI's response in the app
    st.write(f"# System Prompt\n{system_prompt}\n# User Prompt\n{user_prompt}\n# AI Response\n{response}")
