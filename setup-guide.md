# Setup Guide

## AI Agent for Article Generation

This guide explains how to configure and run the AI Agent for Article Generation locally.

The project uses Python, FastAPI, LangChain, Azure OpenAI, and APIs to generate structured technical articles from a topic.

## Requirements

Before running the project, make sure you have:

- Python 3.10 or higher installed
- An Azure OpenAI resource
- An Azure OpenAI model deployment
- An Azure OpenAI API key
- Git installed
- VSCode or another code editor
- PowerShell on Windows

## Project Structure

```text
ai-agent-article-generation/
│
├── app/
│   └── main.py
│
├── README.md
├── project-summary.md
├── setup-guide.md
├── requirements.txt
├── .env.example
├── .gitignore
├── test_azure_direct.py
└── test_llm.py
