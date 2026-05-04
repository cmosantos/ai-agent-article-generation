import os
import requests

from typing import List, Optional
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()

app = FastAPI(
    title="AI Article Generation Agent",
    description="Python API using LangChain and Azure OpenAI to generate structured technical articles.",
    version="1.0.0",
)


class ArticleRequest(BaseModel):
    topic: str = Field(..., description="Main topic or idea for the article")
    language: str = Field(default="English", description="Article language")
    audience: str = Field(default="Technology professionals and learners", description="Target audience")
    tone: str = Field(default="Professional, human, practical", description="Writing tone")


class ResearchItem(BaseModel):
    title: str
    snippet: str
    url: str


class ArticleResponse(BaseModel):
    article_title: str
    article_subtitle: str
    target_audience: str
    article_summary: str
    seo_description: str
    keywords: List[str]
    hashnode_tags: List[str]
    article_outline: List[str]
    full_article: str
    linkedin_post: str
    research_notes: List[ResearchItem]
    status: str


def get_env_value(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise HTTPException(
            status_code=500,
            detail=f"Missing environment variable: {name}"
        )

    return value


def research_topic(topic: str) -> List[ResearchItem]:
    """
    Simple public API research step using Wikipedia search.
    This can later be replaced by Tavily, SerpAPI, Azure AI Search, Bing Search, or another research API.
    """
    try:
        response = requests.get(
            "https://en.wikipedia.org/w/api.php",
            params={
                "action": "query",
                "list": "search",
                "srsearch": topic,
                "format": "json",
                "utf8": 1,
                "srlimit": 3,
            },
            timeout=10,
        )

        response.raise_for_status()
        data = response.json()

        results = []

        for item in data.get("query", {}).get("search", []):
            page_id = item.get("pageid")
            title = item.get("title", "")
            snippet = item.get("snippet", "").replace("<span class=\"searchmatch\">", "").replace("</span>", "")
            url = f"https://en.wikipedia.org/?curid={page_id}"

            results.append(
                ResearchItem(
                    title=title,
                    snippet=snippet,
                    url=url,
                )
            )

        return results

    except Exception:
        return []


def get_llm():
    api_key = get_env_value("AZURE_OPENAI_API_KEY")
    endpoint = get_env_value("AZURE_OPENAI_ENDPOINT")
    deployment = get_env_value("AZURE_OPENAI_DEPLOYMENT")
    api_version = get_env_value("AZURE_OPENAI_API_VERSION")

    return AzureChatOpenAI(
        azure_deployment=deployment,
        azure_endpoint=endpoint,
        api_key=api_key,
        api_version=api_version,
        temperature=0.4,
    )


@app.get("/")
def health_check():
    return {
        "status": "running",
        "service": "AI Article Generation Agent"
    }


@app.post("/generate-article", response_model=ArticleResponse)
def generate_article(request: ArticleRequest):
    research_notes = research_topic(request.topic)

    research_context = "\n".join(
        [
            f"Title: {item.title}\nSnippet: {item.snippet}\nURL: {item.url}"
            for item in research_notes
        ]
    )

    if not research_context:
        research_context = "No external research results were available. Write based on the user's topic and general technical knowledge. Do not invent sources."

    llm = get_llm()

    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                """
You must not invent sources, studies, links, or statistics.

Use the research context only as background. Do not copy it directly.

Write the full article in a discursive and human style.
Avoid excessive bullet points, numbered lists, and fragmented sections.
Do not use markdown heading symbols such as ###.
Use short section titles as plain text.
Create a strong introduction, a well-developed middle section, and a clear conclusion.
Make the reader identify with the topic.
Keep the article practical, professional, and natural.

Return a structured response matching the expected schema.
"""
            ),
            (
                "human",
                """
Topic:
{topic}

Language:
{language}

Target audience:
{audience}

Tone:
{tone}

Research context:
{research_context}

Create a complete article package with:
- article title
- article subtitle
- target audience
- article summary
- SEO description
- keywords
- Hashnode tags
- article outline
- full article with a human introduction, cohesive development, and clear conclusion, written in a discursive blog style without excessive bullet points or markdown heading symbols
- LinkedIn post to promote the article
- status as Draft
"""
            ),
        ]
    )

    structured_llm = llm.with_structured_output(ArticleResponse)

    chain = prompt | structured_llm

    result = chain.invoke(
        {
            "topic": request.topic,
            "language": request.language,
            "audience": request.audience,
            "tone": request.tone,
            "research_context": research_context,
        }
    )

    result.research_notes = research_notes
    result.status = "Draft"

    return result