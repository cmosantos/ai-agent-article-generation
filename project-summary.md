# Project Summary

## Project Name

AI Agent for Article Generation

## Description

AI Agent for Article Generation is a practical AI project built with Python, LangChain, Azure OpenAI, FastAPI, and APIs.

The agent receives a topic through an API request, uses LangChain for prompt orchestration, calls Azure OpenAI to generate structured content, and returns a complete article package including title, subtitle, summary, SEO description, keywords, Hashnode tags, full article, LinkedIn post, research notes, and draft status.

## Problem Solved

Technical professionals, learners, and content creators often spend time organizing article ideas, creating outlines, writing drafts, generating SEO metadata, preparing publication tags, and creating social media posts.

This project automates the first draft creation process while keeping the output structured and ready for human review.

## Main Capabilities

- Receives article topics through a FastAPI endpoint
- Uses Azure OpenAI as the language model provider
- Uses LangChain for prompt orchestration
- Generates structured article output
- Creates article title, subtitle, summary, SEO description, keywords, and tags
- Generates a complete long-form article draft
- Generates a LinkedIn post for article promotion
- Includes a simple research step through a public API
- Exposes the agent through an API endpoint
- Can be integrated with n8n using HTTP Request

## Technologies Used

- Azure OpenAI
- Python
- LangChain
- FastAPI
- APIs
- Pydantic
- Uvicorn
- n8n integration

## Workflow Overview

The project follows this flow:

```text
User topic
↓
FastAPI endpoint
↓
LangChain prompt orchestration
↓
Research step through public API
↓
Azure OpenAI generation
↓
Structured JSON response
↓
Optional n8n integration
