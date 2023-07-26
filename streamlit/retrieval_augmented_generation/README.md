# Document Question Answering System

## Overview

This web application uses OpenAI's GPT model to answer questions based on a context scraped from a URL provided by the user. The application uses OpenAI's Python client library to interact with the GPT model, the BeautifulSoup library to parse HTML content, and Streamlit for the web interface.

The user provides a URL, a question, and an optional system prompt. The application fetches and parses the HTML content from the URL, uses it as context to answer the question using the GPT model, and displays the answer on the web interface.

## How to Run

Here are the steps to run this application:

1. **Install Dependencies**:

    Make sure Python is installed on your system. Python 3.6 or later is required.

    Install the necessary Python packages with the following command:

    ```
    pip install streamlit openai beautifulsoup4 requests
    ```

2. **Get an OpenAI API Key**:

    To use OpenAI's models, you need an API key from OpenAI. Obtain this by creating an account on [OpenAI's website](https://www.openai.com/) and subscribing to their API.

3. **Set up Streamlit Secrets**:

    Securely set your OpenAI API key using Streamlit secrets. In your Streamlit application directory, run:

    ```
    streamlit secrets new
    ```

    In the text editor that opens, add the following line:

    ```
    [openai]
    openai_key = "your-openai-api-key"
    ```

    Replace "your-openai-api-key" with your actual OpenAI API key. Save and close the editor.

4. **Run the Streamlit App**:

    Navigate to the directory containing the Python script for the Streamlit app in your terminal and run:

    ```
    streamlit run app.py
    ```

    Replace "your_script.py" with the actual filename of your Python script.
