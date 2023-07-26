---
title: Wine Recommendation Bot
emoji: 🍷
colorFrom: "#FF0000"
colorTo: "#8B0000"
sdk: streamlit
sdk_version: "1.0.0"
app_file: app.py
pinned: false
---

# Wine Recommendation System

## Overview

This web application leverages OpenAI's GPT model to generate wine recommendations based on a client's description. The application uses the Hugging Face Datasets library to load a dataset of wines, OpenAI's Python client library to interact with the GPT model, and Streamlit for the web interface.

When a user provides a description of a client and the number of wines they'd like to choose from, the application randomly selects the specified number of wines from the dataset. It then uses the GPT model to generate recommendations based on the selected wines and the client's description, and displays these recommendations on the web interface.

## How to Run

### 1. Install Dependencies

Ensure Python is installed on your system. Python 3.6 or later is required.

Install necessary Python packages with the following command:

```
pip install streamlit openai datasets
```


### 2. Get an OpenAI API Key

You need an API key from OpenAI to use OpenAI's models. You can get this by creating an account on [OpenAI's website](https://www.openai.com/) and subscribing to their API.

### 3. Set up Streamlit Secrets

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

### 4. Run the Streamlit App

Navigate to the directory containing the Python script for the Streamlit app in your terminal and run:

```
streamlit run your_script.py
```