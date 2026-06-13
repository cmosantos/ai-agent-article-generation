# Referência da API

## Endereço local

```text
http://127.0.0.1:8000
```

A documentação interativa do FastAPI fica disponível em:

```text
http://127.0.0.1:8000/docs
```

## Health check

### `GET /`

Resposta esperada:

```json
{
  "status": "running",
  "service": "AI Article Generation Agent"
}
```

## Gerar artigo

### `POST /generate-article`

Corpo da requisição:

```json
{
  "topic": "Como agentes de IA estão sendo usados no suporte técnico",
  "language": "Portuguese",
  "audience": "Profissionais de tecnologia e suporte",
  "tone": "Profissional, humano e prático"
}
```

Campos:

| Campo | Obrigatório | Valor padrão | Descrição |
|---|---:|---|---|
| `topic` | Sim | — | Tema principal do artigo |
| `language` | Não | `English` | Idioma da saída |
| `audience` | Não | `Technology professionals and learners` | Público-alvo |
| `tone` | Não | `Professional, human, practical` | Estilo de escrita |

Exemplo com `curl`:

```bash
curl -X POST "http://127.0.0.1:8000/generate-article" \
  -H "Content-Type: application/json" \
  -d '{
    "topic": "Local AI versus cloud AI",
    "language": "English",
    "audience": "Technology professionals",
    "tone": "Professional, practical and human"
  }'
```

## Estrutura da resposta

```json
{
  "article_title": "...",
  "article_subtitle": "...",
  "target_audience": "...",
  "article_summary": "...",
  "seo_description": "...",
  "keywords": ["..."],
  "hashnode_tags": ["..."],
  "article_outline": ["..."],
  "full_article": "...",
  "linkedin_post": "...",
  "research_notes": [
    {
      "title": "...",
      "snippet": "...",
      "url": "..."
    }
  ],
  "status": "Draft"
}
```

## Erros de configuração

Quando uma variável obrigatória do Azure OpenAI não está definida, a API retorna erro `500` indicando o nome da variável ausente.

Variáveis obrigatórias:

- `AZURE_OPENAI_API_KEY`
- `AZURE_OPENAI_ENDPOINT`
- `AZURE_OPENAI_DEPLOYMENT`
- `AZURE_OPENAI_API_VERSION`

## Segurança

Nunca publique o arquivo `.env` nem chaves de API. Use `.env.example` apenas como modelo e mantenha os segredos em variáveis de ambiente ou em um serviço de gerenciamento de segredos.
