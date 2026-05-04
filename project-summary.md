# Project Summary

## AI Agent for Article Generation

AI Agent for Article Generation is a practical AI project that generates structured technical articles from a topic provided by the user.

The project was built with Python, LangChain, Azure OpenAI, FastAPI, and APIs. It exposes an API endpoint that receives an article topic and returns a complete content package including title, subtitle, summary, SEO description, keywords, Hashnode tags, full article, LinkedIn post, research notes, and draft status.

## Purpose

The purpose of this project is to demonstrate how AI agents can support technical content creation by combining language models, prompt orchestration, structured outputs, and API-based automation.

Instead of generating only free-form text, the agent returns organized fields that can be reused by other tools, such as n8n, Google Sheets, Gmail, Google Docs, or publishing workflows.

## Problem Addressed

Creating technical articles usually requires several manual steps:

- defining the article angle
- organizing the structure
- writing the draft
- preparing SEO metadata
- selecting keywords and tags
- creating a social media post
- preparing the content for review or publication

This project automates the first draft generation process while keeping the final content structured and ready for human review.

## Technical Architecture

The project follows this architecture:

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
↓
Optional n8n integration
