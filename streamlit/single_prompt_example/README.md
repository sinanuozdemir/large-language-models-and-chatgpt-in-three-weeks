# OpenAI Playground Web App

## Overview

This is a simple application for a set of prompts with a single input.

You can provide a system prompt to set a context for the model, a user prompt as the query for the model, and select which GPT model they wish to use for generating the response. This application uses OpenAI's Python client library to interact with the API and Streamlit to create the web interface.

## How to Run

Here are the steps to run this application:

1. **Install Dependencies**:

    First, make sure Python is installed on your system. This application requires Python 3.6 or later.

    Next, install the necessary Python packages. You can do this by running the following command:

    ```
    pip install streamlit openai
    ```

2. **Get an OpenAI API Key**:

    In order to use OpenAI's models, you need to have an API key from OpenAI. You can obtain this by creating an account on [OpenAI's website](https://www.openai.com/) and subscribing to their API.

3. **Set up Streamlit Secrets**:

    You can securely set your OpenAI API key using Streamlit secrets. In your Streamlit application directory, run:

    ```
    streamlit secrets new
    ```

    In the text editor that opens up, add the following line:

    ```
    [openai]
    openai_key = "your-openai-api-key"
    ```

    Replace "your-openai-api-key" with your actual OpenAI API key. Save and close the editor.

4. **Run the Streamlit App**:

    Finally, in your terminal, navigate to the directory containing the Python script for the Streamlit app and run the following command:

    ```
    streamlit run your_script.py
    ```

    Replace "your_script.py" with the actual filename of your Streamlit script.
