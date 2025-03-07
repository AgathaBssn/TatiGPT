import os
import requests
import json

API_KEY = os.getenv("AIMLAPI_KEY")

class LlmClient:

    async def get_response(self, messages: list[dict[str, str]]) -> dict:
        if not API_KEY:
            raise ValueError("❌ API key is missing! Check your environment variables.")

        url = "https://api.aimlapi.com/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json",
        }

        payload = {
            "model": "meta-llama/Llama-Vision-Free",
            "messages": messages,  # Must contain at least one message
            "max_tokens": 512,
            "stop": "",  # Empty string as required
            "stream": False,
            "stream_options": {
                "include_usage": True
            },
            "n": 1,
            "seed": 1,
            "top_p": 1,
            "top_k": 1,
            "temperature": 1,
            "repetition_penalty": None,  # Must be `null`
            "logprobs": None,  # Must be `null`
            "echo": True,
            "min_p": 1,
            "presence_penalty": None,  # Must be `null`
            "frequency_penalty": None,  # Must be `null`
            "logit_bias": None,  # Must be `null`
            "tools": [
                {
                    "type": "function",
                    "function": {
                        "description": "",
                        "name": "",
                        "parameters": None  # Must be explicitly `null`
                    }
                }
            ],
            "response_format": {
                "type": "text"
            }
        }

        try:
            response = requests.post(url, headers=headers, json=payload)

            if response.status_code == 429:
                return {"error": "limit raised"}

            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"❌ API Request Failed: {e}")
            return {"error": str(e)}


llm_client = LlmClient()