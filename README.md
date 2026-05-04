# AI Agent for Article Generation

AI Agent for Article Generation is a Python-based AI agent that uses LangChain, Azure OpenAI, and APIs to generate structured technical articles from a topic provided by the user.

The agent receives a topic, prepares a structured prompt, optionally collects basic research context through a public API, and returns a complete article package including title, subtitle, summary, SEO description, keywords, Hashnode tags, full article, LinkedIn post, research notes, and draft status.

## Project Objective

The objective of this project is to demonstrate how AI agents can support technical content creation by combining prompt orchestration, structured output, external API usage, and Azure OpenAI.

This project is aligned with real-world use cases involving technical blogging, professional content creation, AI automation, and developer productivity.

## Main Features

- Receives a topic through an API request
- Uses LangChain to orchestrate the prompt flow
- Uses Azure OpenAI as the language model provider
- Generates structured article output
- Creates article title, subtitle, summary, SEO description, keywords, and Hashnode tags
- Generates a complete long-form article
- Generates a LinkedIn post to promote the article
- Includes a simple research step using a public API
- Exposes the agent through a FastAPI endpoint
- Returns structured JSON ready to be used by other automation tools

## Technologies Used

- Python
- FastAPI
- LangChain
- Azure OpenAI
- APIs
- Pydantic
- Uvicorn
- python-dotenv

## How It Works

The workflow follows this structure:

```text
User topic
↓
FastAPI endpoint
↓
LangChain prompt orchestration
↓
Simple research step through public API
↓
Azure OpenAI generation
↓
Structured JSON response