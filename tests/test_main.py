import os
import unittest
from unittest.mock import Mock, patch

from fastapi import HTTPException

from app.main import ArticleRequest, get_env_value, health_check, research_topic


class TestHealthCheck(unittest.TestCase):
    def test_health_check_returns_running_status(self):
        result = health_check()

        self.assertEqual(result["status"], "running")
        self.assertEqual(result["service"], "AI Article Generation Agent")


class TestArticleRequest(unittest.TestCase):
    def test_uses_default_request_values(self):
        request = ArticleRequest(topic="Cloud computing")

        self.assertEqual(request.language, "English")
        self.assertEqual(request.audience, "Technology professionals and learners")
        self.assertEqual(request.tone, "Professional, human, practical")


class TestEnvironmentConfiguration(unittest.TestCase):
    def test_returns_existing_environment_variable(self):
        with patch.dict(os.environ, {"TEST_SETTING": "configured"}, clear=False):
            self.assertEqual(get_env_value("TEST_SETTING"), "configured")

    def test_raises_http_exception_when_variable_is_missing(self):
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaises(HTTPException) as context:
                get_env_value("MISSING_SETTING")

        self.assertEqual(context.exception.status_code, 500)
        self.assertIn("MISSING_SETTING", context.exception.detail)


class TestResearchStep(unittest.TestCase):
    @patch("app.main.requests.get")
    def test_converts_wikipedia_results_to_research_items(self, mock_get):
        response = Mock()
        response.raise_for_status.return_value = None
        response.json.return_value = {
            "query": {
                "search": [
                    {
                        "pageid": 123,
                        "title": "Artificial intelligence",
                        "snippet": "A <span class=\"searchmatch\">technical</span> summary",
                    }
                ]
            }
        }
        mock_get.return_value = response

        results = research_topic("Artificial intelligence")

        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].title, "Artificial intelligence")
        self.assertEqual(results[0].snippet, "A technical summary")
        self.assertEqual(results[0].url, "https://en.wikipedia.org/?curid=123")
        mock_get.assert_called_once()

    @patch("app.main.requests.get", side_effect=RuntimeError("network unavailable"))
    def test_returns_empty_list_when_research_fails(self, _mock_get):
        self.assertEqual(research_topic("Cloud computing"), [])


if __name__ == "__main__":
    unittest.main()
