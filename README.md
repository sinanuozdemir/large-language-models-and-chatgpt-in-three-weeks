# Large Language Models and ChatGPT in Three Weeks

Welcome to the "[Large Language Models and ChatGPT in Three Weeks](https://learning.oreilly.com/live-events/large-language-models-and-chatgpt-in-3-weeks/0636920090988/)" code repository! In this repo, we dive deep into understanding and utilizing large language models, with a specific focus on OpenAI's GPT-3, GPT-3.5-turbo (ChatGPT), and GPT-4.

For more, check out my [Expert Playlist](https://learning.oreilly.com/playlists/2953f6c7-0e13-49ac-88e2-b951e11388de)!

Much of the code in these sessions come from my latest book on LLMs: [A Quick Start Guide to LLMs](https://github.com/sinanuozdemir/quick-start-guide-to-llms) so if you're itching for more, check it out and please leave a rating/review to tell me what you thought :)

## Project Overview

The project is divided into the following sections:

1. **Introduction to Large Language Models (LLMs)**: We start with a brief introduction to LLMs, understanding their architecture, strengths, and potential use-cases.

2. **Working with ChatGPT**: ChatGPT is a version of the GPT model fine-tuned for generating conversational responses. We'll learn how to make API calls to ChatGPT and interpret the responses.

3. **Latency Evaluation**: We analyze and compare the latency of API calls when using hosted API services versus running models on local compute resources. This helps in making informed decisions about where to run these powerful models.

4. **Cost Calculation**: The code includes methods to calculate the cost of API calls based on the token usage by different models.

5. **Generating Responses with OpenAI Models**: We use the OpenAI's `ChatCompletion` and `Completion` methods to generate responses from prompts.

The code in this project helps you to get hands-on experience with these powerful language models, and also gives insights about factors to consider when deciding to use these models, such as cost and latency.

## Prerequisites

- Familiarity with Python
- An OpenAI API key. You can obtain it by signing up on the [OpenAI website](https://www.openai.com/).
- Familiarity with machine learning concepts and natural language processing would be helpful, but not mandatory.

## Installation

1. Clone this repository to your local machine.
2. Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```
Ensure you have set the following environment variables with your API keys or tokens:

```
OPENAI_API_KEY: Your OpenAI API key.
COHERE_API_KEY: Your Cohere API key (if using Cohere's services).
HF_TOKEN: Your Hugging Face token (if using Hugging Face's services).
```
You're all set to explore the notebooks!

## Usage - Jupyter Notebooks

This project contains several Jupyter notebooks each focusing on a specific topic. You can find them in the `notebooks` directory:

1. **[Intro to Prompt Engineering](./notebooks/intro_prompt_engineering.ipynb)**: This notebook introduces the concept of prompt engineering, a crucial aspect of effectively using language models.

2. **[Making Predictions](./notebooks/making_predictions.ipynb)**: Here, we delve into the process of making predictions with large language models and interpret their responses.

3. **[Cost Projecting](./notebooks/cost_projecting.ipynb)**: This notebook focuses on understanding and calculating the costs involved in using large language models. It includes functions to calculate the cost of API calls based on the token usage by different models.

4. **[OpenRouter + Prompt Caching](./notebooks/OpenRouter_and_prompt_caching.ipynb)**: Using OpenRouter to be more model/provider agnostic plus a tutorial on prompt caching

4. **[Use Cases](./notebooks/use_cases.ipynb)**: In this notebook, we explore various use cases for large language models, providing practical examples of how they can be used in different scenarios.

5. **Retrieval Augmented Generation (RAG)**
	- **[RAG - Retrieval](notebooks/RAG_Retrieval.ipynb)**: An introduction to vector databases, embeddings, and retrieval
	- **[RAG - Generation](notebooks/RAG_Generate.ipynb)**: Building a RAG chatbot using our semantic search retrieval system
	- **[Advanced - GraphRAG](notebooks/GraphRAG.ipynb)** - A simple introduction to GraphRAG (RAG using a knowledge graph) using Neo4J, Cohere's Re-Rank, GPT-4o, and a touch of Langchain
	- **[Evaluating LLMs with Rubrics](https://colab.research.google.com/drive/1DeVYrdNb3FlQQLeBqGPFkx6roZaPwVRy?usp=sharing)** - Exploring a rubric prompt to evaluate generative output
	- **[CLIP-based Stock Image Search](https://colab.research.google.com/drive/1aUz0FKQDSAyXyhRyvkkRsSy7S30mpRJc?usp=sharing)**: Using CLIP to search through a library of images
     - **[Workflow Evaluation](https://github.com/sinanuozdemir/oreilly-ai-agents/blob/main/notebooks/LangGraph_Workfow_Eval.ipynb)**  

6. **[AI Agents](https://colab.research.google.com/drive/14jAlW2E7ya_aS1M6eUsuHciC1WvLfIif?usp=sharing)**: A simple application of an AI agent who can google things, create images, and check a paper stock portfolio

	-  **[ReAct Agents in LangGraph + MCP + Tool Positional Bias]([notebooks/LangGraph_React%20-%20MCP%20+%20Tool%20Selection.ipynb](https://github.com/sinanuozdemir/oreilly-ai-agents/blob/main/notebooks/LangGraph_React%20-%20MCP%20+%20Tool%20Selection.ipynb))** - Integrating MCP with a ReAct Agent in Langgraph + Testing for Positional Bias

**BONUS NOTEBOOKS**

- **[LLM Token Embeddings](./notebooks/LLM%20Embeddings.ipynb)**: In this notebook, I look at the token embeddings of BERT and GPT2 to show how the masked/non-masked attention systems affect the embeddings based on their position in a document.

- **[Fine-tuning BERT for Classification](./notebooks/bert_app_review.ipynb)**: In this notebook, I fine-tune a BERT model for classification and showcase some metrics compared to ChatGPT.

- **[Fine-tuning OpenAI for Classification](./notebooks/openai_app_review_fine_tuning.ipynb)**: In this notebook, I fine tune some OpenAI models to an open dataset.

- **[Fine-tuning embeddings](https://colab.research.google.com/drive/1FOr9hgMEcTa8UJJSuKjoHpohVb-Qz-FJ?usp=sharing)**: In this notebook, I fine-tune an embedding model to compete with OpenAI's embeddings out of the box.


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

